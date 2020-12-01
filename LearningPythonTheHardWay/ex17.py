from sys import argv

script, in_file, out_file = argv

print("Opening file {in_file}")
in_data = open(in_file, 'r')
indata = in_data.read()

print("Writing to file {out_file}")
out_data = open(out_file, 'x')

print("Write to out file:")
out_data.write(indata)

in_data.close()
out_data.close()
