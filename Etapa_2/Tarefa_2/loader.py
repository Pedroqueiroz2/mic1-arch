# Tarefa_2/loader.py
import os

class Registers:
    def __init__(self):
        self.mar = 0
        self.mdr = 0
        self.pc = 0
        self.mbr = 0
        self.sp = 0
        self.lv = 0
        self.cpp = 0
        self.tos = 0
        self.opc = 0
        self.h = 0

    def load_from_file(self, filepath):
        if not os.path.exists(filepath):
            # REMOVIDO O EMOJI: Texto limpo em ASCII puro para evitar o erro no Windows
            print(f"[Aviso] Arquivo de registradores nao encontrado: {filepath}")
            return

        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or '=' not in line:
                    continue
                name, value_str = line.split('=')
                name = name.strip().lower()
                value_str = value_str.strip()
                try:
                    val = int(value_str, 2)
                    if hasattr(self, name):
                        if name == 'mbr':
                            setattr(self, name, val & 0xFF)
                        else:
                            setattr(self, name, val & 0xFFFFFFFF)
                except ValueError:
                    continue