import os

def load_instructions(file_path):
 
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo de programa '{file_path}' não foi encontrado.")
        
    instructions = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.strip()
            
            if not clean_line or clean_line.startswith("#"):
                continue
                
            if len(clean_line) != 6 or not all(bit in '01' for bit in clean_line):
                print(f"Aviso: Linha inválida ignorada: '{clean_line}'. Deve ser um binário de 6 bits.")
                continue
            
            instruction_int = int(clean_line, 2)
            instructions.append(instruction_int)
            
    return instructions