import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from src.ula import Ula
from src.instruction import InstructionRegister
from src.loader import load_instructions
from src.logger import Logger


def main():
    A = 1  # -1 em 32 bits
    B = 0x80000000

    base_dir = os.path.dirname(os.path.abspath(__file__))
    prog_path = os.path.join(base_dir, 'data', 'programa_etapa2_tarefa1.txt')
    log_path  = os.path.join(base_dir, 'saida', 'saida_simulador.txt')

    print(f"Carregando instruções de: {prog_path}")
    instructions = load_instructions(prog_path)

    logger = Logger(log_path, B, A)
    ir = InstructionRegister()
    pc = 1

    for inst_value in instructions:
        ir.update(inst_value)

        try:
            ula = Ula(ir.to_binary_string(), A, B)
            resultado = ula.executarUla()

            logger.log_cycle(pc, ir.value, ula.a, ula.b, resultado.s, resultado.sd, resultado.flag_z, resultado.flag_n, resultado.vai_um)
        except ValueError as e:
            logger.log_error(pc, ir.value)
        
        pc += 1

    logger.log_eop(pc)
    print(f"Simulação concluída. Log gerado em: {log_path}")


if __name__ == '__main__':
    main()