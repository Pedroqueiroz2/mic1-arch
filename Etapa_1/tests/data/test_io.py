import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(parent_dir)

from loader import load_instructions
from instruction import InstructionRegister
from logger import Logger

def run_test():
    logger = Logger(log_path="saida/saida_simulador.txt")
    ir = InstructionRegister()
    
    test_prog = "program_test.txt"
    with open(test_prog, "w", encoding='utf-8') as f:
        f.write("111110\n110101\n110100\n011100\n")

    print("Carregando instruções do programa de teste...")
    instructions = load_instructions(test_prog)
    
    pc = 1
    a = -1  
    b = 1   
    s = 0
    co = 1

    for inst_value in instructions:
        ir.update(inst_value)
        logger.log_cycle(pc, ir.value, a, b, s, co)
        
        if pc == 1:
            a = 0; b = 1; s = 2; co = 0
        elif pc == 2:
            s = 1
        elif pc == 3:
            a = -1; s = -1
            
        pc += 1
        
    logger.log_eop(pc)
    print("Teste concluído com sucesso! Resultado gerado em: 'saida/saida_simulador.txt'.")

    if os.path.exists(test_prog):
        os.remove(test_prog)

if __name__ == "__main__":
    run_test()