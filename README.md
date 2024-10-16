# ms-project
microservices project - practice

install mysql and mongodb locally!!!
run minikube and use minikube tunnel to connect
build images directly in minikube and reference accordingly - `minikube image build -t gateway -f Dockerfile .` > `image: library/gateway` - and force local usage with `imagePullPolicy: Never`
