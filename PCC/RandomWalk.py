from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.xvalues = [0]
        self.yvalues = [0]

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.xvalues) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.xvalues[-1] + x_step
            y = self.yvalues[-1] + y_step

            self.xvalues.append(x)
            self.yvalues.append(y)
