class counter(object):
    def __init__(self, limit, initial, min_digits):
        self.limit = limit
        self.count = initial
        if (self.count>self.limit) or (self.count < -1):
            self.count = self.limit-1
            print("The input for initial value is invalid, and is set to be limit-1")
        self.min_digits = min_digits

    def get_value(self):
        return self.count

    def __str__(self):
        value = str(self.count)
        value = len(value)
        value = self.min_digits - value
        return (value*"0")+str(self.count)

    def tick(self):
        self.count = self.count-1
        if self.count < 0:
            self.count = self.limit - 1
            return True
        else:
            return False

my_counter = counter(6, 7, 2)
print(my_counter)
print(my_counter.get_value())
for i in range(6):
 print(my_counter.tick())
print(my_counter)
