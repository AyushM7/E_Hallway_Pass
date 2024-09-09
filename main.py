import time

def newLine():
  print(" ")
  print("________________________________________________")
  print(" ")
  print(" ")
  

def newSCAN():
  while True:
    ID = input("Scan your id please: ") 
    before = int(round(time.time()));
    cID = input("Please scan ID when you get back: ")
    after = int(round(time.time()))
    
    if cID == ID:
      stamp = after - before
      
      if(stamp <= 20 & stamp > 0):
        print(" ")
        print("Did you even leave?")
        newLine()
        newSCAN()
        
      elif (stamp < 60):
        print(" ")
        print("Welcome back, you were out for "+ str(stamp) + " seconds.")
        newLine()
        newSCAN()
        
      elif (stamp > 60) & (stamp < 600):
        print(" ")
        print("Welcome back, you were out for "+ str(stamp//60) + " minutes.")
        newLine()
        newSCAN()
        
      else:
        print(" ")
        print("Where have you been?")
        newLine()
        newSCAN()    
newSCAN()