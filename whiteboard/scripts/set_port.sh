#!/bin/sh
set -e
sed -i -e 's|PORT|'$PORT'|g' /etc/nginx/sites-available/app.conf
