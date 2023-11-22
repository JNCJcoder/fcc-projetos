def add_time(start, duration, start_day=False):
  week = [
      "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
      "Saturday"
  ]

  currentTime = start.split(":")
  currentTimeHour = int(currentTime[0])
  currentTimeMinutes = int(currentTime[1].split(" ")[0])
  currentTimeHourType = currentTime[1].split(" ")[1]

  nextTime = duration.split(":")
  nextTimeHour = int(nextTime[0])
  nextTimeMinutes = int(nextTime[1])

  finalHour = (currentTimeHour + nextTimeHour)
  finalMinutes = (currentTimeMinutes + nextTimeMinutes)
  finalHourDays = ""
  finalHourType = "AM"
  finalWeek = ""

  days = 0

  if currentTimeHourType == "PM":
    finalHour += 12

  while finalMinutes >= 60:
    finalMinutes -= 60
    finalHour += 1

  while finalHour >= 24:
    finalHour -= 24
    days += 1

  if finalHour >= 12 and finalHour < 24:
    finalHourType = "PM"
  elif finalHour >= 0 and finalHour < 12:
    finalHourType = "AM"

  if finalHour > 12:
    finalHour -= 12

  if finalHour == 0:
    finalHour = 12

  if start_day:
    startDayWeek = week.index(start_day.capitalize())
    finalWeek = week[(days + startDayWeek) % 7]

  if days == 1:
    finalHourDays = f'(next day)'
  elif days > 1:
    finalHourDays = f'({days} days later)'

  new_time = f'{finalHour}:{str(finalMinutes).zfill(2)} {finalHourType}'

  if start_day:
    new_time += f', {finalWeek}'
  if days > 0:
    new_time += f' {finalHourDays}'

  return new_time
