class NonOrganic():

    def __init__(self):
        self.how_grown = "non organic"
        self.how_shipped = "however necessary"

    def __str__(self):
        return f'{self.name} can be shipped {self.how_shipped} and is grown {self.how_grown}'


class Organic():

    def __init__(self):
        self.how_grown = "organic"
        self.how_shipped = "non-refridgerated"

    def __str__(self):
        return f'{self.name} has to be shipped {self.how_shipped} because it is grown {self.how_grown}'

    
