ATZbot [![Build Status](https://travis-ci.org/ChristopherIMeyers/ATZbot.svg?branch=master)](https://travis-ci.org/ChristopherIMeyers/ATZbot)
========================

This repo contains all of the scripts that run for the mods on reddit.com/r/allthingszerg.


settings.py (untracked)
* contains all of the (private) configurations (username/passwords)
* example below

```python
reddituser = "automaton2000"    
redditpass = "secretpass"    
```


flairbot.py
* uses settings.py
* script that pulls twitch stream information and pipes it to the atz sidebar every X minutes



TODO
* automatic flair updating
* consolidate code 
* tests
* travis.ci
