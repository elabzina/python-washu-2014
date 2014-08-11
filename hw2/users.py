import datetime

file = open("newfile.txt", "a")

str = "%s hello world in the new file\n" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
file.write(str)

file.write("and another line\n")

file.close()