from datetime import datetime, timedelta  
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):

	def __init__(self, events, year=None, month=None):
		self.events = events
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<dt> {event.title} </dt><dd> {event.description} </dd>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	def formatmonth(self, year, month):
		events = Event.objects.filter(start_time__year=year, start_time__month= month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(year, month, withyear=True)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(year, month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
