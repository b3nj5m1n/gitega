import sqlite3
import csv
import argparse
import os
import accountManager
from dateutil import parser as dateParser


class csvExport:
    def __init__(self, account):
        self.account = account
        self.data = []

    def __connectDB(self):
        self.connection = sqlite3.connect(
            os.path.join(self.account.getAccDir(), "traffic.db"))
        self.cursor = self.connection.cursor()

    def __disconnectDB(self):
        self.connection.commit()
        self.connection.close()

    def getData(self, repoName):
        self.__connectDB()
        self.cursor.execute(
            f'''SELECT * from {repoName}''')
        data = self.cursor.fetchall()
        self.__disconnectDB()
        for day in data:
            days = (dateParser.parse(day[0]).strftime("%Y-%m-%d"))
            viewsCount = (int(day[1]) if day[1] else 0)
            viewsUniq = (int(day[2]) if day[2] else 0)
            clonesCount = (int(day[3]) if day[3] else 0)
            clonesUniq = (int(day[4]) if day[4] else 0)
            self.data.append([days, viewsCount, viewsUniq, clonesCount, clonesUniq])

    def writeData(self, filename, echo=False):
        if echo:
            for row in self.data:
                print(row)
        else:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in self.data:
                    writer.writerow(row)


parser = argparse.ArgumentParser(description='Extract the data of the repository of an account to a csv file for further processing.')
parser.add_argument('accountName', metavar='N', type=str,
                    help='Account name.')
parser.add_argument('repositoryName', metavar='R', type=str,
                    help='Respository name.')
parser.add_argument("--rootDir", required=True)
parser.add_argument("--output", required=False)
parser.add_argument("--pipe", default=True, action=argparse.BooleanOptionalAction)

args = parser.parse_args()
account = accountManager.account(args.accountName, rootDir=args.rootDir)
exporter = csvExport(account)
exporter.getData(args.repositoryName)
exporter.writeData(args.output, args.pipe)

