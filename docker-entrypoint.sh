#!/bin/bash

# A script failure should exist the shell
# https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
# https://explainshell.com/explain?cmd=set+-euxo%20pipefail#
set -exo pipefail

_run_migrations () {
    echo 'Running migrations..'
    flask db upgrade
    echo 'Migrations ran successfully!'
}

_start_application () {
  echo "Staring nginx"
  service nginx start

  echo "Staring uWSGI"
  uwsgi uwsgi.ini
}

_run_migrations
_start_application