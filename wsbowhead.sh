#!/bin/bash
port=7777
pid_dir="tmp/"
pid_file="${pid_dir}run.pid"
function source_venv {
        if [ -d "venv/" ]; then  
            source venv/bin/activate
        fi  
        if [ -d "env/" ]; then  
            source env/bin/activate
        fi  
}

function start_server {
        source_venv
        if [ ! -d ${pid_dir} ]; then
            mkdir ${pid_dir}
        fi
        if [ -f ${pid_file} ]; then
            echo "Server is running , please stop or restart"
            exit
        fi
        export NEW_RELIC_CONFIG_FILE=newrelic.ini
        nohup newrelic-admin run-program gunicorn  -w 8 -k gevent -b 127.0.0.1:${port} web.wsgi:application > /dev/null 2>&1 & echo $! > ${pid_file}
        pid=`cat ${pid_file}`
        echo "Start Success! pid: ${pid}"
}

function stop_server {
        if [ ! -f ${pid_file} ]; then
            echo "Server is not running"
        else
            kill -9 `cat ${pid_file}`
            rm ${pid_file}
            echo "Server is stop"
        fi
}

function show_help {
        echo "help :"
        echo ""
        echo "      start"
        echo "      stop"
        echo "      restart"
        echo "      start -u      - update static file before start"
        echo "      restart -u    - update static file before restart"
        echo ""
}

if [ $# = 1 ]; then
    if [ $1 = 'start' ]; then
        start_server
    elif [ $1 = 'stop' ]; then
        stop_server
    elif [ $1 = 'restart' ]; then
        stop_server
        start_server
    else
        show_help
    fi
elif [ $# = 2 ]; then
    if [ $1 = 'start' ]; then
        if [ $2 = '-u' ]; then
            source_venv
            python manage.py collectstatic
            start_server
        else
            show_help
        fi
    elif [ $1 = 'restart' ]; then
        if [ $2 = '-u' ]; then
            source_venv
            python manage.py collectstatic
            stop_server
            start_server
        else
            show_help
        fi
    else
        show_help
    fi
else
    show_help
fi