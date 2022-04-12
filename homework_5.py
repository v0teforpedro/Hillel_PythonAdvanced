class Counter:

    # best way to set default value to immutable arguments is via '='
    def __init__(self, min_value=0, max_value=100, current_value=None):

        self.min = min_value
        self.max = max_value
        self.cur = current_value

        # check if current value available, otherwise set current as min.
        if not self.cur:
            self.cur = self.min

        # check correct input
        if self.min > self.max:
            raise ValueError('min_value cannot be more than max_value')

        if self.cur < self.min:
            raise ValueError('current_value cannot be less than min_value')

    def increase(self):

        # stop counter if max value is reached
        if self.cur < self.max:
            self.cur += 1

    def get_current_value(self):
        return self.cur


test = Counter(-11, -8, -10)
print(test.get_current_value())
test.increase()
test.increase()
test.increase()
print(test.get_current_value())
print('-------------')
test2 = Counter()
print(test2.get_current_value())
test2.increase()
test2.increase()
test2.increase()
test2.increase()
print(test2.get_current_value())
print('-------------')
test3 = Counter(1, 2)
print(test3.get_current_value())
test3.increase()
test3.increase()
test3.increase()
test3.increase()
print(test3.get_current_value())
