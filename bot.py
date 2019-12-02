#!/usr/bin/env python
import sys
import os
import schedule
import time
from twython import Twython

def tweetTemp():
	#Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
	CONSUMER_KEY = 'SGEDNheidSGZOtRkPGg26aUAw'
	CONSUMER_SECRET = 'waIJnOeWJ8nPGjpT4DpOE2zhKWgdVeaomIohEalL3Jw6UGciUD'
	ACCESS_KEY = '1201363693583392768-nCfCeIFEgWBrDFStMYZo6Pt4ANWAqa'
	ACCESS_SECRET = 'J2fzNd3vIyTWEw3p7q3vKZ9H1iN7V0vKP6nC9R6jZmROQ'

	#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
	api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

	cmd = '/opt/vc/bin/vcgencmd measure_temp'
	line = os.popen(cmd).readline().strip()
	tempC = line.split('=')[1].split("'")[0]
	tempF = (float(tempC) * (9 / 5)) + 32

	tempTweet = "Current CPU temperature: {} deg F".format(tempF)

	#Using our newly created object, utilize the update_status to send in the text passed in through CMD
	api.update_status(status=tempTweet)

def job():
    tweetTemp()

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)