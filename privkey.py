!/usr/bin/python
##COMNO ADDRESS GENERATION
#HOW A COMNO ADDRESS IS GENERATED. AND PROCESS USED TO CREATE ADDRESS FROM PRIVATE KEY
#TO CREATE ANY CRYPTOCURRENCY ADDRESS, 1ST WE NEED TO GENERATE A SECURE PRIVATE KEY
#ALGORITHMS&ENCODERS USED MT_RAND(), SHA256, RIPEMD256, BITCOIN_BASE58
#THANKS TO THEIR CREATORS
#WE WILL CALL THIS COM_ALGORITHM, CREATED BY COMNO
#TO GENERATE THE SAFEST PRIVATE KEY, WE NEED SOME DATA###

#1. THE USERNAME, (can never be changed once account has been created, AND ofcourse can NEVER BE REUSED :-D}{which means there will NEVER BE A COLLISSION OF KEYS even if the next 4 billion DECADES.}
username = "user1";

#2. THE TIMESTAMP OF REGISTRATION (which can easily be bruteforced by a few smart dudes ;-)
import time #needed ?
timereg = "1551143768.00";

#3. THE USERS FIRST HASHED PASSWORD (maybe an md5 hash) (which can never be changed again even if the user forgets that password or changes the password to his/her comno account
password = hashlib.md5("7u6%12HA3user1")

#4. A RANDOM TIMESTAMP PICKED FROM UNIX EPOCH TILL CURRENT_TIME(); (might take a few years to bruteforce tho)
import random
randt = random.randint(0, time.time())

#5. A RANDOM 32CHARACTER AlPhA-NuMeRiC NONCE [0-9,a-z,A-Z] (might be impossible to crack so soon :-D, and even if same random number is generated twice and collides with a previously generated nonce, a single character change in other values (username , timestamp , randtimestamp,  password ) WILL GENERATE AN ENTIRELY NEW HASH SO A SELF COLLISSION IS NEARLY IMPOSSIBLE EVEN IN THE NEXT 100 BILLION DECADES.
from OpenSSL import rand
salt = rand.bytes(32)

###############################################################################################################
##NOW WE MUST COMBINE DATA TO FORM A STRING WITH NO SPACES AND SHA256(); TO CREATE A SINGLE AND SECURE PRIVATE KEY HEX##
private_key = hashlib.sha256(username+timereg+password+randt+salt) ##7f3e4951d88e7018189386cbcf5bf90d650144f43058766d13ce98b98fff0de9
##BEHOLD A SECURE PRIVATE KEY TO SOMEONES COMNO WALLET :)




