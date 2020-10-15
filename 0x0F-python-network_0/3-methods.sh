#!/bin/bash
#comment
curl -siX OPTIONS "$1" | grep -i allow | awk '{print $2}'
