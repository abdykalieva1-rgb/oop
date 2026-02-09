class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        return f"Box({self.length} × {self.width} × {self.height})"

    def __eq__(self, other):
        if isinstance(other, Box):
            return (self.length == other.length and
                    self.width == other.width and
                    self.height == other.height)
        return NotImplemented

b1= Box(2.5, 4,5)
b2 = Box(2, 3, 4)
b3 = Box(2.5, 4, 5)

print(b1)
print(b2)
print(b3)

print(f"{b3} == {b1} → {b3 == b1}")
print(f"{b1} == {b3} → {b1 == b3}")
print(f"{b1} == {b2} → {b1 == b2}")






