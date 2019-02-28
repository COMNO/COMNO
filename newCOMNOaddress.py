!/usr/bin/python
import importlib
moduleName = input('pubkey.py')
importlib.import_module(moduleName)
#THEN LASTLY WE MUST USED GENERATED PUBLIC KEY TO CREATE A PUBLIC ADDRESS WHERE TOKENS WILL BE SENT TO AND STORED
####TO GET PUBLIC ADDRESH IS A BIT TRICKISH BUT VERY SIMPLE#######
##MUST FOLLOW THIS 7 STEPS##

#1. SHA256 must be made on the publickey 
public_key_bytes = codecs.decode(key_hex, ‘hex’)
sha256_bpk = hashlib.sha256(public_key_bytes)
sha256_bpk_digest = sha256_bpk.digest()


#2. ripemd160 must be made on from the result gotten from 1. 
ripemd160_bpk = hashlib.new(‘ripemd160’)
ripemd160_bpk.update(sha256_bpk_digest)
ripemd160_bpk_digest = ripemd160_bpk.digest()
ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, ‘hex’) ##THIS WILL BE THE HASH160 ADDRESS## [a38880d9b66a5b134e9d2af5bb40c6cb182c419b]
#THE HASH160 IS USED TO GENERATE A CHECKSUM FOR THE ADDRESS TO MAKE SURE ADDRESSES ARE VALID THEN THE CHECKSUM IS ADDED AT THE SUFFIX OF THE ADDRESS AND BASE58 DECODED TO CREATE THE REAL ADDRESS .............. just like bitcoin :D
##SO LETS GO AHEAD AND CALCULATE THE CHECKSUM

#3. we must add a network BYTE OF 0X08 (08) as prefix to the result gotten from 2
network_comno_ripemd160_bpk_hex = "08"+(ripemd160_bpk_hex) #[08a38880d9b66a5b134e9d2af5bb40c6cb182c419b]

#4. SHA256 must be made from result of 3
sha256_nbpk = hashlib.sha256(network_comno_ripemd160_bpk_hex)
sha256_nbpk_digest = sha256_nbpk.digest()

#5. SHA256 must be made from result of 4
sha256_2_nbpk = hashlib.sha256(sha256_nbpk_digest)
sha256_2_nbpk_digest = sha256_2_nbpk.digest()
sha256_2_hex = codecs.encode(sha256_2_nbpk_digest, ‘hex’)

#6. First four bytes (8 CHARACTERS) of result of 5 will be taken and added as suffix to the result gotten from 3 a.k.a (will be used to validate checksum)
checksum = sha256_2_hex[:8] #ebd428e9
#Finally, to make an address, we just concatenate the mainnet key and the checksum. That makes it 
addr = network_comno_ripemd160_bpk_hex+checksum #[08a77b5e6dd1a5362d98f3fbe8651326fa453fb967ebd428e9]

#7. FINALLY THE RESULT OF 6 IS BASE58 ENCODED TO PRODUCE A UNIQUE COMNO ADDRESS
def base58(addr):
    alphabet = ‘123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz’
    b58_string = ‘’
    # Get the number of leading zeros
    leading_zeros = len(address_hex) — len(address_hex.lstrip(‘0’))
    # Convert hex to decimal
    address_int = int(address_hex, 16)
    # Append digits to the start of string
    while address_int > 0:
        digit = address_int % 58
        digit_char = alphabet[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Add ‘1’ for each 2 leading zeros
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = ‘1’ + b58_string
    return b58_string ##<---- OUR PUBLIC COMNO ADDRESS [4UcWYZ99RuXny5XyDJiJgDnvaYNHKeeFqz]
	
	#Conclusion
	#The wallet key generation process can be split into four steps:
	
    #-->generating a secure Private key with sha256
    #-->creating a public key with ECDSA
    #-->encrypting the key with SHA-256 and RIPEMD-160
    #-->calculating the checksum with double SHA-256
    #-->encoding the key with Base58



