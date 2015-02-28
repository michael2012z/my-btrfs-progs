import sys
import getopt
import os

def usage():
    print '-h/--help, print help messages'
    print '-f/--file [file name], file to generate'
    print '-s/ --string [string], string to populate'
    print '-n/--number [number], number of repetation'
    print '-r/--remove, remove the file after generating'

def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'hrf:s:n:', ['help', 'remove', 'file=', 'string=', 'number='])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    fn = ''
    s = ''
    n = 0
    r = False
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-f', '--file'):
            fn = a
        elif o in ('-s', '--string'):
            s = a
        elif o in ('-n', '--number'):
            n = int(a)
        elif o in ('-r', '--remove'):
            r = True

    f = open(fn, 'w')
    print fn, "generated"
    for i in range(0, n):
        f.write(s)
    f.close()
    if (r):
        os.remove(fn)
        print fn, "removed"

if __name__ == '__main__':
    main(sys.argv)

