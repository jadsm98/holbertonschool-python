#!/bin/bash
#comment
curl "$1" -siX OPTIONS | grep -i Allow:  | awk '{$1=""; print $0}'
