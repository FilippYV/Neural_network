import random

import numpy as np


# 3 на 5

class Neural:
    def __init__(self, inputs, weight, step, answers, last_error):
        self.inputs = inputs
        self.weight = weight
        self.step = step
        self.answers = answers
        self.last_error = last_error
        self.t = 0

    def train(self):
        eph = 0
        count = 0
        while count != len(self.inputs):
            self.summ_to_active = 0
            for i in range(len(self.inputs[count])):
                self.summ_to_active += self.inputs[count][i] * self.weight[i]
            self.summ_to_active -= self.t
            if self.summ_to_active > 0:
                self.summ_to_active = 1
            else:
                self.summ_to_active = -1
            if self.summ_to_active != self.answers[count]:
                for i in range(len(self.weight)):
                    self.weight[i] = round(self.weight[i] + self.inputs[count][i] * self.answers[count],
                                           5)
                    # print(self.weight[i], i)
                self.t = self.t - self.answers[count]
                count = 0
            else:
                count += 1
            eph += 1
            print(f'Эпоха №{eph} - ', self.weight)

    def start(self, new_value):
        self.train()
        print('Веса -', self.weight)
        final_answer = 0
        for i in range(len(new_value)):
            final_answer += new_value[i] * self.weight[i]
        final_answer -= self.t

        if final_answer >= 0:
            final_answer = 1
            print('Ответ:', final_answer)
        else:
            print('Ответ:', -1)


def random_weight():
    mass_weigh = []
    for i in range(15):
        mass_weigh.append(round(random.random(), 5))
    return mass_weigh


if __name__ == '__main__':
    last_error = 0
    step = 0.0001
    mass_value = [[-1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1],
                  [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1]]
    mass_answers = [1, 1]
    brain = Neural(mass_value, random_weight(), step, mass_answers, last_error)
    brain.start([-1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1])
    # [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1]
