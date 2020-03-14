# REST API: Lambda, API Gateway, CDK

A version of the guestbook app with a separate frontend and backend. The client calls a REST API to add and get guestbook entries.

## Setup

Install the [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) and [specify your credentials and region](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_credentials). This README assumes you are using your default profile, but you can use another profile with the `--profile` flag.

In the `restapi` directory, set up a Python virtual environment and install the requirements:

```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

Bootstrap CDK for the region you will be working in:

```
cdk bootstrap
```

Deploy the REST API:

```
cdk deploy
```

Note the `RestApiStack.ApiGatewayEndpoint` printed at the end of the deply and replace the `<FMI>` in `frontend/statis/guestbook.js` with the it.

The client can be run locally or deployed to S3.


