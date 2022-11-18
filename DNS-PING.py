#@author: Giten Mitra
#Date: 21 May 2022
#Description: This script will alert to user if DNS is down and website is not working.

import json
import urllib.request
import logging
import boto3
from urllib.error import URLError, HTTPError
client = boto3.client('sns')
import subprocess


logger = logging.getLogger()
def test():
    try:
     statuscode = urllib.request.urlopen("http://www.amazon.in").getcode()
    except URLError as error:
        logger.error("Server connection failed: %s", error.reason)
        prog = subprocess.run(["ping", "11.11.11.11"], capture_output=True)
        print("Output is \n",prog.stdout.decode())
        response = client.publish(
            TopicArn='arn:aws:sns:us-east-1:1111111111:SecurityGroup-Test1234',
            Message='prog',
            Subject='Server connection failed'
            )
    else:
        print("Everythng working fine")
    return

test()
