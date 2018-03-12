# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:53:02 2018

@author: zabiulla.khan

Write a Python Program to print the given string in the format specified in the sample
output.

WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens

Sample Output:
WE, THE PEOPLE OF INDIA,
having solemnly resolved to constitute India into a SOVEREIGN, !
SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
and to secure to all its citizens:
    
"""
#Given string
str1 = '''WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all 
its citizens'''

#Split the string into a list with comma as a separator
list1 = str1.split(', ')

#remove new line char
str1 = list1[2].split('\n')

#add a partition to move the next part to next line
str2 = list1[5].partition('and')

#remove new line char
str3 = str2[2].split('\n')

#format as per the desired output
new_str = list1[0]+','+list1[1]+',\n'+ str1[0]+' '+str1[1]+', !\n'+list1[3]+', '+list1[4]+', '+str2[0]+'\n'+str2[1]+str3[0]+' '+str3[1]

#print the formatted output
print(new_str)
