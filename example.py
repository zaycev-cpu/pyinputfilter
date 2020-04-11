import pyinputfilter as pif


flt = pif.TextFilter(minlen = 3, maxlen=20, alphabet = pif.DEFAULT_ALPHABET)
print(flt.execute('Hello, World!'))