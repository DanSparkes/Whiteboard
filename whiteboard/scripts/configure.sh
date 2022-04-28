#!/bin/sh
supervisorctl -c /etc/supervisor/conf.d/supervisord.conf update
supervisorctl -c /etc/supervisor/conf.d/supervisord.conf start uwsgi
