class patient:
    def getStatus():
        pass


class specialization:
    def __init__(self, spec_num):
        self.normnl_queue = list()
        self.urgent_queue = list()
        self.super_urgent_queue = list()
        self.spec_num = spec_num
        self.normal_queue_head = 0
        self.urgent_queue_head = 0
        self.super_urgent_head = 0

    def add_patent(self, patient):
        if len(self.normal)+len(self.urgent_queue)+len(self.super_urgent_queue) < 10:
            if self.getStatus == 0:
                self.normal.append(patient)
                self.normal_queue_head += 1
            elif self.getStatus == 1:
                self.urgent_queue.append(patient)
                self.urgent_queue_head += 1
            elif self.getStatus == 2:
                self.super_urgent_queue.append(patient)
                self.super_urgent_head += 1
        else:
            print("the patient can not be added!")

    def remove_patient(self):
        if patient in self.normal_queue:
            self.normal_queue[self.normal_queue_head].pop()
            self.normal_queue_head += 1
        elif patient in self.urgent_queue:
            self.urgent_queue[self.normal_queue_head].pop()
            self.normal_queue_head += 1
        elif patient in self.super_urgent_queue:
            self.super_urgent_queue[self.super_urgent_head].pop()
            self.super_urgent_head += 1
