from collections import namedtuple


Degree = type("Degree", (), dict(__init__=lambda *_: None))
Career = type("Career", (), dict(__init__=lambda *_: None))
Session = namedtuple("Session", "name")
