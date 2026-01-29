class Instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject):
        print(f'im {self.name} upskilling {subject} from {self.address}')
instructor_1=Instructor('pandu','cvl')
# print(f'im {self.name} from {self.address}')
# print(instructor_1.name)
instructor_1.display('python')