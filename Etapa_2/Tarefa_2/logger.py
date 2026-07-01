import os

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def log_task2_cycle_header(self, cycle, ir_bits, b_bus, c_bus):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"Cycle {cycle}\n")
            f.write(f"ir = {ir_bits[0:8]} {ir_bits[8:17]} {ir_bits[17:21]}\n\n")
            f.write(f"b_bus = {b_bus}\n")
            f.write(f"c_bus = {', '.join(c_bus) if c_bus else 'none'}\n\n")

    def log_task2_state(self, message, regs):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"> {message}\n")
            reg_names = ['mar', 'mdr', 'pc', 'mbr', 'sp', 'lv', 'cpp', 'tos', 'opc', 'h']
            for name in reg_names:
                val = getattr(regs, name)
                if name == 'mbr':
                    f.write(f"mbr = {val & 0xFF:08b}\n")
                else:
                    f.write(f"{name} = {val & 0xFFFFFFFF:032b}\n")

    def log_eop_task2(self, cycle):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write("=====================================================\n")
            f.write(f"Cycle {cycle}\n")
            f.write("No more lines, EOP.")