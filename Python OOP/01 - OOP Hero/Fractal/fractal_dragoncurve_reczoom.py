# import turtle

# class DragonCurve:
#     def __init__(self, iterations=10, length=10):
#         self.iterations = iterations
#         self.length = length
#         self.window = turtle.Screen()
#         self.window.title("Dragon Curve Fractal")
#         self.turtle = turtle.Turtle()
#         self.turtle.speed(0)  # Set kecepatan maksimal
#         self.turtle.hideturtle()
#         self.turtle.penup()
#         self.turtle.goto(-200, 0)  # Memulai dari titik tertentu
#         self.turtle.pendown()
#         self.turtle.speed(0)

#     def dragon_curve(self, axiom="FX", rules=None):
#         if rules is None:
#             rules = {"X": "X+YF+", "Y": "-FX-Y"}

#         # Generate string berdasarkan aturan
#         result = axiom
#         for _ in range(self.iterations):
#             result = "".join(rules[char] if char in rules else char for char in result)
#         return result

#     def draw(self, instructions):
#         for command in instructions:
#             if command == "F":  # Move forward
#                 self.turtle.forward(self.length)
#             elif command == "+":  # Turn right
#                 self.turtle.right(90)
#             elif command == "-":  # Turn left
#                 self.turtle.left(90)

#     def run(self):
#         instructions = self.dragon_curve()
#         self.draw(instructions)
#         self.window.mainloop()

# # Jalankan Dragon Curve dengan 12 iterasi dan panjang garis 10
# dragon = DragonCurve(iterations=12, length=8)
# dragon.run()
