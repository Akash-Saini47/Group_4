from student import Student  
import pickle 
import os 

data_source="student.pkl" 
def save_data(s): 
    student_data=[] 
    
    if  os.path.exists(data_source): 
        with open(data_source,"rb") as file: 
            student_data=pickle.load(file) 
            student_data.append(s) 
    else:
        student_data.append(s) 
    with open(data_source,"wb") as file: 
        pickle.dump(student_data,file)


#creating load data 
def load_data(): 
    with open(data_source,"rb") as file: 
        data=pickle.load(file) 
    for ele in data: 
        print(ele.display_detail())
