#!/usr/bin/env bash

sudo echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install mysql-server-5.7
mysql --version
