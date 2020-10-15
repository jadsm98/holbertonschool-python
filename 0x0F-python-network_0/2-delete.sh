#!/bin/bash
#comment
curl -sX DELETE "$1" -sX GET "$1"
