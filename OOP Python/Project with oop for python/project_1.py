import time
# # print("Starting.....")
# # time.sleep(2)
# # print("After 2 secound")

# current_time = time.time()
# # print(current_time)

# d = time.gmtime()
# # print(d)

# localTime = time.localtime()
# # print(localTime)


# formatTime = time.strftime("%Y-%m-%d  %H:%M:%S")
# print(formatTime)

# print()


# start = time.perf_counter()
# end = time.perf_counter()

# # print(f"Elapsed time: {end - start} secounds")

# start1 = time.monotonic()
# end1 = time.monotonic()

# # print(f"Elapsed time: {end1 - start1} secounds")


# readable_time = time.asctime()
# print(readable_time)







# Create a python program capable of greeting you with good morning, good afternoon, good evening . your program should use time module to get the current hour.

# currentTime = time.strftime('%H:%M:%S')
# print(currentTime)

# current_Hour = int(time.strftime('%H'))
# print(current_Hour)

# Minute = int(time.strftime('%M'))
# print(Minute)

# Secound = int(time.strftime('%S'))
# print(Secound)

current_Hour = int(input("Enter your time: "))

if(current_Hour >= 0 and current_Hour < 12):
    print("Good morning")
elif(current_Hour >= 12  and current_Hour < 15):
    print("Good afternoon")
elif (current_Hour >=15 and current_Hour < 17):
    print("Good twilight")
elif(current_Hour >=17 and current_Hour <19):
    print("Good evening")
elif(current_Hour >=19 and current_Hour < 24):
    print("Good night")

    





