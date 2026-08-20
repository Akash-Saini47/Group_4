class Student: 
    def __init__(self,name,roll,branch): 
        self.name=name 
        self.roll=roll 
        self.branch=branch 

    def display_detail(self): 
        return f"name:{self.name},roll:{self.roll},branch:{self.branch}" 
s1=Student("manna",23,"cs")