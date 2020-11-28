import argparse
import accountManager
import statistics
import parser

argParser = argparse.ArgumentParser()
argParser.add_argument("--name", required=True)
argParser.add_argument("--rootDir", required=False)
args = argParser.parse_args()

account = accountManager.account(args.name, "github", args.rootDir)
stats = statistics.statistics(account)

stats.updateAllRepos()

parser = parser.parser(account)
parser.parse()
