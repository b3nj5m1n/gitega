# gitega

Regularly execute script to keep a local copy of the stats of all your public github repos.

## Requirements

Install using this command:
`pip install -r requirements.txt`

## Authentication

Generate a personal access token (Settings -> Developer Settings -> Personal Access Tokens -> Generate new token) with all repo permissions.

## Add a new account

Run addAccount.py to add a new account:
`python addAccount.py --name YourUserName --token YourAccessToken`

## Update data

Regularly run update.py to update all traffic data for all repositorys of an account.
`python update.py --name YourUserName`

## Parse data

Running parser.py will parse all new collected stats data and save it to an sql lite database.

## Save location

All data (Including the access token) is saved in the gitega directory in your home directory.
