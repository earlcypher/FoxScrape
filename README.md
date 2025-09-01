# Project FoxScrape
    - FoxScrape v1.0
    - Created by Lei

## Table of Contents
    - [Project FoxyScrape](#project)
    - [Table of Contents](#table)
    - [Installation](#installation)
    - [Termux Installation](#termux)
    - [Linux Installation](#linux)
    - [Conclusion](#conclusion)

## Installation
    Must having a latest version of Python or Python3.
    
    For the linux application it depends on you, but make sure it's compatible
    with Python
    
    For the instance we have a two system operation option to use Pc/Android:
    
    - [Termux Installation](#termux)
    - [Any Debian based Linux Installation](#linux)

## Termux Installation

    - Update & Upgrade the Termux Packages
    ```
    pkg update && pkg upgrade -y
    ```
    - Installing dependencies 
    ```
    pkg install python git python-requests python-pandas python-wheel -y && pip
    install threading
    ```
    - Cloning repository from FoxScrape repository
    ```
    git clone 
    ```
    - Run the script
    ```
    cd FoxyScrape && python foxscrape.py
    ```
    
## Linux Installation
    - Installing dependencies
    ```
    apt-get update && apt-get upgrade -y && apt install python3 git
    python-pandas python-requests python-wheel && pip install threading
    ```
    - Run the script
    ```
    cd FoxyScrape && python3 foxyscrape.python3
    ```
    
# Conclusion 
    Purpose of this script is to make user help to scrap a proxy from a web.