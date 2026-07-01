class InstructionRegister:
    def __init__(self):
        self.value = 0
        self.signals = {}

    def update(self, binary_string):
        self.value = int(binary_string, 2)
        length = len(binary_string)
        bits = [int(b) for b in binary_string]
        
        self.signals = {
            'enb':  bits[0],
            'ena':  bits[1],
            'f1':   bits[2],
            'f0':   bits[3],
            'inva': bits[4],
            'inc':  bits[5],
            'sll8': bits[6],
            'sra1': bits[7],
            'c_bus': [],
            'b_bus': 'none',
            'raw_bits': binary_string
        }
        
        if length == 21:
            c_bits = bits[8:17]
            c_regs = ['h', 'opc', 'tos', 'cpp', 'lv', 'sp', 'pc', 'mdr', 'mar']
            self.signals['c_bus'] = [c_regs[i] for i, bit in enumerate(c_bits) if bit == 1]
            
            b_val = int("".join(map(str, bits[17:21])), 2)
            b_map = {
                0: 'mdr', 1: 'pc', 2: 'mbr', 3: 'mbru', 
                4: 'sp', 5: 'lv', 6: 'cpp', 7: 'opc', 8: 'tos'
            }
            self.signals['b_bus'] = b_map.get(b_val, 'none')

    def get_signals(self):
        return self.signals