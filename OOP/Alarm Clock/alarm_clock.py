
class Alarm_Clock:
    def __init__(self, time):
        self.current_time = 1200
        self.is_on = False
        self.set_alarm_time = time

    def the_time(self, current):
        self.current_time = current
        print(f'the current time is: {self.current_time}')

    def turn_on(self):
        self.is_on = True
        print('Alarm has been turned on')

    def alarm_on_off(self):
        if self.is_on == False:
            print('alarm is off!')
        elif int(self.set_alarm_time) > 0:
            print(f'alarm on and is set to: {int(self.set_alarm_time)}')