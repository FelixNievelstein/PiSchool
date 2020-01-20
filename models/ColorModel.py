class ColorModel(object):
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class ColorHelper:

    @staticmethod    
    def whiteColor():
        return ColorModel(255, 255, 255)