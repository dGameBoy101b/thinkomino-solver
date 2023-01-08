class DictionaryXMLBuilder:
	def __init__(self):
		self.result = dict()
		self.__key_stack = list()

	def __get_head(self, keys: list = None) -> dict:
		if keys is None:
			keys = self.__key_stack
		result = self.result
		for key in keys:
			result = result[key]
		return result

	def start(self, tag: str, attrs: dict):
		self.__get_head()[tag] = dict()
		self.__key_stack += [tag]

	def data(self, data: str):
		self.__get_head(self.__key_stack[:-1])[self.__key_stack[-1]] = data

	def end(self, tag: str):
		del self.__key_stack[-1]

	def close(self):
		result = self.result
		self.result = dict()
		self.__key_stack = list()
		return result
