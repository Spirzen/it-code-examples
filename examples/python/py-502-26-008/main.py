class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        import datetime
        now = datetime.date.today()
        return cls(now.year, now.month, now.day)

d1 = Date(2026, 1, 31)
d2 = Date.from_string("2026-01-31")
d3 = Date.today()
