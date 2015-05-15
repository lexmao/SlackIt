SlackIt
---

A Linux deamon that tells you when there are new messages on Slack

Configure
---

open config.py file and set the right access token at this line:
```bash
slack_team_token = "" # token available here: https://api.slack.com/web at the "Authentication" section.
```

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
