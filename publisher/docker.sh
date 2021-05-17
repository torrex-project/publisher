#!/bin/bash

docker run -d --restart always --net host -v "`pwd`:/code" -w /code --env-file .env -it publisher bash run.sh
