import os
import requests
import accountManager
import logger
from datetime import datetime


class statistics:
    def __init__(self, account):
        self.account = account
        self.logger = logger.logger

    def updateAllRepos(self):
        self.logger.log("Starting full update.")
        for repo in self.account.getUpstreamRepos():
            self.updateRepo(repo)

    def updateRepo(self, repoName):
        self.logger.log("Updating " + repoName + ".")
        # Views
        dataDir = os.path.join(self.account.getAccDir(),
                               "statsData", repoName, "views")
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)
        data = requests.get('https://api.github.com/repos/' + self.account.accountName + '/' + repoName + '/traffic/views',
                            auth=(self.account.accountName, self.account.getToken()))
        with open(os.path.join(dataDir, datetime.now().strftime("%d_%m_%y__%H_%M_%S.json")), "wb") as file:
            file.write(data.content)
        # Clones
        dataDir = os.path.join(self.account.getAccDir(),
                               "statsData", repoName, "clones")
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)
        data = requests.get('https://api.github.com/repos/' + self.account.accountName + '/' + repoName + '/traffic/clones',
                            auth=(self.account.accountName, self.account.getToken()))
        with open(os.path.join(dataDir, datetime.now().strftime("%d_%m_%y__%H_%M_%S.json")), "wb") as file:
            file.write(data.content)

