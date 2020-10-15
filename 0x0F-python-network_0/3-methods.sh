#!/bin/bash
#comment
curl "$1" -sX OPTIONS | grep -i Allow | awk '{$1="";print}' | sed -e 's/^[[:space:]]*//'
