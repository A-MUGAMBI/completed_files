#!/usr/bin/python3
"""a program that prints all letters with no new line and also exclude letters e and q"""

for letter in range(97, 123):
	if chr(letter) != 'q' and chr(letter) != 'e':
		print("{}".format(chr(letter)), end="")
