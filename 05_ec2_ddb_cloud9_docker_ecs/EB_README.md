Configure  aws-elasticbeanstalk-ec2-role=> AmazonDynamoDBFullAccess

./
  application.py -> do not specify port in app.run, change name to application
  Dockerfile -> specify application:application
  requirements.txt (flask, boto3, awsebcli)


rm .ebignore
echo "env" > .ebignore
echo "__pycache__" >> .ebignore
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
eb init -p python-3.6 gb --region us-east-1
eb create myguestbook-env

On update run
  eb deploy
