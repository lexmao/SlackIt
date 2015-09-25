SlackIt
---

A Linux deamon that tells you when there are new messages on Slack

![Alt text](http://i.imgur.com/kpic5N1.png)

Configure
---

open config.py file and set the right access token at this line:
```bash
slack_team_token = "" # token available here: https://api.slack.com/web
```
in the same file you'll find some variables to set
```bash
log_file = "/var/log/slackit.log"
notification_time_appear = 10										
```
* log_file: log file path for the system monitoring
* notification_time_appear: how much time the notification should stay visible

Start, stop or restart deamon
---
Simply run:
```bash
sudo python slackit.py start | stop | restart
```
Credits
---
SlackIt uses @serverdensity python-daemon class to run the Linux daemon

https://github.com/serverdensity/python-daemon
