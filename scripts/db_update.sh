#!/bin/bash

SERVER_HOST="139.129.97.73" # gululu.me
SERVER_USER="bowhead_web"
SERVER_PASSWORD="bowhead_web"
SERVER_DB="bowhead_web"

LOCAL_HOST="localhost"
LOCAL_USER="bowhead_web"
LOCAL_PASSWORD="bowhead_web"
LOCAL_DB="bowhead_web"

echo "Wait......"
mysqldump --host=${SERVER_HOST} -u${SERVER_USER} -p${SERVER_PASSWORD} --opt ${SERVER_DB} | mysql --host=${LOCAL_HOST} -u${LOCAL_USER} -p${LOCAL_PASSWORD} -C ${LOCAL_DB}
echo "Update db Done!"