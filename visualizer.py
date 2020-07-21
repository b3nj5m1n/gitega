import matplotlib.pyplot as pyplot
import datetime
import sqlite3
import os
import accountManager
from dateutil import parser as dateParser
import mpld3


class visualizer:
    def __init__(self, account):
        self.account = account
        self.days = []
        self.viewsCount = []
        self.viewsUniq = []
        self.clonesCount = []
        self.clonesUniq = []

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
            self.days.append(dateParser.parse(day[0]))
            self.viewsCount.append(int(day[1]) if day[1] else 0)
            self.viewsUniq.append(int(day[2]) if day[2] else 0)
            self.clonesCount.append(int(day[3]) if day[3] else 0)
            self.clonesUniq.append(int(day[4]) if day[4] else 0)

    def plotWeb(self):
        pyplot.style.use('dark_background')
        fig = pyplot.figure()
        ax = fig.gca()
        ax.plot(self.days, self.viewsCount, "#ff0066")
        ax = fig.gca()
        ax.plot(self.days, self.viewsUniq, "#00ff66")
        mpld3.show(fig)

    def plotImg(self, imageDir):
        pyplot.style.use('dark_background')
        # Views
        fig = pyplot.figure()
        ax = fig.gca()
        ax.plot(self.days, self.viewsCount, "#ff0066")
        ax = fig.gca()
        ax.plot(self.days, self.viewsUniq, "#00ff66")
        ax.grid(True)
        fig.savefig(os.path.join(imageDir, "views.png"))
        # Clones
        fig = pyplot.figure()
        ax = fig.gca()
        ax.plot(self.days, self.clonesCount, "#ff0066")
        ax = fig.gca()
        ax.plot(self.days, self.clonesUniq, "#00ff66")
        ax.grid(True)
        fig.savefig(os.path.join(imageDir, "clones.png"))


account = accountManager.account("b3nj5m1n")
vis = visualizer(account)
vis.getData("dotfiles")
# vis.plotWeb()
vis.plotImg("plots")

# year = [datetime.datetime(2000, 1, 1),
#         datetime.datetime(2005, 1, 1),
#         datetime.datetime(2010, 1, 1),
#         datetime.datetime(2015, 1, 1)]
# pop = [0, 10, 0, 20]

# plt.scatter(year, pop)
# plt.show()
