import numbers
import datetime

def globalValidate(x):
	if (not isinstance(x, numbers.Number)): 
		print "Wrong format. The input is not a number."
		return False
		
	if x<=0: 
		print "The input must be possitive."
		return False
	return True

def writeLog(text):
        file = open("log.txt","a")
        file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +"  " + text + '\n')
        file.close()

def activeLog(flag):
        w= "w"
        s=""
        if flag: w="a"
        file = open("log.txt", w)
        if flag: file.write('\n \n')
        file.close()

def outLog():
        file = open("log.txt","r")
        print file.read()
        file.close()
        
