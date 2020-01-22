from flowers import Flower
from flowers.grown_shipped import NonOrganic

class Lilly(Flower, NonOrganic):
    def __init__(self, name):
        Flower.__init__(self, name)
        NonOrganic.__init__(self)