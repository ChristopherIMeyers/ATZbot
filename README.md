ATZbot [![Build Status](https://travis-ci.org/ChristopherIMeyers/ATZbot.svg?branch=master)](https://travis-ci.org/ChristopherIMeyers/ATZbot)
========================

This repo contains the script that runs for the mods on reddit.com/r/allthingszerg to update the sidebar with stream information.

Update AWS Server
---
```bash
sudo yum install python27
sudo yum install python27-pip
sudo python27 -m pip install praw
```

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

Crontab 
---
```bash
MAILTO=*********
*/30 * * * * python27 /home/ec2-user/ATZbot/streamsbot.py
```

Files
---

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

