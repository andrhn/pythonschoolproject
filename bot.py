import telegram

class Bot():
    def __init__(self, token):
        self.token = token
        self.bot = telegram.Bot(self.token)

