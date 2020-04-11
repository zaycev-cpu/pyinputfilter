RESULT_FILTER_OK = 0
RESULT_FILTER_INVALID_LEN = 1
RESULT_FILTER_INVALID_TYPE = 2
RESULT_FILTER_NOT_IN_APHABET = 3
RESULT_FILTER_NOT_IN_RANGE = 4
RESULT_FILTER_CANT_CONVERT = 5


class ResultFilter(object):
	def __init__(self, error = RESULT_FILTER_OK, text = None):
		self.error = error
		self.text = text

	def __str__(self):
		tmpl = lambda s: f"<{self.__class__.__name__} ({s})>"

		if self.success:
			return tmpl('ok')

		return tmpl(self.error)

	@property
	def success(self):
		return True if self.error == RESULT_FILTER_OK else False