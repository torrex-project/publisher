#!/bin/bash

docker run -d --net host -v "`pwd`:/code" -w /code --env-file .env -it publisher bash run.sh
