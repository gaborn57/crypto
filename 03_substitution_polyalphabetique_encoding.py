#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-
import sys

print("Polyalphabetic substitution cypher")
# asking for a key
key=input("  Specify (string, private) key: ")

# controlling key validity
if len(key)<1:
  sys.stderr.write("  ERROR key should not be empty\n")
  sys.exit(1)

# generating a salt based on the given key
salt=[]
for i in key:
  ascii=ord(i)
  if ascii >= 97 and ascii <= 122:
    delta=97
  elif ascii >=65 and ascii <= 90:
    delta=65
  salt.append(str(ord(i)-delta+1))

# asking for the message to encrypt, using our key (salt)
given=input("  Enter the text to encrypt: ")
if len(given)<1:
  sys.stderr.write("  ERROR nothing given\n")
  sys.exit(2)

# encoding each text character
j=0
for i in given:
  ascii=ord(i)
  if ascii >= 97 and ascii <= 122:
    delta = 97
  elif ascii >=65 and ascii <= 90:
    delta = 65
  else:
    sys.stdout.write(i)
    continue
  sys.stdout.write(chr((ascii-delta+1+int(salt[j]))%26+delta))
  j+=1
  if j==len(salt):
    j=0
