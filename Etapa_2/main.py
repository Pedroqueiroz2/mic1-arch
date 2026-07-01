import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from ula import Ula
from instruction import InstructionRegister
from loader import load_instructions
from logger import Logger
from registers import Registers

def main():
    prog_path = os.path.join(current_dir, 'data', 'programa_etapa1.txt')
    log_path = os.path.join(current_dir, 'saida', 'saida_simulador.txt')
    
    if not os.path.exists(prog_path):
        prog_path = "programa_etapa1.txt"

    regs = Registers()
    ula = Ula()
    ir = InstructionRegister()
    logger = Logger(log_path=log_path)
    
    regs.pc = 1
    regs.h = -1   
    regs.mbr = 1  
        
    try:
        instructions = load_instructions(prog_path)
    except FileNotFoundError as e:
        print(e)
        return

    for inst_value in instructions:
        ir.update(inst_value)
        signals = ir.get_signals()
        
        a_input = regs.h
        b_input = regs.mbr
        
        sll8_active = 0
        sra1_active = 0
        
        s_out, co, n_flag, z_flag = ula.compute(
            a_input, b_input, signals, sll8=sll8_active, sra1=sra1_active
        )
        
        logger.log_cycle(regs.pc, ir.value, a_input, b_input, s_out, co, n_flag, z_flag)
        
        if regs.pc == 1:
            regs.h = 0
            regs.mbr = 1
        elif regs.pc == 2:
            regs.mbr = 1
        elif regs.pc == 3:
            regs.h = -1
            regs.mbr = 1
            
        regs.pc += 1

    logger.log_eop(regs.pc)
    print(f"Simulação da Etapa 2 concluída com sucesso! Resultados em: {log_path}")

if __name__ == "__main__":
    main()