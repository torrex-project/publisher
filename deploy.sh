#!/bin/bash

rsync --exclude "*~" -e "ssh" -rtuv ./* root@torrex04:/root/publisher
