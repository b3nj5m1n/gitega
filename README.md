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

Use update.sh to automatically update all your accounts and send a report to you via email. Call the script with the path to your .gitega directory and your email (Will be used to send & receive, requires you to have msmtp set up)
Put something like this (This one will run at 17:00 every day) in your crontab file (Using crontab -e):
`0 17 * * * bash /home/YourUserName/Documents/Github/gitega/update.sh "/home/YourUserName/.gitega" "YourEmailAdress"`

Regularly run update.py to update all traffic data for all repositorys of an account.
`python update.py --name YourUserName`

This will also parse the data and store it in an sql lite database.

## Save location

All data (Including the access token) is saved in the gitega directory in your home directory.
