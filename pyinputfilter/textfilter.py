import pyinputfilter as pif
import string

DEFAULT_ALPHABET = string.ascii_letters + ' !_@.,'

class TextFilter(pif.InputFilter):

	def init(self):
		self.minlen = 0
		self.maxlen = 0
		self.alphabet = None

	def verify(self, value) -> pif.ResultFilter:
		if type(value) != str:
			return pif.ResultFilter(pif.RESULT_FILTER_INVALID_TYPE)

		if len(value) > self.maxlen or len(value) < self.minlen:
			return pif.ResultFilter(pif.RESULT_FILTER_INVALID_LEN)

		if self.alphabet is not None:
			for v in value:
				if v not in self.alphabet:
					return pif.ResultFilter(pif.RESULT_FILTER_NOT_IN_APHABET)

		return pif.ResultFilter(pif.RESULT_FILTER_OK)