class BaseItem:
    def __init__(self):
        self.weight = 0
        self.price = 0


class Weapon(BaseItem):
    pass


class Defense(BaseItem):
    pass


class Common(BaseItem):
    pass