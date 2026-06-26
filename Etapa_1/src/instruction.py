class InstructionRegister:
    def __init__(self):
        self.value = 0

        self.f0 = 0
        self.f1 = 0
        self.ena = 0
        self.enb = 0
        self.inva = 0
        self.inc = 0

    def update(self, value_6bits):
        self.value = value_6bits & 0x3F

        self.f0   = (self.value >> 5) & 1
        self.f1   = (self.value >> 4) & 1
        self.ena  = (self.value >> 3) & 1
        self.enb  = (self.value >> 2) & 1
        self.inva = (self.value >> 1) & 1
        self.inc  =  self.value       & 1

    def get_signals(self):
        return {
            'f0': self.f0,
            'f1': self.f1,
            'ena': self.ena,
            'enb': self.enb,
            'inva': self.inva,
            'inc': self.inc
        }

    def to_binary_string(self):
        return f"{self.value:06b}"
