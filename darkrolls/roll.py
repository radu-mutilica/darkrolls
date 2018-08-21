import functools
from . import config

class Invalid(Exception):
    pass


class __Roll(object):
    def __init__(self, undead, timestamp):
        self.undead = undead
        self.timestamp = timestamp

    def resolve(self):
        pass

class Octs(__Roll):
    def __init__(self, undead, timestamp):
        super(Octs, self).__init__(undead, timestamp)


class Septs(__Roll):
    def __init__(self, undead, timestamp):
        super(Septs, self).__init__(undead, timestamp)


class Sexts(__Roll):
    def __init__(self, undead, timestamp):
        super(Sexts, self).__init__(undead, timestamp)


class Quints(__Roll):
    def __init__(self, undead, timestamp):
        super(Quints, self).__init__(undead, timestamp)


class Quads(__Roll):
    def __init__(self, undead, timestamp):
        super(Quads, self).__init__(undead, timestamp)


class Trips(__Roll):
    def __init__(self, undead, timestamp):
        super(Trips, self).__init__(undead, timestamp)


class Dubs(__Roll):
    def __init__(self, undead, timestamp):
        super(Dubs, self).__init__(undead, timestamp)


def verify(timestamp):
    for roll_type in [Octs, Septs, Sexts, Quints, Quads, Trips, Dubs]:
        if len(set(timestamp[config.options['roll'][roll_type.__name__.lower()]['length']:])) == 1:
            return functools.partial(roll_type, timestamp=timestamp)
    raise Invalid("that's not a roll, sorry")
