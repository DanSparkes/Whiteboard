#!/bin/sh
set -e

echo PORT $PORT
sed -i -e 's|PORT|'$PORT'|g' /etc/nginx/sites-available/app.conf
