import sqlite3
import accountManager
import os
import json
from dateutil import parser as dateParser
import logger


class parser:
    def __init__(self, account):
        self.account = account
        self.logger = logger.logger()

    def __connectDB(self):
        self.connection = sqlite3.connect(
            os.path.join(self.account.getAccDir(), "traffic.db"))
        self.cursor = self.connection.cursor()

    def __disconnectDB(self):
        self.connection.commit()
        self.connection.close()

    def __ensureTables(self):
        # Make sure a table exists for each repository
        for repo in self.account.getLocalRepos():
            self.cursor.execute(
                f'''CREATE TABLE IF NOT EXISTS
                "{repo}"(time date, viewsCount int, viewsUniq int, clonesCount int, clonesUniq int,
                UNIQUE(time));''')

    def parseRepo(self, repoName, keepBackup=True):
        # Views
        dataDir = os.path.join(self.account.getAccDir(),
                               "statsData", repoName, "views")
        parsedDataDir = os.path.join(dataDir, ".parsed")
        reports = [os.path.join(dataDir, f) for f in os.listdir(
            dataDir) if os.path.isfile(os.path.join(dataDir, f))]
        for report in reports:
            # Open one json file at a time, move it to .parsed directory after parsing
            reportFile = open(report, "r")
            try:
                reportData = json.load(reportFile)
                reportFile.close()
                for timestamp in reportData["views"]:
                    date = dateParser.parse(timestamp["timestamp"])
                    count = timestamp["count"]
                    uniq = timestamp["uniques"]
                    self.cursor.execute(
                        f'''INSERT OR IGNORE INTO '{repoName}' (time, viewsCount, viewsUniq)
                        VALUES ('{date}', '{count}', '{uniq}') ''')
                    self.cursor.execute(
                        f'''UPDATE '{repoName}' SET viewsCount = '{count}', viewsUniq = '{uniq}' WHERE time ='{date}' ''')
                if keepBackup:
                    if not os.path.exists(parsedDataDir):
                        os.makedirs(parsedDataDir)
                    os.rename(report, os.path.join(
                        parsedDataDir, os.path.basename(report)))
            except json.JSONDecodeError as err:
                print(f"There was an error parsing views for {report}")
            except KeyError as err:
                print(f"There was an error parsing views for {report}")
        # Clones
        dataDir = os.path.join(self.account.getAccDir(),
                               "statsData", repoName, "clones")
        parsedDataDir = os.path.join(dataDir, ".parsed")
        reports = [os.path.join(dataDir, f) for f in os.listdir(
            dataDir) if os.path.isfile(os.path.join(dataDir, f))]
        for report in reports:
            # Open one json file at a time, move it to .parsed directory after parsing
            reportFile = open(report, "r")
            try:
                reportData = json.load(reportFile)
                reportFile.close()
                for timestamp in reportData["clones"]:
                    date = dateParser.parse(timestamp["timestamp"])
                    count = timestamp["count"]
                    uniq = timestamp["uniques"]
                    self.cursor.execute(
                        f'''INSERT OR IGNORE INTO '{repoName}' (time, clonesCount, clonesUniq)
                        VALUES ('{date}', '{count}', '{uniq}') ''')
                    self.cursor.execute(
                        f'''UPDATE '{repoName}' SET clonesCount = '{count}', clonesUniq = '{uniq}' WHERE time ='{date}' ''')
                if keepBackup:
                    if not os.path.exists(parsedDataDir):
                        os.makedirs(parsedDataDir)
                    os.rename(report, os.path.join(
                        parsedDataDir, os.path.basename(report)))
            except json.JSONDecodeError as err:
                print(f"There was an error parsing clones for {report}")
            except KeyError as err:
                print(f"There was an error parsing clones for {report}")

    def parse(self):
        self.__connectDB()
        self.__ensureTables()
        for repo in self.account.getLocalRepos():
            self.logger.log(f"Parsing {repo}.")
            self.parseRepo(repo)
        self.__disconnectDB()
