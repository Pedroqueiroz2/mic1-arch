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

    def load_from_file(self, file_path):
        import os
        if not os.path.exists(file_path):
            return
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    name, val = line.split('=')
                    name = name.strip().lower()
                    val_str = val.strip()
                    if name == 'mbr':
                        self.mbr = int(val_str, 2)
                    elif hasattr(self, name):
                        setattr(self, name, int(val_str, 2))