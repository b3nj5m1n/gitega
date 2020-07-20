# gitega

Regularly execute script to keep a local copy of the stats of all your public github repos.

## Requirements

Install using this command:
`pip install -r requirements.txt`

## Authentication

Generate a personal access token (Settings -> Developer Settings -> Personal Access Tokens -> Generate new token) with all repo permissions.

## Add a new account

Run addAccount.py to add a new account:
`addAccount.py --name YourUserName --token YourAccessToken`

## Save location

All data (Including the access token) is saved in the gitega directory in your home directory.
