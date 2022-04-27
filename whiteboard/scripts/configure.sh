#!/bin/sh
set -e
sed -i -e 's|PORT|'$PORT'|g' /etc/nginx/sites-available/app.conf
supervisorctl -c /etc/supervisor/conf.d/supervisord.conf update
supervisorctl -c /etc/supervisor/conf.d/supervisord.conf start uwsgi
