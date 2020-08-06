#!/bin/bash

curl --request OPTIONS \
  --url 'http://localhost:39993/admin?file=file' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --header 'file: asd' \
  --data admin=WhiteHacksAdmin
