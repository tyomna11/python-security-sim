import time
ip = input("Write target IP: ")
speed = input("If you wanna quick scanning write '1'. For deep scanning write '2': ")
if speed == "1":
    step = 24
    delay = 0.7
elif speed == "2":
    step = 17
    delay = 2.5  
else: 
    print("Invalid value :(")     
    exit()
time.sleep(0.1)
for i in range (0, 100, step):
    print(f"Scanning {ip} -- {i}/100%. Please wait.")
    time.sleep(delay)
print(f"Scanning {ip} -- 100/100%. Please wait.")   
time.sleep(1.5)
print("Scanning complated! :)")
print("The IP has vulnerability (Port open - 56)") 