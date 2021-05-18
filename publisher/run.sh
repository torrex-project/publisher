#!/bin/bash

/code/torsniff -e 4000 -f 5000 | python /code/publish.py
