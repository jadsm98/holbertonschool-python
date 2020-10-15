#!/bin/bash
#comment
curl -slX OPTIONS "$1" | grep -i Allow | cut --complement -d '' -f 1
