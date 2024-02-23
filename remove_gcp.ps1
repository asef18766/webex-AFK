$VM_NAME="webxafk"
$NETWOK_NAME="webxafk-net"
gcloud compute instances delete $VM_NAME --quiet --zone=asia-east1-a
gcloud compute firewall-rules delete allow-webxafk-ssh --quiet
gcloud compute networks delete $NETWOK_NAME --quiet
