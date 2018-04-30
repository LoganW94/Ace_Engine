
class Screen:

	@staticmethod
	def new(PY, game_size, color, caption='', imagepath=None):

		screen = PY.display.set_mode(game_size)
		PY.display.set_caption(caption)
		return screen