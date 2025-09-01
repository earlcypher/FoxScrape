# FoxyScrape v1.0

A Python-based web scraping tool designed to extract proxy information from websites.

### Created by Lei

## Table of Contents

· [Installation](#install)
· [Termux Installation](#termux)
· [Linux Installation](#linux)
· [Usage](#usage)
· [Purpose](#purpose)

## Installation (#install)

Ensure you have the latest version of Python or Python3 installed. This tool is compatible with both PC and Android systems.

### Choose your installation method:

· Termux (Android)
· Linux Systems

## Termux Installation {#termux}

1. Update & Upgrade Termux Packages
   ```bash
   pkg update && pkg upgrade -y
   ```
2. Install Dependencies
   ```bash
   pkg install python git python-requests python-pandas python-wheel -y
   pip install threading
   ```
3. Clone Repository
   ```bash
   git clone https://github.com/yourusername/FoxyScrape.git
   ```
4. Run the Script
   ```bash
   cd FoxyScrape
   python foxscrape.py
   ```

## Linux Installation {#linux}

1. Install Dependencies
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   sudo apt install python3 git python3-pandas python3-requests python3-wheel
   pip install threading
   ```
2. Clone Repository
   ```bash
   git clone https://github.com/yourusername/FoxyScrape.git
   ```
3. Run the Script
   ```bash
   cd FoxyScrape
   python3 foxscrape.py
   ```

## Usage {#usage}

After installation, navigate to the FoxyScrape directory and execute the script:

```bash
python foxscrape.py
```

or

```bash
python3 foxscrape.py
```

# Purpose {#purpose}

This script is designed to help users scrape proxy information from various websites, providing an easy way to gather proxy data for various applications.
