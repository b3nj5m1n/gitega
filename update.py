import argparse
import accountManager
import statistics
import parser

argParser = argparse.ArgumentParser()
argParser.add_argument("--name", required=True)
args = argParser.parse_args()

account = accountManager.account(args.name)
stats = statistics.statistics(account)

# stats.updateAllRepos()

parser = parser.parser(account)
parser.parse()
parser.parseRepo("dotfiles")
