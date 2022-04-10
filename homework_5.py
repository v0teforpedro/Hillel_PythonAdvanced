class Counter:

    def __init__(self, min_value=0, max_value=100, current_value=0):
        self.min = min_value
        self.max = max_value
        self.cur = current_value

    def increase(self):
        if self.min < 0 or self.max > 100 or self.cur == self.max:
            return 'Out of range'
        elif self.min > self.cur:
            self.cur = self.min
            self.cur += 1
            return self.cur
        else:
            self.cur += 1
            return self.cur

    def get_current_value(self):
        return self.cur

print('Без параметров')
counting = Counter()
print(counting.get_current_value())
print(counting.increase())
print(counting.get_current_value())
print(counting.increase())
print(counting.increase())
print(counting.increase())

print('С параметрами')
counting2 = Counter(97, 100, 94)
print(counting2.get_current_value())
print(counting2.increase())
print(counting2.get_current_value())
print(counting2.increase())
print(counting2.increase())
print(counting2.increase())

print('Не все параметры')
counting2 = Counter(97)
print(counting2.get_current_value())
print(counting2.increase())
print(counting2.get_current_value())
print(counting2.increase())
print(counting2.increase())
print(counting2.increase())
