#from sys import argv;open(argv[2],'x').writelines([l for l in open(argv[1],'r')])
from sys import argv;open(argv[2],'x').write(open(argv[1],'r').read())
