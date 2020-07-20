import os
import requests
import account_manager
import logger
from datetime import datetime


class statistics:
    def __init__(self, account):
        self.account = account
        self.logger = logger.logger

    def update(self):
        dataDir = os.path.join(self.account.getAccDir(), "statsData")
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)
        data = requests.get('https://api.github.com/repos/' + self.account.accountName + '/' + "dotfiles" + '/traffic/views',
                            auth=(self.account.accountName, self.account.getToken()))
        with open(os.path.join(dataDir, datetime.now().strftime("%d_%m_%y__%H_%M_%S.json")), "wb") as file:
            file.write(data.content)
        self.logger.log(str(data.content))


s = statistics(account_manager.account("b3nj5m1n"))
# s.account.update()
s.update()
