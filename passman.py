#! /bin/env python

from sjcl import SJCL
cyphertext = SJCL().encrypt(b"udyeaxor", "admin")
print (cyphertext)
