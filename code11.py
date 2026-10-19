import time

year = int(input("Enter a year: "))
start = time.perf_counter()

if year % 400 == 0:
    result = "Leap year"
elif year % 100 == 0:
    result = "Not a leap year"
elif year % 4 == 0:
    result = "Leap year"
else:
    result = "Not a leap year"

end = time.perf_counter()
print(result)
print("Time taken:", (end - start) * 1000, "ms")