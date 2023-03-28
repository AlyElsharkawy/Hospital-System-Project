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
        return f"{self.name} is a {self.getStatus} who wants to use specialization number {self.specialization}"