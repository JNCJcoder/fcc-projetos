import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      self.contents += value * [key]

  def draw(self, balls_number):
    balls_number = min(balls_number, len(self.contents))
    return [
        self.contents.pop(random.randrange(len(self.contents)))
        for _ in range(balls_number)
    ]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0

  for index in range(0, num_experiments):
    counts = {}
    match = True
    temporaryHat = copy.deepcopy(hat)
    balls = temporaryHat.draw(num_balls_drawn)

    print("experiment:", index)

    for ball in balls:
      counts[ball] = counts.get(ball, 0) + 1

    for color in expected_balls:
      if counts.get(color, 0) < expected_balls[color]:
        match = False

    if match:
      success = success + 1

  return success / num_experiments
