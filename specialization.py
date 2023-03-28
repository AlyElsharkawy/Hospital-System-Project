class patient:
    def getStatus():
        pass


class specialization:
    def __init__(self, spec_num):
        self.normal = list()
        self.urgent = list()
        self.super_urgent = list()
        self.spec_num = spec_num

    def add_patent(self, patient):
        if len(self.normal)+len(self.urgent)+len(self.super_urgent) < 10:
            if self.getStatus == 0:
                self.normal.append(patient)
            elif self.getStatus == 1:
                self.urgent.append(patient)
            elif self.getStatus == 2:
                self.super_urgent.append(patient)
        else:
            print("the patient can not be added!")
