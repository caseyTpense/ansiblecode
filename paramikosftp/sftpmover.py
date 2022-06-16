#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os

def movethemfiles(sftp):
    wherefrom=input('where would you like to move files from?')

    whereto= input('where would you like to move the files to?')
    for x in os.listdir(wherefrom): # iterate on directory contents
        if not os.path.exists(whereto +x):
            sftp.put(wherefrom+x, whereto+x)
       # if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
       #     sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location 
        

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
movethemfiles(sftp)
## close the connections
sftp.close() # close the connection
t.close()

