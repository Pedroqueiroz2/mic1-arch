
'''
A: OPERANDO 1
B: OPERANDO 2
ENA: Enable A. Quando está em 0, qualquer valor em A é ignorado e se torna 0.
ENB: Enable B. Quando está em 0, qualquer valor em B é ignorado e se torna 0.
INVA: Inverte A bit a bit.
INC: Guarda o vai-um. Soma 1 ao resultado final.
F0 e F1: Em conjunto definem a operação a ser realizada.

Conjunto de operações:
    F0 = 0 e F1 = 0  -> indica que a saída é igual a A && B (A and B)
    F0 = 0 e F1 = 1  -> indica que a saída é igual a A | B  (A or B)
    F0 = 1 e F1 = 0  -> indica que a saída é igual ao complemento de B
    F0 = 1 e F1 = 1  -> indica que a saída é igual a soma aritmética

Planejamento da execução do programa
    1- Armazenamento das variáveis iniciais A e B
    2- Abrir o arquivo de leitura, armazenar a linha e a palavra
    3- Armazenamento da combinação de sinais
    4- Processamento das instruções
    5- Escrita dos valores de IR, PC, A, B, S e o Vai-um no log
    6- Próxima linha
'''

class UlaResult:
    def __init__(self, s: int, vai_um: int):
        self.s = s
        self.vai_um = vai_um
        
class Ula:
    def __init__(self, ir: str, a: int, b: int):
        self.f0 = int(ir[0])
        self.f1 = int(ir[1])
        self.ena = int(ir[2])
        self.enb = int(ir[3])
        self.inva = int(ir[4])
        self.inc = int(ir[5])
        self.a = a
        self.b = b
        
        self.zerar()
        self.inversor()
        
    def zerar(self):
        if self.ena == 0:
            self.a = 0
        if self.enb == 0:
            self.b = 0
            
    def inverter(self):
        if self.inva == 1:
            self.a = (~self.a) & 0xFFFFFFFF
            
    