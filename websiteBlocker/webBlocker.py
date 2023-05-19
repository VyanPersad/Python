#To run python files in the background then change the extension to .pyw so the file now
#becomes python_file.pyw
#Once selected/clicked there will be no terminal show it will work, however you will
#need to go to task manager to see it run.
#Also you will need to run the file as an administrator

#The other aspect of this program would be to schedule the script execution in windows
#Got to Task Scheduler in windwows and schedule a task and set it to highest privledges
#In the actions tab you will select your python script.

import time
#Note how we assign dt to datetime
from datetime import datetime as dt
#If you were to actually implement the script thenn this is the filepath of the host file
#on the local machine.

#hostfilepath="C:\Windows\System32\drivers\etc\hosts"
#For the purposes of coding we won't be using the actual filepath
filepath = "hostFile.txt"
#Where you want to re-direct to.
redirect = "127.0.0.1"
#An array list of potential sites you wish to block
website_list = ["www.facebook.com", "facebook.com", "www.hotmail.com"]

#This will allow for the script to run continuously.
while True:
    print(dt.now())
    #Check the time
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 8) < dt.now() < dt(dt.now().year,
                                           dt.now().month,
                                           dt.now().day, 22):
        print("Working Hours.....")
        #In this case we pass the test filepath, in reality for a working version you will pass
        #the hostfilepath
        with open(filepath, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "   " + website + "\n")
                    #This line essentially prints to file the layout needed namely the
                    #redirect address (specified above) and the website name then
                    #it goes to the next line.
    else:
        with open(filepath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Not Working Hours.....")

    #This ensures the script would run every 5 secs.
    time.sleep(5)
