import os
import shutil


def epicpass():
    name = input("name:")
    email = input("email:")
    password = input("password:")
    extra = input("extra:")
    f = open("logins.txt", "a")
    f.write("\n")
    f.write("_______________")
    f.write("\n")
    f.write(name)
    f.write("\n")
    f.write(email)
    f.write("\n")
    f.write(password)
    f.write("\n")
    f.write(extra)
    f.write("\n")
    f.write("_______________")
    
    f.close()
    yeet()
    
    
    






def yeet():
    print("____________________________________________________")
    print("|          you are now loading password remember    |")
    print("|                                                   |")
    print("|    ________                                       |")
    print("|   |   ok   |                                      |")
    print("|   |________|                                      |")
    print("-----------------------------------------------------")
    menu = input("OK: y to make login or e to remove logins.txt or l to view logins: ")
    if menu == "y":
        print("\n" * 20)
        print("\n" * 20)
        epicpass()
    if menu == "e":
        os.remove("logins.txt")
        yeet()
    if menu == "l":
        f = open("logins.txt", "r+")
        print(f.read())
        f.close()
        yeet()
    else:
        yeet()
    

yeet()
