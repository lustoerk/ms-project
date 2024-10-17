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