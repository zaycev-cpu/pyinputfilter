# pyinputfilter
A small library that serves to filter input data as strings.

```diff
- Now the library is not ready for use!
```

### Get started

```python
import pyinputfilter as pif

def test()
	# get text from user
	indata = input('text: ')

	# create filter for text
	flt = pif.TextFilter(minlen = 3, maxlen=20, alphabet = pif.DEFAULT_ALPHABET)

	# executing filter for user data
	result = flt.execute(indata)

	# write success
	if result.success:
		print('ok')
	else:
		print('not ok')

if __name__ == '__main__':
	while True:
		test()
```

```
```