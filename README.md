# Sup Bot

Credits: [NLR Programming](https://www.youtube.com/channel/UC1D390f71viXSzv3JLe-yHw)

Easy and Simple Supreme bot that parses the DOM of the site and automates clicking and typing! I plan on to expand more on this program such as adding a UI and a proxy feature.

**NOTE**: Use this at your own risk, I am merely creating this for educational purposes.

## Installation
---
* Clone the directory in any given path you want.
```
git clone https://github.com/herropaul/supremeBot
```
* Make sure to install the required libraries in **requirements.txt**
```
pip install -r requirements.txt
```
* For my **Chrome** users, be sure to download a [Chrome Driver](https://chromedriver.chromium.org/downloads) to open up the chrome browser with the bot. Here's how it should look like to access the chrome driver
```
from splinter import Browser
executable_path = {'executable_path': r'/path/to/chromedriver'}

browser = Browser('chrome', **executable_path)
```
* For **Firefox** users, there's no need to download a driver. The **Browser** instance will look like this
```
from splinter import Browser
browser = Browser('firefox')
```

## Deployment
---
Currently there is only 1 file required to start the bot, bot.py. To access the script, make sure you are in the correct directory where the file is and run:
```
python bot.py
```

Before starting, make sure to edit the INFO dictionary such as: **product**, **color**, **size**, and **category** to choose the correct product you want.

## Demo
---
![demoGif](https://im4.ezgif.com/tmp/ezgif-4-3326c3bf39da.gif)

## TODO
---
* [ ] Add proxy feature
* [ ] Add User Interface
* [ ] Update cleaner code
