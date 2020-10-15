#!/bin/bash
#comment
curl -sl -X OPTIONS "$1" | grep -i Allow | cut --complement -d ' ' -f 1
