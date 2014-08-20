from datetime import *

def make_date(str):
    return  (datetime.strptime(str.get_text(), '%B %d, %Y')).strftime('%x')

def num(s):
    try:
        return int(s)
    except ValueError:
        return ""
	
def parse_comments(str):
    if (not isinstance(num(str[0]), int)): return 0
    i=0
    while str[i]!=" ": i+=1
    return(num(str[0:i]))  


