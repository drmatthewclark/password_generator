#!/usr/bin/env python

import random
import sys

# ASCII characters, including space
ascii_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=]}[{;:"/?.>,\\< \''

# non ASCII characters to add to entropy. Intelligently written password code should accept all UTF8 characters.
# however, sadly many don't
extra_chars = 'Ññ¡¿ÇçŒœßØøåÆæÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸåÅכּךכיטחזוהדגבּבאלמנסעפפּצקרששׁשׂתץףןם¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾'

use_non_ascii = False    # if true use the extra characters
spaces_ok = False        # if true, password can contain spaces
plength = 16             # default password length


def gen_pword(plength):
	if use_non_ascii:
		charset = ascii_chars + extra_chars
	else:
		charset = ascii_chars
	
	if not spaces_ok:
		charset = charset.replace(' ','')

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
	
	
	random.seed(gen_pword(256))	
	pword = gen_pword(plength)
	print(pword)
