
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
        
        if(self.inva == 1):
            self.a = self.inverter(self.a)
        
    def executarUla(self) -> UlaResult:
        if self.f0 == 0 and self.f1 == 0:
            return UlaResult(self.AND(), 0)
        
        elif self.f0 == 0 and self.f1 == 1:
            return UlaResult(self.OR(), 0)
        
        elif self.f0 == 1 and self.f1 == 0:
            return UlaResult(self.inverter(self.b), 0)
        
        elif self.f0 == 1 and self.f1 == 1:
            resultado, vai_um = self.soma()
            return UlaResult(resultado, vai_um)
        
        
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
        resultado = self.a + self.b + self.inc
        
        if resultado > 0xFFFFFFFF:
            vai_um = 1
            resultado = resultado & 0xFFFFFFFF
        return resultado, vai_um