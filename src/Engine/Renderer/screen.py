
class Screen:

	@staticmethod
	def new(PY, width, height, color, caption='', imagepath=None):

		screen = PY.display.set_mode((width, height))
		PY.display.set_caption(caption)
		return screen