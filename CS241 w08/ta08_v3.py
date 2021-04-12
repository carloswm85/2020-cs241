import math


class Time:
    def __init__(self):
        self.time_secs = 0

    '''@property
    def get_hours_simple(self):
        if self._hour > 12:
            return self._hour - 12

    @property
    def get_period(self):
        if self._hour < 12:
            return 'AM'
        else:
            return 'PM'''''

    # HOURS
    def get_hour(self):
        return math.floor(self.time_secs / 3600)

    def set_hour(self, value):
        self.time_secs = value * 3600
        print('Value: {} time_secs: {}'.format(value, self.time_secs))

    # MINUTES
    def get_min(self):
        temp = math.floor(self.time_secs % 60)
        return math.floor(temp / 60)

    def set_min(self, value):
        temp = value * 60
        self.time_secs += temp
        print('Value: {} temp: {} time_secs: {}'.format(value, temp, self.time_secs))

    # SECONDS
    def get_sec(self):
        temp = self.time_secs % 3600
        temp %= 60
        return temp

    def set_sec(self, value):
        self.time_secs += value
        print('Value: {} time_secs: {}'.format(value, self.time_secs))

    h = property(get_hour, set_hour)
    m = property(get_min, set_min)
    s = property(get_sec, set_sec)


def main():
    clock = Time()

    # hour = int(input('Enter hours: '))
    # minutes = int(input('Enter minutes: '))
    # sec = int(input('Enter seconds: '))
    # clock.h = hour
    # clock.m = minutes
    # clock.s = sec

    print('Enter hours: ')
    clock.h = 48
    print('Enter minutes: ')
    clock.m = 120
    print('Enter seconds: ')
    clock.s = 90

    print('Hours: {}'.format(clock.h))
    print('Minutes: {}'.format(clock.m))
    print('Seconds: {}'.format(clock.s))
    # print(clock.get_period)
    # print(clock.get_hours_simple)


if __name__ == '__main__':
    main()
