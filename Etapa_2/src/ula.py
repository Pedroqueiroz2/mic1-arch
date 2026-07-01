class Ula:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.s = 0
        self.co = 0
        self.n = 0
        self.z = 0

    def compute(self, a_val, b_val, signals, sll8=0, sra1=0):
      
        a_in = a_val & 0xFFFFFFFF
        b_in = b_val & 0xFFFFFFFF

        a_line = a_in if signals['ena'] else 0
        b_line = b_in if signals['enb'] else 0

        if signals['inva']:
            a_line = (~a_line) & 0xFFFFFFFF

        f_type = (signals['f0'] << 1) | signals['f1']
        
        carry_out = 0
        if f_type == 0:    
            result = a_line & b_line
        elif f_type == 1:  
            result = a_line | b_line
        elif f_type == 2: 
            result = (~b_line) & 0xFFFFFFFF
        else:             
            inc = signals['inc']
            sum_res = a_line + b_line + inc
            result = sum_res & 0xFFFFFFFF
            if sum_res > 0xFFFFFFFF:
                carry_out = 1

        if sll8:
            result = (result << 8) & 0xFFFFFFFF
        elif sra1:
            sign_bit = result & 0x80000000
            result = result >> 1
            if sign_bit:
                result |= 0x80000000

        self.s = result & 0xFFFFFFFF
        self.co = carry_out
        
        self.n = 1 if (self.s & 0x80000000) else 0
        self.z = 1 if (self.s == 0) else 0

        return self.s, self.co, self.n, self.z