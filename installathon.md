# Installathon

This guide will lay out the requirements for the computing for social sciences class.

## Everybody
Everybody needs to sign up for a [Github](github.com) account, and put then fill out [this form](https://docs.google.com/forms/d/1PHhWIvkBj8nO0YNOT_R87BiQ9XvyBcp0PrMvGhCcuwo/viewform).

## Mac Users
Mac Users will need to install the [Anaconda Python Distrobution](http://continuum.io/downloads). Make sure to install python 2.7 and click `yes` when asked to override your `.bash_profile` 

You will also need to install mysql server. [Download](http://dev.mysql.com/downloads/mysql/) and install the .dmg package. 

## Windows Users
Because Windows isn't a Unix system, we provide a Vagrant Box for building a Virtual Machine (that is , a linux machine running inside your system) with the require dependencies. To do so, follow the instructions below. 

1. Install [Vagrant](https://www.vagrantup.com/)
2. [Download](https://github.com/hunterowens/cssVagrantBox/archive/master.zip) and unzip the Vagrant Box.
2. Run `vagrant plugin install vagrant-fabric` from a Command Prompt. 
3. Run `vagrant up` (will take a long time). Make sure that you are in the directory that you unziped the box to before running this. To check, run the `ls` (list) command. If the output has a file called `Vagrantfile`, then you are good to go. If not, us the `cd` (change directories) command to navagate to the folder. 

Congrats! You can now run `vagrant ssh` to access your Vagrant Virtual Machine.

## Problems?
We will be holding extended office hours on Wednesday to help you work through any issues you may have with this. 

