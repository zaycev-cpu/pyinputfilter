import pyinputfilter as pif
from pyinputfilter.resultfilter import ResultFilter

import pyinputfilter.resultfilter as rf

class InputFilter(object):
	def __init__(self, *a, **kw):
		self.init()

		for key in kw:
			setattr(self, key, kw[key])

	def verify(self, value) -> rf.ResultFilter:
		return rf.ResultFilter(rf.RESULT_FILTER_OK)

	def execute(self, value):
		val = self.convert(value)
		if type(val) == rf.ResultFilter:
			return val
		return self.verify(val)

	def convert(self, value):
		return None

	def init(self):
		pass