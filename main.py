class IntegralCalculator:
    accuracy = 0.5
    def __init__(self, accuracy=0.5):
         self.accuracy = accuracy

    def calculate(self, precision = accuracy):
        self.accuracy = precision

        cut_precision = precision
        cut_range = 0
        for i in range(100): #how much will we cut from integral
            cut_precision /= 2
            cut_range = self._cut_range(cut_precision)
            if cut_range != False:
                break
        if cut_range == False:
            raise Exception("no range to cut")


    def _cut_range(self, accuracy):
        cut_distance = 1/4

        for i in range(0, 10):
            cut_distance /= 2
            accuracy_loss = self._cut_range_loss(cut_distance)
            if accuracy_loss < accuracy:
                return cut_distance
        return False
    @staticmethod
    def _cut_range_loss(cut_distance): #TODO: u'now make it do what it suppouse
        return 10

if __name__ == '__main__':
    print("hello world")
    integral = IntegralCalculator(accuracy=0.5)
    integral.calculate()
