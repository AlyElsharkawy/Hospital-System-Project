import logging
import time
import queue
timeInstance = time.localtime()
current_time = time.strftime("%d-%m-%Y", timeInstance)
logging.basicConfig(filename=f" {current_time} Patient Flow.txt", filemode="w", level=logging.INFO, format= "%(message)s")

def appendLog(inputMessage):
    logging.info(inputMessage)

def showMenu():
    print("Main Menu Options: ")
    print(" 1) Add new patient: ")
    print(" 2) Print all patients: ")
    print(" 3) Get next patient: ")
    print(" 4) Remove a leaving patient: ")
    print(" 5) End the program")

def numToStatus(num):
    if num == 0:
        return "Normal"
    elif num == 1:
        return "Urgent"
    elif num == 2:
        return "Super-Urgent"

class Patient:
    # 0 is normal
    # 1 is urgent
    # 2 is super urgent
    def __init__(self, name, status, intendedSpecialization):
        self.name = name
        self.status = status
        self.specialization = intendedSpecialization
    
    def getName(self):
        return self.name
    
    def getStatus(self):
        return self.status
    
    def getSpecialization(self):
        return self.specialization
    
    def __str__(self):
        return f"Patient: {self.name} is {numToStatus(self.status)}"
    
class Specialization:
    def __init__(self, spec_num):
        self.normal = list()
        self.urgent = list()
        self.super_urgent = list()
        self.spec_num = spec_num
        self.normal_queue_head = 0
        self.urgent_queue_head = 0
        self.super_urgent_head = 0

    def totalPatients(self):
        return len(self.normal) + len(self.urgent) + len(self.super_urgent)

    def addPatient(self, name, specNum, status):
        if self.totalPatients() < 10:
            if status == 0:
                self.normal.append(Patient(name, status, specNum))
            elif status == 1:
                self.urgent.append(Patient(name, status, specNum))
            elif status == 2:
                self.super_urgent.append(Patient(name, status, specNum))
        else:
            print("The patient can not be added. The queue is full.")
        
    def remove_patient(self, status):
        if status == 0:
            self.normal[self.normal_queue_head].pop()
            self.normal_queue_head += 1
        elif status == 1:
            self.urgent[self.normal_queue_head].pop()
            self.normal_queue_head += 1
        elif status == 2:
            self.super_urgent[self.super_urgent_head].pop()
            self.super_urgent_head += 1
    
    def printAllPatients(self):
        if self.totalPatients() > 0:
            print(f"Specialization {self.spec_num}: There are {self.totalPatients()} patients")
            totalList = self.super_urgent + self.urgent + self.normal
            for i in totalList:
                print(i)
            print("")
    
    def getNextPatient(self):
        if len(self.super_urgent) > 0:
            return self.super_urgent.pop(0)
        elif len(self.urgent) > 0:
            return self.super_urgent.pop(0)
        elif len(self.normal) > 0:
            return self.normal.pop(0)
    
    def getSpecNum(self):
        return self.spec_num

currentSpecs = []
for i in range(1,21):
    currentSpecs.append(Specialization(i))

def addDummyData():
    for spec in currentSpecs:
        for num in range(2):
            spec.addPatient(f"Dummy {num + 1}", spec.getSpecNum(), 0)
            spec.addPatient(f"Dummy {num + 2}", spec.getSpecNum(), 1)
            spec.addPatient(f"Dummy {num + 3}", spec.getSpecNum(), 2)

#Main program execution starts here
addDummyData()
while True:
    while True:
        showMenu()
        userInput = input("Please enter action: ")
        try:
            userInput = int(userInput)
            break
        except:
            print("Error. Please enter a number from one to five.")
            continue

    if userInput > 5 or userInput < 1:
        print("Number out of bounds. Please enter a valid number.\n")
        continue

    if userInput == 1:
        patientName = input("Please enter patient name: ")
        desiredSpecialization = int(input("Please enter desired specialization (1-20): "))
        patientStatus = int(input("Please enter patient status (0-normal | 1-urgent | 2-super urgent): "))
        currentSpecs[desiredSpecialization - 1].addPatient(patientName, desiredSpecialization, patientStatus)
        logging.info(f"Succesfully added {patientName} to specialization number {desiredSpecialization} with a status of {patientStatus}")
        print("")
    
    elif userInput == 2:
        for spec in currentSpecs:
            spec.printAllPatients()
        pass

    elif userInput == 3:
        desiredSpecialization = int(input("Please enter desired specialization: "))
        currentPatient = currentSpecs[desiredSpecialization - 1].getNextPatient()
        print(f"{currentPatient.getName()}, please go to the Dr.")
        pass

    elif userInput == 4:
        #remove a leaving patient
        pass

    elif userInput == 5:
        #end the program
        print("Closing program...")
        quit()
