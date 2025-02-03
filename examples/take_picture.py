import sys

sys.path.append('/home/olivier/git/pyGphoto')

import pyGphoto as pgp

print( pgp.get_picture( filename = 'toto.jpg' ).stdout.decode() )
