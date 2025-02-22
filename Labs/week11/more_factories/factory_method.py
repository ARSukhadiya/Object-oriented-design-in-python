from abc import ABC, abstractmethod, abstractproperty
import xml.etree.ElementTree as etree
import json

class Student:
    def __init__(self, firstName, lastName, age, gpa, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gpa = gpa
        self.gender = gender
        
    def display(self):
        print('firstName:', self.firstName, end="; ")
        print('lastName:', self.lastName, end="; ")
        print('age:', self.age, end="; ")
        print('gpa:', self.gpa, end="; ")
        print('gender:', self.gender)
        
class Parser(ABC):
    @abstractmethod
    def getStudents(self):
        pass
        
class JSONParser(Parser):
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)
            
    def getStudents(self):
        list = []
        students = self.data
        for student in students:
            obj = Student(student['firstName'],
                student['lastName'],
                student['age'],
                student['gpa'],
                student['gender']
            )
            list.append(obj)
            
        return list

class XMLParser(Parser):
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    def getStudents(self):
        list = []
        students = self.tree.findall(".//{}".format('student'))
        for student in students:
            obj = Student(student.find('firstName').text,
                student.find('lastName').text,
                int(student.find('age').text),
                float(student.find('gpa').text),
                student.find('gender').text
            )
            list.append(obj)
            
        return list
            
class ParserFactory:
    def createParser(self, filepath):
        parser = None
        if filepath.endswith('json'):
            parser = JSONParser(filepath)
        elif filepath.endswith('xml'):
            parser = XMLParser(filepath)
        else:
            raise ValueError('Cannot create a parser for {}'.format(filepath))
        return parser
    
def main():
    factory = ParserFactory()
    try:
        filepath = input("Enter the file name: ")
        parser = factory.createParser(filepath)
        for student in parser.getStudents():
            student.display()
    except ValueError as ve:
        print(ve)
        
if __name__ == '__main__':
    main()