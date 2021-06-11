#!/usr/bin/env python
# coding: utf-8


#Suggestion of strong Password
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
sg_letters= int(input("How many letters would you like in your password?\n")) 
sg_symbols = int(input(f"How many symbols would you like?\n"))
sg_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for char in range(1, sg_letters+1):
  password+=random.choice(letters)
for char in range(1, sg_symbols+1):
  password+=random.choice(symbols)
for char in range(1, sg_numbers+1):
  password+=random.choice(numbers)

random.shuffle(password)
pass1=""
for char in password:
  pass1+= char

print("Your suggestion is : ", pass1)

