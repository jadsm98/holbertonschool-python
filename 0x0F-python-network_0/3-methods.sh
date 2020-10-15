#!/bin/bash
#comment
curl -sX OPTIONS "$1" -i | grep -i Allow | awk '{print $2}'
