# Minerva
### Description
Minerva aims to be an anti-spam system for bot-following or "botting" events.

The system collects the latest followers and leaves them in a waiting queue for the streamer or a moderator to accept them, in this way it ensures that they are not false, nor overload the list of alert events saturating with unnecessary animations, thus being able to, group users in predefined numbers for your welcome.

Those who use this tool should be careful to keep the admission list updated to avoid dropping a user along with fake accounts.

### Installation
It uses native libraries and "requests" for GET and POST requests, and imports a file where the access data to the Twitch api are defined.

Requirement installation:
```
pip install requests
```

### Pending tasks
- [x] Use the twitch api to get a list of followers.
- [ ] Configure mysqli to only check new followers.
- [ ] Generate mass admission interface.
- [ ] Generate automatic detection script based on time.
- [ ] Be able to use it as a proxy for streamlabs alerts
(with streamlabs api, sending the corresponding event, previously accepted).
- [ ] ¿Render interface in OBS panel?.

### ETA?
Unfortunately there is no ETA, although it is a priority for me to finish it, I have to meet other obligations and therefore I cannot establish an ETA as an independent developer.

### Contact / Tips
If you want to contribute in any way to the project, get in touch through [the discord server!](https://discord.gg/6827xmkuQh) Thanks.
