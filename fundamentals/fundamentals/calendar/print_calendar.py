import calendar


class CalendarPrinter:

    def __init__(self, first_day_of_calendar = calendar.MONDAY):
        self.first_day_of_calendar = first_day_of_calendar
        pass

    def return_calendar_string(self):
        c = calendar.TextCalendar(self.first_day_of_calendar)
        return c.formatmonth(2019, 1, 0, 0)


if __name__ == "__main__":
    cp_monday = CalendarPrinter()
    cp_wednesday = CalendarPrinter(calendar.WEDNESDAY)
    print("Calendar which starts from Monday:")
    print(cp_monday.return_calendar_string())
    print("Calendar which starts from Wednesday:")
    print(cp_wednesday.return_calendar_string())
