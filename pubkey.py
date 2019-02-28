
!/usr/bin/python
import importlib
moduleName = input('privkey.py')
importlib.import_module(moduleName)

#NOW TO GET PUBLIC KEY, The first thing we need to do is to apply the ECDSA or Elliptic Curve Digital Signature Algorithm to our private key. An elliptic curve is a curve defined by the equation y² = x³ + ax + b with a chosen a and b. There is a whole family of such curves that are widely known and used. Bitcoin uses the secp256k1 curve. Comno uses the same curve to generate its private keys

#By applying the ECDSA to the private key, we get a 64-byte integer. This consists of two 32-byte integers that represent the X and Y of the point on the elliptic curve, concatenated together.

private_key_bytes = codecs.decode(private_key, ‘hex’)
# Get ECDSA public key
key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
key_bytes = key.to_string()
##BEHOLD A SECURE CURVE PUB KEY TO SOMEONES COMNO WALLET :)
key_hex = codecs.encode(key_bytes, ‘hex’) #05D1A31BEEAAD06EF7AEEBD9569F4CC06B35C43B4EA2F2AD06B0EAF2014F9B334158E74EF89C59E03E510A14A42A021D0440F404B661A63948CB606027013255




