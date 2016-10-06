ATZbot [![Build Status](https://travis-ci.org/ChristopherIMeyers/ATZbot.svg?branch=master)](https://travis-ci.org/ChristopherIMeyers/ATZbot)
========================

This repo contains the script that runs for the mods on reddit.com/r/allthingszerg to update the sidebar with stream information.


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

TODO
* more tests
