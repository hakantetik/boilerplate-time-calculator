def add_time(start, duration, day=None):

  #başlangıç zamanları
  start_hour = int(((start.split())[0].split(":"))[0])
  start_min = int(((start.split())[0].split(":"))[1])
  day_time = start.split()[1]

  #eklenecek zamanlar
  adding_mins = int(duration.split(":")[1])
  adding_hours = int(duration.split(":")[0])

  plus_day = 0

  new_min = start_min + adding_mins
  if day_time == "PM":
    start_hour += 12
  new_hour = (start_hour + adding_hours)

  if new_min >= 60:
    new_hour += new_min // 60
    new_min = new_min % 60
  if new_min < 10:
    new_min = f"0{new_min}"

  if new_hour >= 24:
    plus_day += new_hour // 24
    new_hour = new_hour % 24
    
  day_string = None

 

  if new_hour < 12:
    day_time = "AM"
    if new_hour == 0:
      new_hour = 12
  elif new_hour > 12:
    day_time = "PM"
    new_hour -= 12
  elif new_hour == 12:
    day_time = "PM"
  

  

  if plus_day == 1:
    day_string = "(next day)"
  if plus_day > 1:
    day_string = f"({plus_day} days later)"

  days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  ]

  if day != None:
    new_day = day.lower().capitalize()
    day_index = days.index(new_day)
    new_day = days[(day_index + plus_day) % len(days)]
  else: 
    new_day = None
  


  new_time = f"{new_hour}:{new_min} {day_time}"

  # new_day ve day_string ekle

  if new_day != None:
    new_time = new_time + ", " + new_day
  if day_string != None:
    new_time = new_time + " " + day_string
  
  return new_time