from Pong.ball import Ball
from Pong.paddle import Paddle

class Game:
	def __init__(self, PY):
		"setup game vars"
		self.key_file = "Pong/keys.json"
		self.game_name = "Pong"
		self.game_size = (720, 480)
		self.states = ["start", "restart", "levelup"]
		self.current_state = self.states[0]

		"initial game objects"
		#self.gui = Gui()
		self.player_paddle = Paddle(self.game_size, PY, "player")
		self.ai_paddle = Paddle(self.game_size, PY, "ai")
		self.ball = Ball(self.game_size, 10, PY)

		self.init_objs = [self.ball, self.ai_paddle, self.player_paddle]

	def update(self):
		"this should be in a game class which will handle game specific logic"
		"pass in AE so we can have a function that can add or remove objects from game"
		if self.current_state == self.states[0]:
			if self.ball.hit_edge_left:
				print("you Lose!")
				self.current_state = "restart"
			elif self.ball.hit_edge_right:
				print("you Win!")
				self.current_state = "levelup"
		elif self.current_state == self.states[1]:
			print("new game")
			self.ball.set_init_location()
			self.player_paddle.set_init_location()
			self.ai_paddle.set_init_location()
			#self.gui.set_init_state()
			self.current_state = self.states[0]
		elif self.current_state == self.states[2]:
			print("next level")
			self.ball.level_up()
			self.player_paddle.level_up()
			self.ai_paddle.level_up()
			#self.gui.level_up()
			self.current_state = self.states[0]
			