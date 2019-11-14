CS 430P/530: Internet, Web & Cloud Systems Code

This repository has the code examples used to show a Guestbook web application can be
built and deployed in multiple ways on the Internet and on Cloud platforms.  The code
is used in a sequence as part of this course:
http://thefengs.com/wuchang/courses/cs430

.
├── WebDev_Guestbook_v1_pylist
|     Original Python/Flask Guestbook application using Python list model
|     done in an MVC architecture with pluggable model backends
├── WebDev_Guestbook_v2_modules_mvp
|     Python/Flask Guestbook application done in an MVP style architecture
├── WebDev_Guestbook_v3_nginx_uwsgi
|     nginx/uwsgi-based version of Guestbook using SQLite3 model
├── WebDev_Guestbook_v4_datastore
|     Serverless version of Guestbook using AppEngine and Cloud Datastore
├── Container_Guestbook
|     Container version of Guestbook using Python list model
├── Container_Guestbook_Kubernetes
|     Kubernetes version of Guestbook using Container Registry and Cloud Datastore
├── Container_Guestbook_Serverless
|     Container version of Guestbook for Cloud Run using a Cloud Datastore model
└── API_Functions_Guestbook
      REST API version of Guestbook using Cloud Functions, Cloud Datastore

