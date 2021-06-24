#!/usr/local/bin/bash

set -e
set -x

# push remotes
git push origin master
git push github master

# pull latest changes
ssh root@95.217.223.96 'cd /opt/apps/gorate && git pull'

# migrate database
ssh root@95.217.223.96 'cd /opt/apps/gorate && source venv/bin/activate && python manage.py migrate'

# reload uwsgi
ssh root@95.217.223.96 'uwsgi --reload /tmp/uwsgi_gorate.pid'

# reload nginx
ssh root@95.217.223.96 'nginx -t && systemctl reload nginx'
