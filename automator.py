import requests
from sys import argv
from art import tprint

tprint(";-AUTOMATOR-;")

print("              Coded by: Ahmed Tareq\n\n")

if len(argv) == 1 : print("Please provide the required input file_name and dir_name or file name")

elif "help" in argv : print("USAGE: python3 automator.py file_name dir_name")
    
elif len(argv) == 2 : print("Please provide the dir_name or file name")

else :
    with open(argv[1], "r") as f:
        urls = f.read().splitlines()
   
    directory = str(argv[2])
    print(f"looking for {directory} in the provided domains")
    
    for item in urls :
        url = item + directory
        try :
            status = requests.get(url, timeout = 1)
            if status.status_code == 200 :
            	print(url)
            	output = open("output.txt", 'a')
           	    output.write(f"{url}\n")
                output.close()
            else : continue
        except : pass
