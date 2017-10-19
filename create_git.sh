#!/bin/bash

#install GIT
sudo apt-get install git

##Create a git project from an existing folder
sudo git config --global user.name "Martina"
sudo git config --global user.email "martina.manfrin87@gmail.com"
#cd CV_app
sudo git init
sudo git remote add origin https://gitlab.com/Manfrin/CV_app.git
sudo git add .
sudo git commit -m "FIRST COMMIT"
sudo git push -u origin master



