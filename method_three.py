import time 
import sys 

print("Loading:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]10%","[■■□□□□□□□□]20%", "[■■■□□□□□□□]30%", "[■■■■□□□□□□]40%",\
              "[■■■■■□□□□□]50%", "[■■■■■■□□□□]60%", "[■■■■■■■□□□]70%",\
                  "[■■■■■■■■□□]80%", "[■■■■■■■■■□]90%", "[■■■■■■■■■■]100%"]

for i in range(len(animation)):
    time.sleep(0.4)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")