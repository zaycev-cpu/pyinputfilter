import pyinputfilter as pif

class NumFilter(pif.InputFilter):

	def init(self):
		self.min = 0
		self.max = 256

	def verify(self, value) -> pif.ResultFilter:
		if value > self.min or value < self.max:
			return pif.ResultFilter(pif.RESULT_FILTER_INVALID_LEN)

		if self.alphabet is not None:
			for v in value:
				if v not in self.alphabet:
					return pif.ResultFilter(pif.RESULT_FILTER_NOT_IN_APHABET)

		return pif.ResultFilter(pif.RESULT_FILTER_OK)

	def convert(self, value) -> str:
		return int(value)