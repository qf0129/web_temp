#!/bin/bash

# Backup database with crontab every hour , config as follows : 
#  0 * * * * /opt/bowhead/WsBowhead/scripts/db_backup.sh

BACKUP_DIR='/opt/bowhead/db_backup/'
TODAY=`date +%Y%m%d`
TIME=`date +%Y%m%d%H%M%S`
TODAY_DIR=${BACKUP_DIR}${TODAY}/

if [ ! -d ${BACKUP_DIR} ]; then  
    sudo mkdir ${BACKUP_DIR}
fi  

if [ ! -d ${TODAY_DIR} ]; then  
    sudo mkdir ${TODAY_DIR}
fi  

mysqldump -u bowhead_web -pbowhead_web bowhead_web | gzip > ${TODAY_DIR}bowhead_web.${TIME}.sql.gz
