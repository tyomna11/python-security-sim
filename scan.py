import time
print("Simulator scanning IP for vulnerabilities by tywwyt :)")
ip = input("Write your IP address: ")
for i in range(0, 100, 17):
    time.sleep(2.5)
    print(f"Scaning is in progress for IP: {ip} --- {i}/100%. Please wait.")
time.sleep(2.5)    
print(f"Scaning is in progress for IP: {ip} --- 100/100%. Please wait.")   
time.sleep(0.2) 
print("Scaning completed! :)")
time.sleep(0.7)
print("Your IP has vulnerability (Port open: 80).")    