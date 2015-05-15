SlackIt
---

A Linux deamon that tells you when there are new messages on Slack

configure
---

open config.py file and set the right access token at this line:
```bash
slack_team_token = "" 	# token available here: https://api.slack.com/tokens
```

Start, stop or restart deamon
---
Simply run:
```bash
sudo python slackit.py start | stop | restart
```
