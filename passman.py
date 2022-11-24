#! /bin/env python

from sjcl import *
cyphertext = SJCL().encrypt(b"udyeaxor", "admin")
print (cyphertext)
