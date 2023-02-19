import time
from datetime import datetime as dt
host_path=r"C:\Users\user\web_blocker\hosts"
host="C:\\Windows\\System32\\drivers\\etc\\hosts"
ip_address="192.168.0.20"
website_list=["www.facebook.com","facebook.com","www.chess.com","chess.com","www.youtube.com","youtube.com"]


while True:
    
    if dt(dt.now().year,dt.now().month,dt.now().day,9)< dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,23):
        with open(host, "r+") as myfile:
            content=myfile.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    myfile.write(ip_address+"  "+ website+"\n")
        
        
    else:
        with open(host, "r+") as myfile:
            content=myfile.readlines()
            myfile.seek(0)
            for line in content:
                if not any(website in line for website in website_list ):
                    myfile.write(line)
            myfile.truncate()
    time.sleep(5)
    
        
    

