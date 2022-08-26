#reference at https://codereview.stackexchange.com/questions/46482/bank-atm-program-in-python
import time, json, sys, random, os, pickle

#decoration
def loading():
  print("Loading", end = "") 
  timeset = round(random.uniform(1, 3), 2)
  t_end = time.time() + timeset
  
  for x in "...":
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.6)
    
  while time.time() < t_end:
    os.system("clear")
    loading()
    break 

def loading2():
  print("\nLoading", end = "") 
  timeset = round(random.uniform(1, 3), 2)
  t_end = time.time() + timeset
  
  for x in "...":
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.6)
    
  while time.time() < t_end:
    os.system("clear")
    loading()
    break 

def saving():
  print("\nSaving", end = "") 
  timeset = round(random.uniform(1, 3), 2)
  t_end = time.time() + timeset
  
  for x in "...":
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.6)
    
  while time.time() < t_end:
    os.system("clear")
    loading()
    break 

def loggingout():
  print("Logging Out", end = "") 
  timeset = round(random.uniform(1, 3), 2)
  t_end = time.time() + timeset
  
  for x in "...":
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.6)
    
  while time.time() < t_end:
    os.system("clear")
    loading()
    break 




#modes

#data save
data_dict = {"Pin":"0", "Balance":0.0}
with open("data.pickle", "wb") as f:
  pickle_save = pickle.dump(data_dict, f)          



#deposit
def deposit():
  pickle_read = open("data.pickle" , "rb")
  pickle_load = pickle.load(pickle_read)
  balance = pickle_load["Balance"]
  print("\n\nBALANCE : RM" + str(balance))
  deposit = round(float(input("Insert your desired amount > ")), 2)
  loading2()
  balance += deposit
  print("\nSuccess!")
  print("NEW BALANCE : RM" + str(balance))
  data_dict["Balance"] = balance
  with open("data.pickle", "wb") as f:
   pickle_save = pickle.dump(data_dict, f)

  time.sleep(3)
  
  saving()
  
#withdraw
def withdraw():
  pickle_read = open("data.pickle" , "rb")
  pickle_load = pickle.load(pickle_read)
  balance = pickle_load["Balance"]
  print("\n\nBALANCE : RM" + str(balance))
  withdraw = int(input("How much would you like to withdraw? > "))
  loading2()
  
  if balance > 20:
    balance -= withdraw
    print("\nSuccess!")
    print("NEW BALANCE : RM" + str(balance))
    data_dict["Balance"] = balance
    with open("data.pickle", "wb") as f:
      pickle_save = pickle.dump(data_dict, f)

    time.sleep(3)
    
    saving()
  else:
    print("\nInsufficient funds in account. Please deposit more money")

#fundtransfer
def fundtrans():
  pickle_read = open("data.pickle" , "rb")
  pickle_load = pickle.load(pickle_read)
  balance = pickle_load["Balance"]
  
  put = input("""\n\nPlease type the 12 digit account number you wish to transfer > """)
  if len(put) != 12:
    print("This account number is not 12 digits")
    
  else:
    
    loading2()
    cashamo = float(input("\nEnter the amount of money you wish to transfer > "))
    loading2()
    if balance > 20:
      balance -= cashamo
      print("\nSuccess!")
      print("NEW BALANCE : RM" + str(balance))
      data_dict["Balance"] = balance
      with open("data.pickle", "wb") as f:
        pickle_save = pickle.dump(data_dict, f)

      time.sleep(3)
      
      saving()
    else: 
      print("\nInsufficient funds in account. Please deposit more money")

#balance checking
def balcheck():
  pickle_read = open("data.pickle" , "rb")
  pickle_load = pickle.load(pickle_read)
  balance = pickle_load["Balance"]
  print("\nBALANCE : RM" + str(balance))

#change pin
def pinchange():
  pin = input("\nPlease set your new 4 digit pin number > ")
  while True:  
    while len(pin) == 4:
      data_dict["Pin"] = pin
      with open("data.pickle", "wb") as f:
        pickle_save = pickle.dump(data_dict, f)
      loading()
      os.system("clear")
      return True
    else:
      print("Error, your pin number is not 4 digits")
      return False

#logout
def logout():
  print("\nPlease come again soon")
  time.sleep(2)
  loggingout()
  print("\n")
  sys.exit()
  
 
 


    
  



        



#true pin
def pinsetup(pin):
  if pin == data_dict["Pin"]:
    return True
  else:
    return False



#logging in
def pintype():
  tries = 0
  atmps = 3
  while tries <= 2:
    print("You have " + str(atmps) + " attempt/s left")
    pin = input("Insert your 4 digit pin number > ")
    if pinsetup(pin):
      print("\nPin accepted!")
      return True
    
    else:
      print("\nInvalid pin number")
      tries += 1
      atmps -= 1

  print("Amount of tries exceeded. Unable to login")
  return False


#set pin
def setpin():
  pickle_read = open("data.pickle" , "rb")
  pickle_load = pickle.load(pickle_read)
  pin = pickle_load["Pin"]
  if pin == "0": 
    pin3 = input("Please set your 4 digit pin number > ")
    while True:  
      while len(pin3) == 4:
        data_dict["Pin"] = pin3
        with open("data.pickle", "wb") as f:
          pickle_save = pickle.dump(data_dict, f)
        loading()
        os.system("clear")
        return True
      else:
        print("Error, your pin number is not 4 digits")
        return False

    

#atm menu
def startmenu():
  if setpin():
    print("Welcome to the ATM")
    if pintype():
      loading()
      while True: 
        cho = input("""\n\nWould you like to:
        1) Deposit         2) Withdraw
        3) Fund transfer   4) Balance checking                         5) Change pin      6) Logout
        Answer: """)
        if cho == "1" and "1)" and "1." and "Deposit" and "deposit" and "DEPOSIT":
          loading()
          deposit()
          continue

        elif cho == "2" and "2)" and "2." and "Withdraw" and "withdraw" and "WITHDRAW":
          loading()
          withdraw()
          continue
        
        elif cho == "3" and "3)" and "3." and "Fund Transfer" and "fund transfer" and "FUND TRANSFER":
          loading()
          fundtrans()
          continue

        elif cho == "4" and "4)" and "4." and "Balance checking" and "balance checking" and "BALANCE CHECKING":
          loading()
          balcheck()
          continue

        elif cho == "5" and "5)" and "5." and "Change pin" and "change pin" and "CHANGE PIN":
          loading()
          pinchange()
          continue

        elif cho == "6" and "6)" and "6." and "Logout" and "logout" and "LOGOUT":
          loading()
          logout()
          continue

        else: 
          print("An Error Occured")
          break
          


startmenu()


  
