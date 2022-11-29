"""Melon and Squash classes."""

import robots


class Melon:
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.\
        melon_type: type of melon being built.
        """
        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return f"{self.color} {self.weight:.2f} lbs {self.melon_type}"


class Squash(Melon):
    """Winter squash."""
    #  ^bc of the line in ship proced.:
    #  else:
    #             melon = Squash(melon_type)
    def __init__(self, melon_type):
        super().__init__("Winter Squash")
        self.melon_type = melon_type
        

    def prep(self):
        """prep and paint unripe squash green to fool customers"""
        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
        robots.painterbot.paint(self)


#ORIGINAL ERROR:
# Fulfilling order of 4 Winter Squash
# -----

# Traceback (most recent call last):
#   File "/Users/Erikka/src/homework/melon-production/shipping_procedure.py", line 113, in <module>
#     assess_and_pack_orders()
#   File "/Users/Erikka/src/homework/melon-production/shipping_procedure.py", line 84, in assess_and_pack_orders
#     melon = Squash(melon_type)
# TypeError: Squash.__init__() takes 1 positional argument but 2 were given