#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this is a Receive file progrem based on the http
this is Receiver, and the sender should provide the http server,
and you should sure you python is python3
Usage:
--------
python RecvFile.py [fileName]
the fileName is the storged Name , which should include the file fileder for example:
absolute path or relative path of the recevied file 
"""
import socket, os, sys, time

try:
    from urllib import request
except Exception as e:
    print(
        """
        You import the urllib is wrong, 
        You should try the:
        pip install urllib3
        of course, you should sure the pip module be installed
        """
        )
    sys.exit(1)

def showUsage():
    print(
        """
this is a Receive file progrem based on the http
this is Receiver, and the sender should provide the http server,
and you should sure you python is python3
Usage:
--------
python RecvFile.py fileName
the fileName is the optionally storged Name , which should include the file fileder for example:
absolute path or relative path of the recevied file 
"""
    )
    sys.exit(1)





def getTheUrlFile(url, filename):
    """
    form the rul download the file
    """
    urlRequest  = request.Request(url)
    i = 1
    while True:
        try:
            urlResponse = request.urlopen(urlRequest)
            break
        except Exception as e:
            i = i + 1
            print('the Connect is falied, re-connect.......')
            if i > 4:
                print('the file download is failed, pleased sure the file is existed on the server')
                return ' '
            # continue
    getFile = urlResponse.read()
    with open(filename, 'wb') as fp:
        fp.write(getFile)
        print('the file %s is downloaded', filename)
    return filename

def recvFile(FileName):
    """
    recv the fileName and download the file
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((' ', 443))
    socket.setdefaulttimeout(2)
    i = 1
    while True:
        try:
            print('......................Rcv.........')
            rcvData, addr = s.recvfrom(1024)
            print('Received from %s:%s.' % addr)
            rcvName = rcvData.decode('utf-8')
            print(rcvName)
            s.sendto('0'.encode('utf-8'),addr)
            rcvName = rcvName.split('\\')
            # print(rcvName)
            rcvName[0] = rcvName[0][0]+'%3A'
            # rcvName[-1] = rcvImageName[-1] + '.ROI.bmp' 
            FileNameRcv = rcvName[-1]
            if not FileName:
                FileName = FileNameRcv
            urlName = 'http://' + addr[0] + '/' +'/'.join(rcvName)
            print(urlName)
            timeI = time.clock()
            status = getTheUrlFile(urlName,FileName)
            if FileName == status:
                timeIend = time.clock()
                print('the received time taken get the file is %fs ' % (timeIend - timeI))
                s.sendto('1'.encode('utf-8'),addr)
                break
            if not status:
                FileName = ''
                break

        except Exception as e:
            i = i + 1
            if i > 100:
                FileName = ''
                break
            # print(e)
    s.close()
    return FileName

# def runRecvFile():
print('fuck')
if len(sys.argv) > 2:
    showUsage()
fileName = ''
if len(sys.argv) == 2:
    fileName = sys.argv[1]
rcvName = recvFile(fileName)
if rcvName:
    print('the %s is successfully Received' % rcvName)
else:
    print('the %s is failedly Received' % rcvName)
    

# if __name__ == 'main':
#     runRecvFile()

