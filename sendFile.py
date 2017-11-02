#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this is a send file progrem based on the http
this is sender, and the sender should provide the http server,
and you should sure you python is python3
---------
Usage:
python sendFile.py RecverIP fileName
--------
RecverIp：the Recever IP address
--------
fileName: the Name, which should include the folder for example:
absolute path or relative path, of the file sent by Sender
"""
import socket, os, sys, time


if(len(sys.argv) != 3):
    print(
        """
this is a send file progrem based on the http
this is sender, and the sender should provide the http server
---------
Usage:
python sendFile.py RecverIP fileName
--------
RecverIp：the Recever IP address
--------
fileName: the Name, which should include the folder for example:
absolute path or relative path, of the file sent by Sender
"""

    )
    sys.exit(1)

RecverIP = sys.argv[1]
fileName = sys.argv[2]
socket.setdefaulttimeout(2)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
i = 1
sendFlags = True
while True:
    try:
        if sendFlags:
            s.sendto(os.path.abspath(fileName).encode('utf-8'),(RecverIP, 443))
            print(fileName)
        nameResponse = (s.recv(1024).decode('utf-8'))
        if nameResponse == '1':
            print('the file image is sent to %s successfully'% RecverIP)
            break
        if nameResponse =='0':
            print('fuckkk')
            sendFlags = False
    except Exception as e:
        if sendFlags:
            i = i + 1
        if i > 10:
            print('tried 10 times is wrong')
            break  
s.close()
