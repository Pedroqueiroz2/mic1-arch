
class UlaResult:
    def __init__(self, s: int, vai_um: int, flag_z: int, flag_n: int):
        self.s = s
        self.vai_um = vai_um
        self.flag_z = flag_z
        self.flag_n = flag_n
        
class Ula:
    def __init__(self, ir: str, a: int, b: int):
        self.sll8 = int(ir[0])
        self.sra1 = int(ir[1])
        
        if self.sll8 == 1 and self.sra1 == 1:
            raise ValueError("Instrução inválida: sll8 e sra1 não podem ser ambos 1.")
        
        self.f0 = int(ir[2])
        self.f1 = int(ir[3])
        self.ena = int(ir[4])
        self.enb = int(ir[5])
        self.inva = int(ir[6])
        self.inc = int(ir[7])
        
        self.a = a
        self.b = b
        
        self.zerar()
        
        if(self.inva == 1):
            self.a = self.inverter(self.a)
        
    def executarUla(self) -> UlaResult:
        if self.f0 == 0 and self.f1 == 0:
            s_parcial = self.AND()
        
        elif self.f0 == 0 and self.f1 == 1:
            s_parcial = self.OR()
        
        elif self.f0 == 1 and self.f1 == 0:
            s_parcial = self.inverter(self.b)
        
        elif self.f0 == 1 and self.f1 == 1:
            s_parcial, vai_um_parcial = self.soma()
        
        if self.sll8:
            s_final = self.deslocamento_logico_esquerda(s_parcial)
        elif self.sra1:
            s_final = self.deslocamento_aritmetico_direita(s_parcial)

        z = 1 if s_final == 0 else 0
        n = 1 if (s_final & 0x80000000) else 0
        
        return UlaResult(s_final, vai_um_parcial if self.f0 == 1 and self.f1 == 1 else 0, z, n)

    def zerar(self):
        if self.ena == 0:
            self.a = 0
        if self.enb == 0:
            self.b = 0
            
    def inverter(self, x: int) -> int:
        return (~x) & 0xFFFFFFFF
            
    def AND(self):
        return self.a & self.b
    
    def OR(self):
        return self.a | self.b
    
    def soma(self):
        vai_um = 0
        s = self.a + self.b + self.inc
        
        if s > 0xFFFFFFFF:
            vai_um = 1
            s = s & 0xFFFFFFFF
        return s, vai_um
        
    def deslocamento_logico_esquerda(self, s):
        return (s << 8) & 0xFFFFFFFF
    
    def deslocamento_aritmetico_direita(self, s):
        resultado = (s >> 1) & 0xFFFFFFFF
        
        if s & 0x80000000:
            resultado |= 0x80000000
        
        return resultado & 0xFFFFFFFF
    