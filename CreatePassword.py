#import libraries
import string
import random

#main function
def Generate(PassLength):
	#string.ascii_letters Return all ASCII letters (both lower and upper case), abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
	#string.digits returns '0123456789'
	#string.punctuation returns !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
	password=string.ascii_letters+string.digits+string.punctuation
	#empty list
	passwordlist = []
	for x in range(PassLength):
		#choice()	Returns a random element from the given sequence
		randomize=random.choice(password)
		passwordlist.append(randomize)

	outreturn = "".join(passwordlist)
	return outreturn

	
	
