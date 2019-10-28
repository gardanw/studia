class Vec2 :

    def __init__(self, *args: float()):
        if type(args[0]) == list:
            self.x = args[0][0]
            self.y = args[0][1]
        else:
            self.x = args[0]
            self.y = args[1]

    def __str__(self):
        string = str()
        string += str(self.x) + ', ' + str(self.y)
        return string

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self.add(other)

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __sub__(self, other):
        return self.sub(other)

    def __isub__(self, other):
        return self.sub(other)



if __name__ == "__main__":
    w1 = Vec2([1, 2])
    w2 = Vec2(1, 3)
    w2 -= w1
    print(w2)