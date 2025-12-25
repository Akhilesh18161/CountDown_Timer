import time

sec_entered = int(input("Enter time in second: "))

for x in range(sec_entered, 0, -1):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{second:02}")
print("Time's Up!")
