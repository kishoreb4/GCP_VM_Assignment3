#!/bin/bash

CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
echo "CPU Usage: $CPU_USAGE%"

if (( $(echo "$CPU_USAGE > 75" | bc -l) )); then
    echo "CPU usage exceeded 75%. Creating new VM in GCP..."
    gcloud compute instances create "scaled-vm-$(date +%s)" \
        --zone=us-central1-b \
        --machine-type=e2-micro \
        --image-family=ubuntu-2004-lts \
        --image-project=ubuntu-os-cloud
fi
