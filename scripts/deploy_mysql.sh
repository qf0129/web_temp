#!/bin/bash

LOCAL_HOST="localhost"
LOCAL_PORT="3306"
LOCAL_USER="root"
LOCAL_PASSWORD=""

function deploy_mysql {
    echo "Wait......"
   mysql -h${LOCAL_HOST}  -P${LOCAL_PORT}  -u${LOCAL_USER} -p${LOCAL_PASSWORD} -e "CREATE database IF NOT EXISTS bowhead_web;"
   mysql -h${LOCAL_HOST}  -P${LOCAL_PORT}  -u${LOCAL_USER} -p${LOCAL_PASSWORD} -e "CREATE user bowhead_web@localhost identified by 'bowhead_web';"
   mysql -h${LOCAL_HOST}  -P${LOCAL_PORT}  -u${LOCAL_USER} -p${LOCAL_PASSWORD} -e "FLUSH PRIVILEGES;"
   mysql -h${LOCAL_HOST}  -P${LOCAL_PORT}  -u${LOCAL_USER} -p${LOCAL_PASSWORD} -e "GRANT ALL PRIVILEGES ON bowhead_web.* TO 'bowhead_web'@'localhost';"
}

function show_help {
        echo "help:"
        echo ""
        echo "     ./deploy_mysql.sh PASSWORD    　　# password of root in localhost mysql  "
        echo ""
}

if [ $# = 1 ]; then
    LOCAL_PASSWORD=$1
    deploy_mysql
else
    show_help
fi