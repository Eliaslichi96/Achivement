# height.py

class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        # Normalize the height if inches are 12 or more
        self.normalize()

    def normalize(self):
        if self.inches >= 12:
            extra_feet = self.inches // 12
            self.feet += extra_feet
            self.inches = self.inches % 12

    def __sub__(self, other):
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches
        result_inches = total_inches_self - total_inches_other

        if result_inches < 0:
            raise ValueError("Resulting height cannot be negative")

        result_feet = result_inches // 12
        result_remaining_inches = result_inches % 12
        return Height(result_feet, result_remaining_inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

# Test the __sub__ method
height1 = Height(5, 10)  # 5 feet 10 inches
height2 = Height(3, 9)   # 3 feet 9 inches

result_height = height1 - height2

print(f"Resulting height: {result_height}")
