#!/bin/bash
#comment
curl "$1" -i -sX OPTIONS | grep -i Allow | awk '{$1="";print}' | sed -e 's/^[[:space:]]*//'
