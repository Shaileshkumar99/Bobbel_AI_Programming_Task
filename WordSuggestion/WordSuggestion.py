#!/usr/bin/python3

import csv

def editDistance(str1, str2, m, n):

	if m == 0:
		return n

	if n == 0:
		return m


	if str1[m-1] == str2[n-1]:
		return editDistance(str1, str2, m-1, n-1)


	return 1 + min(editDistance(str1, str2, m, n-1), 
				editDistance(str1, str2, m-1, n),
				editDistance(str1, str2, m-1, n-1) 
				)


# Driver code

if __name__ == '__main__':

    filename = input('Enter a input CSV filename: ')
    word = input('Enter a word: ')
    d = dict()
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        d = dict()
        for row in reader:
            for i in row:
                dist = (editDistance(word, i.strip(), len(word), len(i.strip())))
                if i.strip() not in d:
                    d[i.strip()] = dist
   
        sorted_dict = sorted(d.items(), key=lambda item: item[1])
        print("------ suggested words are: -------")
        for key in sorted_dict[:5]:
            print(key[0])    
                


