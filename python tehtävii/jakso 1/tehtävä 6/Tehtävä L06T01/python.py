def showtime(sec):
    hours = sec // 3600
    minutes = (sec % 3600) // 60
    seconds = sec % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

print(showtime(500))
print(showtime(10000))
print(showtime(121000))