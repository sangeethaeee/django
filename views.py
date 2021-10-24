from django.shortcuts import render
from django import csv

# Create your views here.
f=open('csvexample.csv','rt')
myReader=cv.reader(f)
number_of_lines=20
for i in myReader(number_of_lines):
    line=a_file.readline()
    print(line)
    