ATZbot [![Build Status](https://travis-ci.org/ChristopherIMeyers/ATZbot.svg?branch=master)](https://travis-ci.org/ChristopherIMeyers/ATZbot)
========================

This repo contains the script that runsfor the mods on reddit.com/r/allthingszerg to update the sidebar with stream information.  The project is setup so it can handle new additional scripts later on as needed.



Update Script on Server
---
```bash
cp ATZbot/settings.py settings.py
rm -r ATZbot
wget https://github.com/ChristopherIMeyers/ATZbot/archive/master.zip
unzip master.zip
rm master.zip
mv ATZbot-master ATZbot
mv settings.py ATZbot/settings.py
```




settings.py (untracked)
* contains all of the (private) configurations (username/passwords)
* example below

```python
reddituser = "automaton2000"    
redditpass = "secretpass"    
```


streamsbot.py
* uses settings.py
* script that pulls twitch stream information and pipes it to the atz sidebar every X minutes

jaedong.py
* uses settings.py
* script that pulls twitch stream information and pipes it to the r/jaedong sidebar every X minutes



TODO
* automatic flair updating
* consolidate code 
* more tests
