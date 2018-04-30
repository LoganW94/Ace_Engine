
class Paddle:
	def __init__(self, game_size, PY, ptype):
		self.game_size = game_size
		self.PY = PY
		self.ptype = ptype

		self.height = 70
		self.width = 14
		self.moverate = 5

		self.set_init_location()
			

	def set_init_location(self):

		if self.ptype == "player":
			self.color = (0,255,0)
			self.centerx = self.width/2
			self.centery = self.game_size[1]/2
			self.rect = self.PY.Rect(0, self.centery - self.height/2, self.width, self.height)
		elif self.ptype == "ai":
			self.color = (255,0,0)
			self.centerx = self.game_size[0] - self.width/2
			self.centery = self.game_size[1]/2
			self.rect = self.PY.Rect(self.centerx - self.width/2, self.centery - self.height/2, self.width, self.height)

		self.shape = ["rect", self.color, self.rect]	


	def update(self, new_input, objs):
		
		if self.ptype == "player":
			if new_input == "UP2":
				self.centery -= self.moverate
			elif new_input == "DOWN2":
				self.centery += self.moverate
				
		elif self.ptype == "ai":		
			if new_input == "UP1":
				self.centery -= self.moverate
			elif new_input == "DOWN1":
				self.centery += self.moverate
				
		self.collision()

		if self.ptype == "player":
			self.rect = self.PY.Rect(0, self.centery - self.height/2, self.width, self.height)
		elif self.ptype == "ai":
			self.rect = self.PY.Rect(self.centerx - self.width/2, self.centery - self.height/2, self.width, self.height)			
		self.shape = ["rect", self.color, self.rect]

	def collision(self):
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= self.game_size[1]-1:
			self.rect.bottom = self.game_size[1] -1	

	def level_up(self):
		self.set_init_location()
		

