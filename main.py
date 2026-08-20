import os 
from student import Student 
from storage import load_data,save_data 

def menu(): 
    while True:
        user_input=input('''
                1. Press 1 to save data 
                2.Press 2 to display data 
                3. Press 3 to exit ''') 
        if user_input=="1":
            name=input("Enter Student Name:")
            roll=input("Enter Student roll:")  
            branch=input("Enter Student Branch:") 
            s=Student(name,roll,branch) 
            save_data(s) 
        elif user_input=="2": 
            load_data() 
        else: 
            break  

menu()
        
