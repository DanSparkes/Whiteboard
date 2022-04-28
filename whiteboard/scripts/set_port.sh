#!/bin/sh
set -e

echo PORT $PORT
sleep 5
sed -i -e 's|PORT|'$PORT'|g' /etc/nginx/sites-available/app.conf
