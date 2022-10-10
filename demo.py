class Points:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset(self):
        self.x = 0
        self.y = 0

    def replace(self):
        self.x =self.y


if __name__ == '__main__':
    pointer = Points()
    pointer.x = 10
    pointer.y = 20
    print(pointer.x, pointer.y)
    pointer.replace()
    print(pointer.x, pointer.y)
