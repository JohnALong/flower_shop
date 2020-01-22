from flowers import Flower
from flowers.grown_shipped import Organic

class Baby_Breath(Flower, Organic):
    def __init__(self, name):
        Flower.__init__(self, name)
        Organic.__init__(self)