# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:05:56 2021

@author: patra
"""






def removeHosts():
    f = open('C:\Windows\System32\drivers\etc\hosts', 'r+')
    f.truncate(0)

def uri_validator(x):
    import re
    regex = re.compile(
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex, x) is not None


def setup():
    print("setting up\n")
    f = open('hosts_temp.txt','a')
    f.truncate(0)
    with open('C:\Windows\System32\drivers\etc\hosts','r') as firstfile, open('hosts_temp.txt','a') as secondfile: 
        for line in firstfile:
            secondfile.write(line)
            
def add():
    name = input("Enter a short name\n")
    while(len(name))>=10:
        name = input("Enter a valid short name\n")
    name = name.lower()
    url = input("Enter the url\n")
    url = url.lower()
    while uri_validator(url)==False:
        url = input("Enter the valid url\n")
        url = url.lower()
    
    req = "#" + name +"\n" + "127.0.0.1 " + url + "\n"
    with open("websites.txt","a") as webfile:
        webfile.write(req)
    
    
    
def show():
    with open("websites.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        x = ""
        for i in d:
            if i[0]=='#':
                for j in i[1:]:
                    if j!="\n":
                        x = x + j
            else:
                x = x + " -------> "
                x = x + i[10:]
                print(x)
                print("\n")
                x = ""
    
    
def remove():
    with open("websites.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        x = input("Enter the name of website you want to remove\n")
        result = "#"+x+"\n"
        print(result)
        nxt=0
        for i in d:
            if nxt==1:
                nxt=0
            elif i == result:
                nxt=1
            elif nxt==0 and i!=result:
                print("yes\n")
                f.write(i)
            f.truncate()
   
    
def block():
    setup()
    removeHosts()
    with open('C:\Windows\System32\drivers\etc\hosts','a') as secondfile, open('hosts_temp.txt','r') as firstfile: 
            for line in firstfile:
                secondfile.write(line)
            secondfile.write("\n")
    with open('C:\Windows\System32\drivers\etc\hosts','a') as secondfile, open('websites.txt','r') as firstfile: 
            for line in firstfile:
                secondfile.write(line)
    
    
def reset():
    removeHosts()
    with open('C:\Windows\System32\drivers\etc\hosts','a') as secondfile, open('hosts_temp.txt','r') as firstfile: 
            for line in firstfile:
                secondfile.write(line)
    
    
def remall():
    f = open('websites.txt', 'r+')
    f.truncate(0)
    
    
def exile():
    reset()
    
    


# Defining main function 
def main(): 
    loopback = True
    while loopback == True:
        print("Hey there, welcome to Website Blocker\n")
        print("1.Add a website\n")
        print("2.Show all blocked websites\n")
        print("3.Remove a website\n")
        print("4.Start blocking\n")
        print("5.Stop blocking\n")
        print("6.Remove all websites\n")
        print("7.Exit")
        x = int(input())
        if x==1:
            add()
        elif x==2:
            show()
        elif x==3:
            remove()
        elif x==4:
            block()
        elif x==5:
            reset()
        elif x==6:
            remall()
        elif x==7:
            exile()
            loopback = False
        else:
            print("Invalid Choice\n")
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 