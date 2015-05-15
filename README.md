SlackIt
---

A Linux deamon that tells you when there are new messages on Slack

Configure
---

open config.py file and set the right access token at this line:
```bash
slack_team_token = "" # token available here: https://api.slack.com/web
```
in the same file you'll find some variables to set
```bash
log_file = "/var/log/slackify.log"
channels = "dev"													      
notification_time_appear = 10										
check_notification_time = 20
```
* log_file: log file path for the system monitoring
* channels: a list of channels to check (at the moment only one is supported)
* notification_time_appear: how much time the notification should stay visible
* check_notification_time: when the deamon have to check new messages on Slack


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
