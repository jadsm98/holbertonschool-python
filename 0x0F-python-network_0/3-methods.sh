#!/bin/bash
#comment
curl -i -sX OPTIONS "$1" | grep -i Allow | awk '{$1=$2=""; print $0}'
