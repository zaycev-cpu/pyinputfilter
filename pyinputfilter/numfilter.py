import pyinputfilter as pif

class NumFilter(pif.InputFilter):

	def init(self):
		self.min = 0
		self.max = 256

	def verify(self, value) -> pif.ResultFilter:
		if value < self.min or value > self.max:
			return pif.ResultFilter(pif.RESULT_FILTER_NOT_IN_RANGE)

		return pif.ResultFilter(pif.RESULT_FILTER_OK)

	def convert(self, value):
		try:
			return int(value)
		except ValueError:
			return pif.ResultFilter(pif.RESULT_FILTER_CANT_CONVERT)
