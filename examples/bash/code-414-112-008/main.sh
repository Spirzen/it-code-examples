#!/bin/bash
# Мониторинг свободного места на дисках

THRESHOLD_WARNING=85
THRESHOLD_CRITICAL=95

df -H | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }' | while read output;
do
    usage=$(echo $output | awk '{ print $1}' | sed 's/%//g')
    partition=$(echo $output | awk '{ print $2 }')
    
    if [ $usage -ge $THRESHOLD_CRITICAL ]; then
        echo "CRITICAL: $partition заполнен на ${usage}%" | send_alert
    elif [ $usage -ge $THRESHOLD_WARNING ]; then
        echo "WARNING: $partition заполнен на ${usage}%" | send_alert
    fi
done
