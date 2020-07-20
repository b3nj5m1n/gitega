import account_manager
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
parser.add_argument("--token", required=True)
args = parser.parse_args()
print(args.name)

account = account_manager.account(args.name)
account.setToken(args.token, True)
