import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from src.ula import Ula
from src.instruction import InstructionRegister
from src.loader import load_instructions
from src.logger import Logger


def main():
    A = 0xFFFFFFFF  # -1 em 32 bits
    B = 1

    base_dir = os.path.dirname(os.path.abspath(__file__))
    prog_path = os.path.join(base_dir, 'data', 'programa_etapa1.txt')
    log_path  = os.path.join(base_dir, 'saida', 'saida_simulador.txt')

    print(f"Carregando instruções de: {prog_path}")
    instructions = load_instructions(prog_path)

    logger = Logger(log_path)
    ir = InstructionRegister()
    pc = 1

    for inst_value in instructions:
        ir.update(inst_value)

        ula = Ula(ir.to_binary_string(), A, B)
        resultado = ula.executarUla()

        logger.log_cycle(pc, ir.value, ula.a, ula.b, resultado.s, resultado.vai_um)
        pc += 1

    logger.log_eop(pc)
    print(f"Simulação concluída. Log gerado em: {log_path}")


if __name__ == '__main__':
    main()