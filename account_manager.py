import requests
import os
import logger


class account:
    def __init__(self, accountName, accountType="github", rootDir="~/.gitega"):
        self.logger = logger.logger()
        self.accountName = accountName
        self.accountType = accountType
        self.rootDir = rootDir

    def getAccDir(self):
        self.accDir = os.path.join(
            str(os.path.expanduser(self.rootDir)), self.accountName + "-" + self.accountType)
        if not os.path.exists(self.accDir):
            os.makedirs(self.accDir)
        return self.accDir

    def __getTokenPath(self):
        return os.path.join(self.getAccDir(), "access", "token.txt")

    def getToken(self):
        if os.path.exists(self.__getTokenPath()):
            with open(self.__getTokenPath(), "r") as file:
                return file.readline()
        else:
            return False

    def setToken(self, token, override=False):
        tokenPath = self.__getTokenPath()
        if not os.path.exists(os.path.join(self.getAccDir(), "access")):
            os.makedirs(tokenPath)
        if not "".__eq__(self.getToken()) or override:
            with open(tokenPath, "w") as file:
                file.write(token)
        else:
            self.logger.log("Could not write token.")