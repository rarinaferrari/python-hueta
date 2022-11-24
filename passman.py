#!/bin/env python


a,b = input(), input()
import base64
from sjcl import SJCL
cyphertext = SJCL().encrypt(a.encode('utf-8'), b.encode('utf-8'))
#s = str(cyphertext)
#s = s.encode("UTF-8")
cyphertext = base64.b64encode(str(cyphertext).encode('utf-8')).decode('utf-8')
print (cyphertext)
