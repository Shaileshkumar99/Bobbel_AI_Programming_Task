#!/usr/bin/python3

import csv

def permutations(remaining, s, candidate=""):
 
    if len(remaining) == 0:
        s.add(candidate)
 
    for i in range(len(remaining)):
 
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]
 
        permutations(newRemaining, s, newCandidate)
 


if __name__ == '__main__':

    filename = input('Enter a input CSV filename: ')
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        d = dict()
        for row in reader:
            for i in row:
                s = set()
                permutations(i.strip(), s)
                if i not in d:
                    d[i] = list(s)
            
                print(i, ": ", d[i])
               
 		
  
