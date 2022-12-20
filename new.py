class Neuron:
    def __init__(self):
        self.weight = 0.6209990000243143
        self.last_error = 6.209990000243143
        self.smoothing = 0.00001

    def get_last_error(self):
        return self.last_error

    def get_smoothing(self):
        return self.smoothing

    def get_weight(self):
        return self.weight

    def process_input_data(self, input_data):
        return input_data * self.weight

    def train(self, input, expectedResult):
        result_now = input * self.weight
        self.last_error = expectedResult - result_now
        correction = self.last_error / result_now
        correction = correction * self.smoothing
        self.weight += correction
    def check_training(self):
        if(self.last_error > self.smoothing or self.last_error < -self.smoothing):
            return True
        else:
            return False


neuron = Neuron()
input_data = 120
# expectedResult = 6.21
# print(neuron.process_input_data(input_data))
# iteration = 1
# while neuron.check_training():
#     neuron.train(input_data, expectedResult)
#     print("Iteration: " + str(iteration) + " | Weight: " + str(neuron.get_weight()))
#     iteration += 1
# print("-=-Successful Training---")
# print(neuron.get_weight())
print(neuron.process_input_data(input_data))