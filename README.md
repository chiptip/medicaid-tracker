# Medical Trust Tracker

this application will link the trust's debit card using Plaid, then prompt the user to upload receipts and store the purpose for audit purposes.


Plaid integration
Web UI file upload

## dev

to run app:

1. bootstrap environment variables
```commandline
cd web
source ./bootstrap.sh
```
2. start up Flask server in development mode
```commandline
flask --app app run --debugger
```
