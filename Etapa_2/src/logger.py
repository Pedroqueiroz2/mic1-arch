import os

class Logger:
    def __init__(self, log_path="saida/saida_simulador.txt"):
        self.log_path = log_path
        folder = os.path.dirname(log_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            
        with open(self.log_path, 'w', encoding='utf-8') as file:
            file.write("Start of Program - Etapa 2\n")
            file.write("=" * 60 + "\n")

    def log_cycle(self, pc, ir_value, a_val, b_val, s_val, co_val, n_val, z_val):
        ir_bin = f"{ir_value:06b}"
        a_bin = f"{a_val & 0xFFFFFFFF:032b}"
        b_bin = f"{b_val & 0xFFFFFFFF:032b}"
        s_bin = f"{s_val & 0xFFFFFFFF:032b}"
        
        block = (
            f"Cycle {pc}\n\n"
            f"PC = {pc}\n"
            f"IR = {ir_bin}\n"
            f"b = {b_bin}\n"
            f"a = {a_bin}\n"
            f"s = {s_bin}\n"
            f"co = {co_val}\n"
            f"n = {n_val}\n"
            f"z = {z_val}\n"
            f"{"=" * 60}\n"
        )
        with open(self.log_path, 'a', encoding='utf-8') as file:
            file.write(block)

    def log_eop(self, pc):
        block = (
            f"Cycle {pc}\n\n"
            f"PC = {pc}\n"
            f"> Line is empty, EOP.\n"
        )
        with open(self.log_path, 'a', encoding='utf-8') as file:
            file.write(block)