#!/usr/bin/python3
"""
Contains one function find_peak()
"""


def find_peak(list_of_integers):
	"""Finds a peak in a list of unsorted integers"""
	li = list_of_integers
	l = len(li)
	if l == 0:
		return None
	if (l == 1) :
		return li[0]
	if (li[0] >= li[1]):
		return li[0]
	if (li[l - 1] >= li[l - 2]):
		return l - 1
	for i in range(1, l - 1) :
		if (li[i] >= li[i - 1] and li[i] >= li[i + 1]) :
			return li[i]
