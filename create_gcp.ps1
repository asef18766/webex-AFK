$VM_NAME="webxafk"
$NETWOK_NAME="webxafk-net"
$SSH_PUB_KEY="~/.ssh/id_rsa.pub"
<#
gcloud compute networks create $NETWOK_NAME

# this port is for debug purpose, it's optionial and recommanded disable by default
gcloud compute firewall-rules create allow-webxafk-scrcpy --network $NETWOK_NAME `
--action allow `
--source-ranges 0.0.0.0/0 `
--rules "tcp:5555" `
--enable-logging

gcloud compute firewall-rules create allow-webxafk-ssh --network $NETWOK_NAME `
--action allow `
--source-ranges 0.0.0.0/0 `
--rules "tcp:22" `
--enable-logging
#>

gcloud compute instances create $VM_NAME --image-project ubuntu-os-cloud --image-family ubuntu-2310-amd64 --zone=asia-east1-a --network $NETWOK_NAME --metadata=ssh-keys=$SSH_PUB_KEY
<#
gcloud compute ssh $VM_NAME --command 'sudo apt update && sudo apt install -y curl'
gcloud compute ssh $VM_NAME --command 'curl -fsSL https://get.docker.com -o install-docker.sh'
gcloud compute ssh $VM_NAME --command 'sudo sh install-docker.sh'
gcloud compute ssh $VM_NAME --command 'sudo apt install -y linux-modules-extra-`uname -r` && sudo modprobe binder_linux devices="binder,hwbinder,vndbinder"'
#>