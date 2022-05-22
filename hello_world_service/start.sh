#!/bin/sh
export ENVIRONMENT=prod
uwsgi --ini hello_world_service.ini