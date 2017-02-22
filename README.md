# Aquapilot Raspberry PI
RaspberryPI relay that will communicate with the cloud.

## Quick Summary ##

* Prerequisites
* How to install
* How to configure
* How to run it
* Contribute

### Prerequisites ###

Well in order to be able to run this project  on your raspberry pi the following requirements need to get achieved :

* Your raspberry pi have Raspbian installed on it. (For now it is the only one supported OS)
* Python is installed on your raspberry pi.
* Pip is installed too (`sudo apt-get install python-pip`)

### How to install ###

Clone the project in `/home/pi/aquapilot` folder:
`git clone https://github.com/aquapilot/aquapilot-raspberry-pi.git`

Install the dependencies:
`sudo pip install yaml firebase serial time json`

Allow script to get executed:
`sudo chmod +x aquapilot-raspberry.py`

### How to configure ###
Go into `src` folder and rename the `config.sample.yml` file into `config.yml`.

Edit the config.yml file and fill up your firebase database informations.

### How to run it ###

You have two options to run it:

1) Run it autmatically when the raspberry pi is started
@TODO

2) Run it manually (for testing purposes)
`python publish.py`

### Contribute ###
I am really not an expert in python and would be happy if you could improve this code according to the coding guidelines
and also with startup scripts etc.

Good nothing more to say for now. You are welcome too contribute