#!/bin/bash

SERVER_HOST="139.129.97.73" # gululu.me
SERVER_USER="bowhead_web"
SERVER_PASSWORD="bowhead_web"
SERVER_DB="bowhead_web"
SQL_DUMP = "dbdump.dql"
LOCAL_HOST="localhost"
LOCAL_USER="bowhead_web"
LOCAL_PASSWORD="bowhead_web"
LOCAL_DB="bowhead_web"

echo "Wait......"
cat $SQL_DUMP  | mysql --host=${LOCAL_HOST} -u${LOCAL_USER} -p${LOCAL_PASSWORD} -C ${LOCAL_DB}
echo "Update db Done!"
