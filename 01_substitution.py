#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-
import sys

print("Substitution cypher")
tmp=input("  Specify the shift value (1-25): ")

try:
  int(tmp)
except:
  sys.stderr.write("  ERROR Value should be an integer\n")
  sys.exit(1)

shift=int(tmp)
if (shift < 1 or shift > 25):
  sys.stderr.write("  ERROR Value should be 1-25\n")
  sys.exit(2)

# val is correctly defined
given=input("  Enter the text to encrypt: ")
if len(given)<1:
  sys.stderr.write("  ERROR nothing given\n")
  sys.exit(3)

for i in given:
  #a 97
  #z 122
  #A 65
  #Z 90
  ascii=ord(i)
  #print(i, ord(i))
  if ascii >= 97 and ascii <= 122:
    delta=97
  elif ascii >=65 and ascii <= 90:
    delta=65
  else:
    sys.stdout.write(i)
    continue
  # perform the translation
  ascii-=delta
  ascii+=shift
  ascii=ascii%26
  ascii+=delta
  sys.stdout.write(chr(ascii))
print()
