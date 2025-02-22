from abc import ABC, abstractmethod
from typing import final

class HighTechProgram(ABC):
    @final
    def makeStudyPlan(self):
        self.takeProgramming()
        self.takeCalculus()
        self.takeCoreCourses()
        self.takeNetwork()
        self.takeProfDevel()
        self.takeAdvCourse()
        
    def takeProgramming(self):
        print("Taking C and C++")
        
    def takeCalculus(self):
        print("Taking Calculus I & II")
        
    def takeNetwork(self):
        print("Taking Computer Networks")
        
    def takeProfDevel(self):
        print("Taking Professional Development")
    
    @abstractmethod
    def takeCoreCourses(self):
        pass
        
    @abstractmethod
    def takeAdvCourse(self):
        pass
        
class ComputerScience(HighTechProgram):
    def takeCoreCourses(self):
        self.takeAlogrithm()
        self.takeDatabase()
    
    def takeAdvCourse(self):
        self.takeSoftwareDesign()
    
    def takeAlogrithm(self):
        print("Taking Data Structures and Discrere Math")
        
    def takeDatabase(self):
        print("Taking Database Design")
    
    def takeSoftwareDesign(self):
        print("Taking Software Design") 
        
class ElectricalEngineering(HighTechProgram):
    def takeCoreCourses(self):
        self.takeDigitalLogic()
        self.takeFPGA()
    
    def takeAdvCourse(self):
        self.takeHardwareDesign()
    
    def takeDigitalLogic(self):
        print("Taking Digital Logic and Circuit Design")
        
    def takeFPGA(self):
        print("Taking FPGA Design")
    
    def takeSoftwareDesign(self):
        print("Taking Software Design") 
        
    def takeHardwareDesign(self):
        print("Taking Hardware Design")
        
    def makeStudyPlan(self):
        print("Hello")
        
def main():
    cs = ComputerScience()
    cs.makeStudyPlan();
    print();
    ee = ElectricalEngineering()
    ee.makeStudyPlan()
    
if __name__ == "__main__":
    main()
        