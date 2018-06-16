
class States:
    def __init__(self):
        self.init_state = None
        self.current_state = None
        self.new_state = None
        self.previous_state = None

    def change_state(self, new_state):
        self.new_state = new_state
        self.previous_state = self.current_state
        self.current_state = self.new_state
