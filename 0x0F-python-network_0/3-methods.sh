#!/bin/bash
#comment
curl -sl -iX OPTIONS "$1" | grep -i Allow | cut --complement -d ' ' -f 1
