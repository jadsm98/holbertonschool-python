#!/bin/bash
# displays body of response
[ $(curl -LI '$1' -o /dev/null -w '%{http_code}\n' -s) == "200" ] && curl -sX GET '$1'
