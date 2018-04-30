
class Ball:
	def __init__(self, game_size, radius, PY):

		self.PY = PY
		self.game_size = game_size

		
		self.radius = radius
		self.color = (0,0,255)

		self.set_init_location()

	def set_init_location(self):

		self.centerx = self.game_size[0]/2
		self.centery = self.game_size[1]/2
		"hit box"
		self.hit_edge_left = False
		self.hit_edge_right = False
		self.rect = self.PY.Rect(
			self.centerx-self.radius,
		 	self.centery-self.radius,
		 	self.radius*2, self.radius*2)

		"start direction. replace with random eventually"
		dx = 1
		dy = 1
		self.sp = 3
		self.vector = [dx,dy,self.sp]

		self.shape = ("circ", self.color, self.rect.center, self.radius)	

	def update(self, new_input, objs):

		self.centerx += self.vector[0]*self.vector[2]
		self.centery += self.vector[1]*self.vector[2]

		self.rect.center = (self.centerx, self.centery)

		"replace with collide_detect function passed through the update call by the engine update class"
		self.collision(objs)

		self.shape = ("circ", self.color, self.rect.center, self.radius)
		

	def collision(self, objs):

		
		if self.rect.top <= 0:
			self.vector[1] = 1
		elif self.rect.bottom >= self.game_size[1]-1:
			self.vector[1] = -1	

		if self.rect.right >= self.game_size[0]-1:
			self.hit_edge_right = True
		elif self.rect.left <= 0:
			self.hit_edge_left = True

		if self.rect.colliderect(objs[2]):
			self.vector[0] = 1
		elif self.rect.colliderect(objs[1]):
			self.vector[0] = -1			

	def level_up(self):
		sp = self.vector[2]
		self.set_init_location()
		self.vector[2] = sp + 2
