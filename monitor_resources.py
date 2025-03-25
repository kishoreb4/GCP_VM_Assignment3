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

#!/bin/bash

# while true; do
#     CPU_USAGE=$(mpstat 1 1 | awk '/Average/ {print 100 - $NF}')
#     echo "CPU Usage: $CPU_USAGE%"

#     if (( $(echo "$CPU_USAGE > 75" | bc -l) )); then
#         echo "CPU usage exceeded 75%. Creating new VM in GCP..."
        
#         ZONES=("us-central1-b" "us-west1-a" "us-east1-b")
        
#         for ZONE in "${ZONES[@]}"; do
#             if gcloud compute instances create "scaled-vm-$(date +%s)" \
#                 --zone="$ZONE" \
#                 --machine-type=n1-standard-1 \
#                 --image-family=ubuntu-2004-lts \
#                 --image-project=ubuntu-os-cloud; then
#                 echo "VM created successfully in $ZONE"
#                 break
#             else
#                 echo "Failed to create VM in $ZONE, trying next zone..."
#             fi
#         done
#     fi

#     sleep 30  # Wait 30 seconds before checking again
# done
