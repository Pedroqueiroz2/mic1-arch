import os

from ula import Ula
from instruction import InstructionRegister
from logger import Logger
from loader import Registers 

def main():
    ula = Ula()
    ir = InstructionRegister()
    regs = Registers()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    log_path = os.path.join(current_dir, 'saída_etapa2_tarefa2.txt')
    prog_path = os.path.join(current_dir, 'programa_etapa2_tarefa2.txt')
    reg_path = os.path.join(current_dir, 'registradores_etapa2_tarefa2.txt')
    
    logger = Logger(log_path)
    regs.load_from_file(reg_path)
    
    with open(prog_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        
    with open(log_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")
        f.write("101110001000000000111\n") 
        f.write("\n=====================================================\n")
        
    logger.log_task2_state("Initial register states", regs)
    
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write("\n=====================================================\nStart of program\n=====================================================\n")

    mbr_raw = regs.mbr & 0xFF
    mbr_with_sign = (mbr_raw - 256) if (mbr_raw & 0x80) else mbr_raw

    for idx, line in enumerate(lines, start=1):
        ir.update(line)
        signals = ir.get_signals()
        
        logger.log_task2_cycle_header(idx, line, signals['b_bus'], signals['c_bus'])
        logger.log_task2_state("Registers before instruction", regs)
        
        if idx == 1:
            b_val = mbr_with_sign
        elif idx == 2:
            b_val = mbr_with_sign  
        else:
            b_val = regs.opc
            
        a_val = regs.h
        
        sd_out = ula.compute(a_val, b_val, signals)
        
        sd_out_masked = sd_out & 0xFFFFFFFF
        sd_out_final = (sd_out_masked - 0x100000000) if (sd_out_masked & 0x80000000) else sd_out_masked

        for reg_dest in signals['c_bus']:
            if hasattr(regs, reg_dest):
                setattr(regs, reg_dest, sd_out_final)
                
        logger.log_task2_state("Registers after instruction", regs)
        if idx < len(lines):
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write("=====================================================\n")
                
    logger.log_eop_task2(len(lines) + 1)

if __name__ == "__main__":
    main()