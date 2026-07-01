import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from ula import Ula
from instruction import InstructionRegister
from logger import Logger
from registers import Registers

def main():
    ula = Ula()
    ir = InstructionRegister()

    log_t1_path = os.path.join(current_dir, 'saida', 'saída_etapa2_tarefa1.txt')
    logger_t1 = Logger(log_path=log_t1_path)
    prog_t1_path = os.path.join(current_dir, 'programa_etapa2_tarefa1.txt')
    
    b_input_t1 = 0x80000000
    a_input_t1 = 0x00000001
    
    with open(log_t1_path, 'w', encoding='utf-8') as f:
        f.write(f"b = {b_input_t1:032b}\na = {a_input_t1:032b}\n\nStart of Program\n============================================================\n")
        
    if os.path.exists(prog_t1_path):
        with open(prog_t1_path, 'r', encoding='utf-8') as f:
            lines_t1 = [line.strip() for line in f if line.strip()]

        for idx, line in enumerate(lines_t1, start=1):
            ir.update(line)
            signals = ir.get_signals()
            
            if line == "11111100":
                logger_t1.log_error_task1(idx, line)
            else:
                s_out, sd_out, co, n, z = ula.compute(a_input_t1, b_input_t1, signals)
                logger_t1.log_cycle_task1(idx, line, a_input_t1, b_input_t1, s_out, sd_out, n, z, co)
            
        logger_t1.log_eop_task1(len(lines_t1) + 1)

    
    log_t2_path = os.path.join(current_dir, 'saida', 'saída_etapa2_tarefa2.txt')
    logger_t2 = Logger(log_path=log_t2_path)
    prog_t2_path = os.path.join(current_dir, 'programa_etapa2_tarefa2.txt')
    reg_t2_path = os.path.join(current_dir, 'registradores_etapa2_tarefa2.txt')
    
    regs = Registers()
    regs.load_from_file(reg_t2_path)
    
    with open(prog_t2_path, 'r', encoding='utf-8') as f:
        lines_t2 = [line.strip() for line in f if line.strip()]
        
    with open(log_t2_path, 'w', encoding='utf-8') as f:
        for line in lines_t2:
            f.write(line + "\n")
        f.write("\n=====================================================\n")
        
    logger_t2.log_task2_state("Initial register states", regs)
    with open(log_t2_path, 'a', encoding='utf-8') as f:
        f.write("\n=====================================================\nStart of program\n=====================================================\n")

    for idx, line in enumerate(lines_t2, start=1):
        ir.update(line)
        signals = ir.get_signals()
        
        logger_t2.log_task2_cycle_header(idx, line, signals['b_bus'], signals['c_bus'])
        logger_t2.log_task2_state("Registers before instruction", regs)
        
        b_val = 0
        if signals['b_bus'] != 'none':
            if signals['b_bus'] == 'mbr':
                raw_mbr = regs.mbr & 0xFF
                if raw_mbr & 0x80:
                    b_val = raw_mbr - 256
                else:
                    b_val = raw_mbr
            elif signals['b_bus'] == 'mbru':
                b_val = regs.mbr & 0xFF
            else:
                val = getattr(regs, signals['b_bus'])
                b_val = val - 0x100000000 if (val & 0x80000000) else val
        
        a_val = regs.h
        if a_val & 0x80000000:
            a_val -= 0x100000000
            
        _, sd_out, _, _, _ = ula.compute(a_val, b_val, signals)
        
        sd_out_masked = sd_out & 0xFFFFFFFF
        if sd_out_masked & 0x80000000:
            sd_out_final = sd_out_masked - 0x100000000
        else:
            sd_out_final = sd_out_masked

        for reg_dest in signals['c_bus']:
            if hasattr(regs, reg_dest):
                setattr(regs, reg_dest, sd_out_final)
                
        logger_t2.log_task2_state("Registers after instruction", regs)
        
    logger_t2.log_eop_task2(len(lines_t2) + 1)


if __name__ == "__main__":
    main()