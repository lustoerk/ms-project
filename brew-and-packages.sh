#!/bin/bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew tap mongodb/brew && brew update
brew install docker kubernetes-cli k9s minikube mysql mysql-client mongodb-community
# brew install pkg-config // this is a bugfix when installing flask-mysqldb