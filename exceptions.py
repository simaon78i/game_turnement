class AddTeamError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AddMatchError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
