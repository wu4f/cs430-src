# CS 430P/530: Internet, Web & Cloud Systems Code

This repository has the code examples used to show a Guestbook web application can be built and deployed in multiple ways on the Internet and on Cloud platforms.  The code is used in a sequence as part of this course: [CS 430P/530](http://thefengs.com/wuchang/courses/cs430)

```
.
├── 01_mvc_pylist
|     Original Python/Flask Guestbook application using Python list model
|     done in an MVC architecture with pluggable model backends
├── 02_mvp_modules_sqlite3
|     Python/Flask Guestbook application done in an MVP style architecture
├── 03_nginx_uwsgi_certbot
|     nginx/uwsgi-based version of Guestbook using SQLite3 model
├── 04_container_dockerhub
|     Container version of Guestbook using Python list model
├── 05_computeengine_appengine_datastore
|     Serverless version of Guestbook using AppEngine and Cloud Datastore
|     Used to also run Compute Engine and Cloud Datastore version as well
├── 05_ec2_ddb_cloud9_docker_ecs
|     EC2/Cloud9, EB, and ECS versions with DynamoDB model
├── 06_cloudrun
|     Container version of Guestbook for Cloud Run using a Cloud Datastore model
├── 07_gcr_kubernetesengine
|     Kubernetes version of Guestbook using Container Registry and Cloud Datastore
└── 08_restapi_cloudfunctions
      REST API version of Guestbook using Cloud Functions, Cloud Datastore
```
