class Robot:
    count = 0

    def __init__(self, name=None):
        self.name = name
        type(self).count += 1
