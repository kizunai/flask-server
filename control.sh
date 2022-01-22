#!/bin/bash
set -x

start() {
    gunicorn -c start_app.py wsgi:app
    echo "wsgi process num:"
    ps -ef | grep -c wsgi
}

stop() {
    ps -fe | grep python3 | grep wsgi:app | grep -v grep | gawk '{print $2}' | xargs kill -9
    echo "app stopped"
}

restart() {
    stop
    sleep 0.5
    start
}

case "$1" in
start)
    start
    ;;
stop)
    stop
    ;;
restart)
    restart
    ;;
*)
    echo "Usage: $0 {start|stop|restart}"
    ;;
esac

