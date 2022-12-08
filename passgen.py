#!/usr/bin/env python

import random
import sys

# ASCII characters, including space
ascii_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=-]}[|{;:"/?.>,\\<\''

# non ASCII characters to add to entropy. Intelligently written password code should accept all UTF8 characters.
# however, sadly many don't
# generate all utf8 printable characters for use in password, 143680 possibilities
# not all of them will print on your computer if you don't have all fonts installed
utf8 = ''.join(tuple(chr(i) for i in range(32, 0x110000) if ( chr(i).isprintable() and not chr(i).isspace() ) ))

use_non_ascii = False    # if true use the extra characters
spaces_ok = False        # if true, password can contain spaces
plength = 16             # default password length


def gen_pword(plength):

	if use_non_ascii:
		charset = utf8
	else:
		charset = ascii_chars
	
	if spaces_ok:
		charset = charset + ' '

	return ''.join(random.choices(charset, k = plength))



if __name__ == "__main__":
	if len(sys.argv) > 1:
		try:
			plength = int(sys.argv[1])
			if len(sys.argv) == 4:
				use_non_ascii = sys.argv[2].lower()[0] in ['t', '1', 'y' ]
				spaces_ok  =    sys.argv[3].lower()[0] in ['t', '1', 'y' ]
			
		except:
			print('usage passgen <length> <use non-ascii> <allow spaces>')
			exit(0)
	

	pword = gen_pword(plength)
	print(pword)
