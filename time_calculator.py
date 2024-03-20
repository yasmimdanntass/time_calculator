def round_up(number):
    return -(-number // 1)
def add_time(start, duration, week_day=''):
  # format the variables
  formatted_start = start.replace(':','').replace('AM','').replace('PM','').replace(' ','')
  formatted_duration = duration.replace(':','').replace(' ','')
  # create a variable to the period
  period = ''
  # create a variable to the new date
  new_date = ''
  # turn the variables into integers and then minutes
  start_mins = int(int(formatted_start)/100)*60 + int(formatted_start)%100
  duration_mins = int(int(formatted_duration)/100)*60 + int(formatted_duration)%100
  # get the sum
  total_mins = start_mins + duration_mins
  hrs = int((total_mins / 60 ) % 24)
  mins = int(total_mins % 60)
  if mins < 10:
      mins = '0' + str(mins)
  # convert to the am/pm system
  if hrs >= 12:
    if hrs == 12:
        if 'AM' in start:
            period = 'PM' 
        else:
           period = 'AM'
    else:
        hrs -=12
        if 'AM' in start:
            period = 'PM'
        else:
            period = 'AM'
  else:
     if 'AM' in start:
            period = 'AM' 
     if 'PM' in start:
            period = 'PM'
     
  # deal with the number of days passed
  days = total_mins / (24 * 60)
  if "PM" in start and period == "AM":
    new_date = ' (next day)'
  if 1 <= days < 1.5:
    days = int(days)
    new_date = ' (next day)'
  elif days > 1.5:
    days = int(round_up(days))  # assuming the round_up function rounds up to the nearest integer
    new_date = f' ({days} days later)'
  # deal with the week day if provided
  if week_day:
      week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(week_day.capitalize())
      new_index = int(int(week) + int(days)) % 7
      new_day = ', ' + ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')[new_index]
  else:
      new_day = ''
  new_time = f'{hrs}:{mins} {period}{new_day}{new_date}'
  print(new_time)
  return new_time

add_time("11:59 PM", "0:01")

