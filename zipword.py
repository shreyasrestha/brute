import zipfile
import time

folderpath=input("Path to folder")
zipf=zipfile.ZipFile(folderpath)
global result
result=0

global tried
tried=0

c=0

if not zipf:
    print("This zipped file/folder is not password protected. You can successfully open it!!")

else:
    wordlistFile=open("wordlist.txt","r")
    body=wordlistFile.lower()
    words=body.split("\n")
    
for i in range(len(words)):
    word=words[i]
    password=word.encode("utf-8").strip()
    c=c+1
    print("Trying to decode password by: {}".format(word))
    try:
        with zipfile.ZipFile(folderpath,"r") as zf:
            zf.extractcall(pwd="password")
            print("SUCCESS!!! The password is: "+word )
            endtime=time.time()
            result=1
        break
    except:
        pass

if result==0:
    print("Sorry password not found!\nA total of "+str(c)+"possible combinations tried. Password is not of 4 characters! ")
else:
    print("Congratulations!!Password found after trying "+str(c)+" combinations.")  
        
    
