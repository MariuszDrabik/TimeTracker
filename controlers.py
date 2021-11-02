from datetime import datetime, timedelta
from repositories import ProjectRepository, TrackRepository


class Time:
    def __init__(self, start: datetime, stop: datetime):
        self._start = start
        self._stop = stop
        self._total_seconds = self.seconds()

    def __str__(self) -> str:
        return str(timedelta(seconds=self._total_seconds))

    def seconds(self):
        self._total_seconds = (self._stop - self._start).total_seconds()
        return self._total_seconds

    def save(self):
        return self._total_seconds


class TimeDuration:
    def __init__(self, time):
        self._time = time

    @classmethod
    def form_data(cls, tracks: list):
        return cls(sum(tracks))


class Project:
    def get_all(self):
        return [f'{i[0]} {i[1]}' for i in ProjectRepository().get_all()]

    def save(self, name):
        ProjectRepository().save(name)
        return 1


class Tracks:
    def get_all(self):
        return TrackRepository().get_all()

    def get_all_by_id(self):
        pass

    def save(self, project_id, start_time, end_time, project_time: Time):
        TrackRepository().save(project_id, start_time, end_time, project_time)


# ??timedelta??
class TimeParser:
    def __init__(self, days, hours, minuts, seconds):
        self.days = days
        self.hours = hours
        self.minuts = minuts
        self.seconds = seconds

    def __str__(self) -> str:
        time = list(map(lambda x: str(x), [
            self.hours, self.hours, self.minuts, self.seconds]))
        for i, j in enumerate(time):
            if len(time[i]) == 1:
                time[i] = f'0{j}'

        return f'{time[0]}d {time[1]}:{time[2]}:{time[3]}'

    @classmethod
    def from_timedelta_string(cls, delta: str = '00:00:00'):
        time = list(map(lambda x: int(float(x)), delta.split(':')))
        print(time)
        days = 0
        hours, minuts, seconds = time

        if seconds > 60:
            minuts = minuts + round(seconds / 60)
            seconds = round(seconds % 60)

        if minuts > 60:
            hours = hours + round(minuts / 60)
            minuts = round(minuts % 60)

        if hours > 24:
            days = round(hours / 24)
            hours = hours % 24
            minuts = minuts
            seconds = round(time[2])

        return cls(days, hours, minuts, seconds)


# if __name__ == '__main__':
#     Project().save('Jeden')
#     Project().save('dwa')
#     Project().save('Trzy')
#     s_time = datetime(2021, 11, 1, 6, 10, 11)
#     e_time = datetime(2021, 11, 1, 12, 36, 2)

#     Tracks().save(3, s_time, e_time, (e_time - s_time).total_seconds())
#     print((e_time - s_time).total_seconds())
#     print(timedelta(seconds=2759151.0))
#     print(TimeParser.from_timedelta_string(str(e_time - s_time)))
