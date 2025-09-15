# employee inheritance
class person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display_person(self):
        print(f"my name is {self.name} , my id is {self.id}")

class employee(person):
    def __init__(self,id,name,post,salary):
        person.__init__(self,id,name)
        self.post = post
        self.salary = salary
    def disp_emp(self):
        person.display_person(self)
        print(f"i am working as a {self.post} and my salary is {self.salary}")
emp1 = employee('1232','joy','supervisor','54000')
emp1.disp_emp()