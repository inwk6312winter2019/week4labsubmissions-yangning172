class Time:
    def time_to_int(self):
        minutes = self.hour*60 + self.minute
        seconds = minutes*60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

