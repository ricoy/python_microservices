#!/bin/sh
uwsgi --ini hello_world_service.ini --socket 0.0.0.0:3001 --protocol=http -w hello_world_service:app