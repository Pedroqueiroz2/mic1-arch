class Ula:
    def compute(self, a, b, signals):
        a_uns = a & 0xFFFFFFFF
        b_uns = b & 0xFFFFFFFF
        
        amux = a_uns if signals['ena'] == 1 else 0
        bmux = b_uns if signals['enb'] == 1 else 0
        
        if signals['inva'] == 1:
            amux = (~amux) & 0xFFFFFFFF
            
        f0 = signals['f0']
        f1 = signals['f1']
        
        if f0 == 0 and f1 == 0:
            s = amux & bmux
        elif f0 == 0 and f1 == 1:
            s = amux | bmux
        elif f0 == 1 and f1 == 0:
            s = (~bmux) & 0xFFFFFFFF
        else:
            s = (amux + bmux) & 0xFFFFFFFF

        if signals['inc'] == 1:
            s = (s + 1) & 0xFFFFFFFF

        sd = s
        if signals['sll8'] == 1:
            sd = (s << 8) & 0xFFFFFFFF
        elif signals['sra1'] == 1:
            if s & 0x80000000:
                sd = (s >> 1) | 0x80000000
            else:
                sd = s >> 1
                
        return sd