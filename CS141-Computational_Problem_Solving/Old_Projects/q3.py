class counter(object):
    def __init__(self, limit, initial, min_digits):
        self.__limit = limit
        self.__count = initial
        if (self.__count>self.__limit) or (self.__count < 0):
            self.__count = self.__limit-1
            print("The input for initial value is invalid, and is set to be limit-1")
        self.__min_digits = min_digits

    def get_value(self):
        return self.__count

    def __str__(self):
        value = str(self.__count)
        value = len(value)
        value = self.__min_digits - value
        return (value*"0")+str(self.__count)

    def tick(self):
        self.__count = self.__count-1
        if self.__count < 0:
            self.__count = self.__limit - 1
            return True
        else:
            return False
