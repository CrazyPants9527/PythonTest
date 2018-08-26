from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
input = open(from_file,encoding='UTF-8')
indata = input.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
input("Ready, hit RETURN to continue, CTRL-C to abort.")

output = open(to_file,'w',encoding='UTF-8')
output.write(indata)

print("Alright, all done.")

output.close()
input.close()