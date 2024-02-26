# webex-afk
a simple service to save your time from boring meeting

**do not use it since it's still WIP!!!**
## how to use
### requirements
* linux
* docker
### setup configuration
create a file named `user_info.json` and filled in the following content
```json
{
    "name":"test",
    "email":"test@gmail.com",
    "url":"https://your-boriung-meet",
    "day":"friday",
    "time":"23:31",
    "dc_webhook":"<this is optional, for uploading screen shot via discord webhook>"
}
```
note here again, `dc_webhook` is **optional**. you can just **delete this key-value pair** if you do not care about proof of your bot
### run
* `sudo apt install -y linux-modules-extra-`uname -r` && sudo modprobe binder_linux devices="binder,hwbinder,vndbinder"`
* `sudo docker compose up -d`
* enjoy your afk service :P
### GCP support
1. create `user_info.json` and run `gcloud init` for your GCP project
2. run `create_gcp.ps1`
3. enjoy your afk service :P
