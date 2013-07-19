import sys
import os
import twitter

api = twitter.Api(
	consumer_key='CONSUMER KEY',
	consumer_secret = 'CONSUMER SECRET',
	access_token_key='ACCESS TOKEN KEY',
	access_token_secret='ACCESS TOKEN SECRET'
	)
	
print "She's working :)"

timeline = [] 
letters = []
command_temp = []
command = ''
i = 7 #to offset the flag at the beginning of the tweet
timeline = api.GetUserTimeline('YOURUSERNAME')
for s in timeline:
	if '~start' in s.text:
		letters = [g for g in s.text]
		length = len(letters)
		command_temp = [letters[i] for i in range(7, length)]
		command = ''.join(command_temp)
		print 'Command about to run: ', command
		break
	else:
		pass
try:
	raw_input('>>(Hit Enter to run, CTRL-C to quit): ')
	print 'you continued'
except KeyboardInterrupt:
	print '\nyou exited'
	sys.exit()
print command
os.system (command)

