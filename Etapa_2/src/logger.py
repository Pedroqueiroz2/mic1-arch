import os

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

   
    def log_cycle_task1(self, cycle, ir_bits, a, b, s, sd, n, z, co):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"Cycle {cycle}\n\n")
            f.write(f"PC = {cycle}\n")
            f.write(f"IR = {ir_bits}\n")
            f.write(f"b = {b & 0xFFFFFFFF:032b}\n")
            f.write(f"a = {a & 0xFFFFFFFF:032b}\n")
            f.write(f"s = {s & 0xFFFFFFFF:032b}\n")
            f.write(f"sd = {sd & 0xFFFFFFFF:032b}\n")
            f.write(f"n = {n}\n")
            f.write(f"z = {z}\n")
            f.write(f"co = {co}\n")
            f.write("============================================================\n")

    def log_error_task1(self, cycle, ir_bits):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"Cycle {cycle}\n\n")
            f.write(f"PC = {cycle}\n")
            f.write(f"IR = {ir_bits}\n")
            f.write("> Error, invalid control signals.\n")
            f.write("============================================================\n")

    def log_eop_task1(self, cycle):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"Cycle {cycle}\n\n")
            f.write("PC = {cycle}\n")
            f.write("> Line is empty, EOP.\n")

    def log_task2_cycle_header(self, cycle, ir_bits, b_bus, c_bus):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"Cycle {cycle}\n")
            part1 = ir_bits[0:8]
            part2 = ir_bits[8:17]
            part3 = ir_bits[17:21]
            f.write(f"ir = {part1} {part2} {part3}\n\n")
            f.write(f"b_bus = {b_bus}\n")
            c_bus_str = ", ".join(c_bus) if c_bus else "none"
            f.write(f"c_bus = {c_bus_str}\n\n")

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