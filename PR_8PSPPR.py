import random


class Neural:
    def __init__(self, inputs, weight, step, answers, last_error, epochs):
        self.inputs = inputs
        self.weight = weight
        self.step = step
        self.answers = answers
        self.last_error = last_error
        self.epochs = epochs
        self.t = 0

    def train(self):
        # for eph in range(self.epochs):
        for i in range(epochs):
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
        # print(f'Эпоха №{eph} -', self.weight)

    def start(self, new_value):
        self.train()
        print('\nВеса -', self.weight)
        final_answer = 0
        for i in range(len(new_value)):
            final_answer += new_value[i] * self.weight[i]
        final_answer -= self.t
        print(final_answer)

        if final_answer >= 0:
            print('Ответ:', 1)
        else:
            print('Ответ:', -1)


def random_weight(lens):
    mass_weigh = []
    for i in range(lens):
        mass_weigh.append(round(random.uniform(0, 1), 5))
    return mass_weigh


if __name__ == '__main__':
    last_error = 0
    step = 0.01
    epochs = 1
    mass_value = [[-1, -1, -1, -1],
                  [-1, -1, -1, 1],
                  [-1, -1, 1, -1],
                  [-1, -1, 1, 1],
                  [-1, 1, -1, -1],
                  [-1, 1, -1, 1],
                  [-1, 1, 1, -1],
                  [-1, 1, 1, 1],
                  [1, -1, -1, -1],
                  [1, -1, -1, 1],
                  [1, -1, 1, -1],
                  [1, -1, 1, 1],
                  [1, 1, -1, -1],
                  [1, 1, -1, 1],
                  [1, 1, 1, -1],
                  [1, 1, 1, 1]]
    mass_answers = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
    brain = Neural(mass_value,
                   random_weight(len(mass_value[0])),
                   step,
                   mass_answers,
                   last_error,
                   epochs)
    brain.start([1, 1, 1, 1])  # [temro_p_exist, cistem_coolers, cooler_coonect, cooler_dress, termopaste_o]
    # brain = Neural(mass_value, [0.69662, 0.95457, 0.57743, 0.88189, 0.00117], step, mass_answers, last_error, epochs)
    # brain.start_no_train([-1, -1, 1, -1, 1])
    # -1.62392, 1.21987, 0.30287, 4.63544, 2.55954]
    # [0.2610785717981914, 0.3120362810697661, 0.18129822721734645, 0.8696472194891667, 0.4112849481502139]
    # [0.40303695031574516, 0.17136774010442501, 0.20722382190355537, 0.07345584171503561, 0.785093661827062]
    # [0.25001, 0.3841, 0.72526, 0.53535, 0.79464]
