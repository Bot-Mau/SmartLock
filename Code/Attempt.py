# this for attempt
import lockdown
import main

from datetime import datetime, date

#this is for get date and time function
def get_time():
        now = datetime.now()
        
        current_time = now.strftime("%H:%M:%S")
        return(current_time)

def get_date():
    today = date.today()
    
    current_date = today.strftime("%m/%d/%Y")
    return (current_date)


#this for get log and check log
def log(a):
    code = str(a)
    f = open("log.txt", "a")
    f.write("code : " + code + '\n')
    f.write("time : "  + get_time() + '\n')
    f.write("date : " + get_date()+ '\n')
    f.write("\n")
    f.close()


def Attempts(count,password):
   log(password)
   if (count > 0):
        count -= 1
        return (main.Main(count))
   else:
        lockdown.lockdown()
        return (main.Main(0))
    

   

    