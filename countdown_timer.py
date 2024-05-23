import time
duration = int(input("Timer duration? (in seconds): "))
print("Timer will be set for " + str(duration) + " seconds")
confirmation=""
while not confirmation=="Yes": 
    confirmation= input("Start now? (Yes/No) ")
for countdown in range(int(duration),0,-1):
    time.sleep(1)
    print(str(countdown))
print("Your " + str(duration) + " seconds are up!")
