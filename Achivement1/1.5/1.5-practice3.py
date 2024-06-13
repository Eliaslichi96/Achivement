class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __gt__(self, other):
        if self.feet > other.feet:
            return True
        elif self.feet == other.feet and self.inches > other.inches:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.feet > other.feet:
            return True
        elif self.feet == other.feet and self.inches >= other.inches:
            return True
        else:
            return False

    def __ne__(self, other):
        return not (self.feet == other.feet and self.inches == other.inches)

# Test cases
print(Height(4, 6) > Height(4, 5))
print(Height(4, 5) >= Height(4, 5))
print(Height(5, 9) != Height(5, 10))
