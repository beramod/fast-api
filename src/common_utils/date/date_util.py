import calendar
from datetime import datetime, timedelta
from src.common_utils.string.string_util import StringUtil

class DateUtil:
    @classmethod
    def get_default_day(cls, date=None):
        return StringUtil.getDigit(date) if date else datetime.now().strftime('%Y%m%d')

    @classmethod
    def get_date_from_string(cls, value):
        yyyyMMdd = StringUtil.getDigit(value)
        return datetime.strptime(yyyyMMdd.ljust(14, '0'), '%Y%m%d%H%M%S')

    @classmethod
    def get_last_day(cls, year, month):
        return calendar.monthrange(int(year), int(month))[1]

    @classmethod
    def get_from_to_date(cls, year, month):
        fromDateAt = datetime.strptime(year+month+'01', '%Y%m%d')
        lasyday = str(cls.get_last_day(year, month))
        toDateAt = datetime.strptime(year+month+lasyday+'235959', '%Y%m%d%H%M%S')
        return fromDateAt, toDateAt

    @classmethod
    def check_before_day(cls, check_value, test_value=None):
        check_dtm = cls.get_date_from_string(check_value).strftime('%Y%m%d')
        test_dtm = cls.get_date_from_string(test_value).strftime('%Y%m%d') if test_value else cls.get_add_date().strftime('%Y%m%d')
        return check_dtm <= test_dtm

    @classmethod
    def get_add_date(cls, add_days=0, date=None):
        now = datetime.now() if date is None else cls.get_date_from_string(date)
        return now + timedelta(add_days)

    @classmethod
    def get_add_day(cls, add_days=0, date=None):
        if date is None:
            date = datetime.now()
        add_day = date + timedelta(add_days)
        return add_day.strftime('%Y%m%d')[2:]

    @classmethod
    def check_date_type(cls, date):
        return type(date) is datetime

    @classmethod
    def get_last_month(cls, year=None, month=None):
        if year is None or month is None:
            now = datetime.now()
            if year is None:
                year = now.year
            if month is None:
                month = now.month

        if 0 < month - 1:
            month = month - 1
        else:
            year = year - 1
            month = 12
        return str(year), str(month).rjust(2,'0')

    @classmethod
    def str_to_datetime(cls, datetime_at):
        yy = int('20' + datetime_at[:2])
        mm = int(datetime_at[2:4])
        dd = int(datetime_at[4:6])
        HH = int(datetime_at[6:8])
        MM = int(datetime_at[8:10])
        SS = int(datetime_at[10:12])
        return datetime(yy, mm, dd, HH, MM, SS)

    @classmethod
    def get_date_at(cls, date: datetime = None) -> str:
        if not date:
            date = datetime.now()
        return date.strftime('%y%m%d')

    @classmethod
    def get_datetime_at(cls, date: datetime = None) -> str:
        if not date:
            date = datetime.now()
        return date.strftime('%y%m%d%H%M%S')

    @classmethod
    def makeYymms(cls):
        now = datetime.now()
        coll_names = []
        year = int(now.strftime('%y'))
        month = int(now.strftime('%m'))

        for i in range(0, 12):
            coll_name = '{}{}'.format(str(year), ('0' if month < 10 else '') + str(month))
            coll_names.append(coll_name)
            month -= 1
            if month == 0:
                year -= 1
                month = 12
        coll_names.sort()
        return coll_names

    @classmethod
    def get_refined_now(self):
        now = datetime.now()
        minute = int(now.strftime('%M'))
        hour = int(now.strftime('%H'))
        day = int(now.strftime('%d'))
        month = int(now.strftime('%m'))
        weekday = now.weekday() + 1
        refined_time = [minute, hour, day, month, weekday]
        return refined_time