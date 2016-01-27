# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
phonebook = {}

n = int(raw_input())

for _ in range(n):
    name = raw_input().strip()
    phonebook[name] = int(raw_input())

for line in sys.stdin:
    search = line.strip()
    if phonebook.has_key(search):
        print search + "="+ str(phonebook[search])
    else: print "Not found"
