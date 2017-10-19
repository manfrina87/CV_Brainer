#!/bin/bash


# check arguments number
if [ $# -ne 1 ]; then
    echo "Error: wrong number of parameters"
    echo "Usage: ./install_CVapp.sh requirements.txt"
    exit 1
fi

#install basic dependencies
sudo apt-get update
sudo apt-get install python python-dev
sudo apt-get install python-pip
sudo pip install --upgrade pip

#install and activate virtualenv
sudo pip install virtualenv
sudo virtualenv ~/dlenv
source ~/dlenv/bin/activate

#install app dependencies
sudo pip install -r $1
sudo python setup.py

#install jupyter notebook
sudo -H pip install jupyter
cp json_formatter.py ~/.ipython/profile_default/startup/json_formatter.py
cp json_formatter.css ~/.ipython/profile_default/startup/json_formatter.css

#NLTK DATA install
#sudo python -c "import nltk; nltk.download('punkt')"
