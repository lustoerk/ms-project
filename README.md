# ms-project
microservices project - practice  
based on the freeCodeCamp Course ["Microservice Architecture with Python & K8s"](https://www.youtube.com/watch?v=hmkF77F9TLw)

email: msarch.dummy.2024@gmail.com

- install mysql and mongodb locally!!!
- run minikube and use minikube tunnel to connect
- build images directly in minikube and reference accordingly - `minikube image build -t gateway -f Dockerfile .` > `image: library/gateway` - and force local usage with `imagePullPolicy: Never`
- issuese with python + pylance + vsc? Dont create venv's per dir, but create it on the workspace level
- use mongosh: show databases - use mp3s - db.fs.files.find()
- download a short from yt and reduce to 10s, brew install yt-dlp


# Tasks


## Improve readde
- describe minikube build setup
- remove venv directories, reduce to onee
- store seecret secretly
- explain deployment process


## Migrate MongoDB into container
## Migrate MySQL into container

- install helm: `brew install helm`
- setup the repo: `helm repo add bitnami https://charts.bitnami.com/bitnami && helm repo update`
- prepare dir: `mkdir -p mysql/manifests && cd mysql/manifests`
- get values to configure mysql: `helm show values bitnami/mysql >> helm-values.yaml`
- create `initdb.yaml` from previous init.sql
- install chart with custom script: `helm install mysql bitnami/mysql -f initdb.yaml`
- validate sucessful init: 
    ```
    MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace default mysql -o jsonpath="{.data.mysql-root-password}" | base64 -d)

    kubectl run mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.4.3-debian-12-r0 --namespace default --env MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --command -- bash

    mysql -uroot -hmysql -p$MYSQL_ROOT_PASSWORD
    show databases;
    use auth; 
    show tables;
    select * from user;
    ```
- fix app to use other database

## helmifyf stuff and host the heelm chart repo
https://helm.sh/docs/topics/chart_repository/#github-pages-example


# Architecture

## Auth
[Another example](https://www.kdnuggets.com/2021/02/deploy-flask-api-kubernetes-connect-micro-services.html)
[Create login and register form](https://codeshack.io/login-system-python-flask-mysql/)

## Gateway
## Converter
## Rabbit
## Notifiication
## Mysql
setup issues
- the non-root user that compares the credentials with the mysql db didnt have access: `CREATE USER 'auth_user'@'%' IDENTIFIED BY 'Aauth123';` was set to @localhost, which only allows access from the same machine. After fixing this, i needed to remove the pvc.
## MongoDB