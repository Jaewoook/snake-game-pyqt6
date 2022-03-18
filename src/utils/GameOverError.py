class GameOverError(Exception):

    reason = 'Game Over error occurred! reason: '

    def __init__(self, reason: str = ''):
        self.reason += reason
        super().__init__(self.reason)
