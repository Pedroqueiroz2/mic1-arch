import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from ula import Ula
    from instruction import InstructionRegister
    from logger import Logger
    from loader import Registers 
except ImportError as e:
    print(f"[Erro] Falta de arquivos: {e}")
    sys.exit(1)

def main():
    log_path = os.path.join(current_dir, 'saída_etapa2_tarefa2.txt')
    prog_path = os.path.join(current_dir, 'programa_etapa2_tarefa2.txt')
    reg_path = os.path.join(current_dir, 'registradores_etapa2_tarefa2.txt')
    
    if not os.path.exists(prog_path) or not os.path.exists(reg_path):
        print("[Erro] Certifique-se de que os arquivos de texto estao na mesma pasta.")
        sys.exit(1)

    ula = Ula()
    ir = InstructionRegister()
    regs = Registers()
    
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

    for idx, line in enumerate(lines, start=1):
        ir.update(line)
        signals = ir.get_signals()
        
        logger.log_task2_cycle_header(idx, line, signals['b_bus'], signals['c_bus'])
        logger.log_task2_state("Registers before instruction", regs)
        
        b_val = 0
        if signals['b_bus'] != 'none':
            if signals['b_bus'] == 'mbru':  
                raw_mbr = regs.mbr & 0xFF
                b_val = (raw_mbr - 256) if (raw_mbr & 0x80) else raw_mbr
            elif signals['b_bus'] == 'mbr':
                b_val = regs.mbr & 0xFF
            else:
                val = getattr(regs, signals['b_bus'])
                b_val = (val - 0x100000000) if (val & 0x80000000) else val
        
        a_val = regs.h
        if a_val & 0x80000000:
            a_val -= 0x100000000
            
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
                
    logger.log_eop_task2(len(lines))

if __name__ == "__main__":
    main()