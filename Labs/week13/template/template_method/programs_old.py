class ComputerScience:
    def makeStudyPlan(self):
        self.takeProgramming()
        self.takeCalculus()
        self.takeAlogrithm()
        self.takeDatabase()
        self.takeNetwork()
        self.takeProfDevel()
        self.takeSoftwareDesign()
        
    def takeProgramming(self):
        print("Taking C and C++")
        
    def takeCalculus(self):
        print("Taking Calculus I & II")
        
    def takeAlogrithm(self):
        print("Taking Data Structures and Discrere Math")
        
    def takeDatabase(self):
        print("Taking Database Design")
        
    def takeNetwork(self):
        print("Taking Computer Networks")
        
    def takeProfDevel(self):
        print("Taking Professional Development")
        
    def takeSoftwareDesign(self):
        print("Taking Software Design")

class ElectricalEngineering:
    def makeStudyPlan(self):
        self.takeProgramming()
        self.takeCalculus()
        self.takeDigitalLogic()
        self.takeFPGA()
        self.takeNetwork()
        self.takeProfDevel()
        self.takeHardwareDesign()
        
    def takeProgramming(self):
        print("Taking C and C++")
        
    def takeCalculus(self):
        print("Taking Calculus I & II")
        
    def takeDigitalLogic(self):
        print("Taking Digital Logic and Circuit Design")
        
    def takeFPGA(self):
        print("Taking FPGA Design")
        
    def takeNetwork(self):
        print("Taking Computer Networks")
        
    def takeProfDevel(self):
        print("Taking Professional Development")
        
    def takeHardwareDesign(self):
        print("Taking Hardware Design")
        
def main():
    cs = ComputerScience()
    cs.makeStudyPlan();
    print();
    ee = ElectricalEngineering()
    ee.makeStudyPlan()
    
if __name__ == "__main__":
    main()
    