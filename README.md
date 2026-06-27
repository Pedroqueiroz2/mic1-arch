# Simulador MIC-1 — Etapa 1 (APS)

Este repositório contém a implementação da **primeira etapa (APS)** do simulador da arquitetura **MIC-1**. Esta etapa consiste em um simulador capaz de ler, decodificar e executar uma sequência de instruções de 6 bits voltadas para a Unidade Lógica e Aritmética (ULA) do MIC-1.

---

## Requisitos do Projeto (Etapa 1)

1. **Leitura de Instruções**: O código deve carregar e processar uma sequência de instruções a partir de um arquivo de texto (`.txt`), onde cada linha representa uma palavra de 6 bits (instrução).
2. **Registradores Principais**:
   - **IR (Instruction Register)**: Armazena temporariamente a instrução de 6 bits em execução.
   - **PC (Program Counter)**: Atua como contador de programa, rastreando a linha/ciclo atual que está sendo executado.
3. **Valores Iniciais das Entradas (ULA)**:
   - Operando $A$: Inicializado com `0xFFFFFFFF` (representando $-1$ em complemento de dois de 32 bits).
   - Operando $B$: Inicializado com `1`.
4. **Geração de Logs**: A cada linha executada, o simulador deve registrar os valores de:
   - Contador de Programa (`PC`)
   - Registrador de Instruções (`IR` em binário de 6 bits)
   - Operando $B$ (`b` em binário de 32 bits)
   - Operando $A$ (`a` em binário de 32 bits, processado conforme os sinais de controle)
   - Saída da ULA (`s` em binário de 32 bits)
   - Vai-um de Saída (`co` - Carry Out)

---

## Funcionamento e Sinais de Controle da ULA

A instrução de 6 bits armazenada no registrador `IR` é dividida da seguinte forma (do bit mais significativo ao menos significativo):

| Bit | Sinal | Descrição |
| :---: | :---: | :--- |
| **5** | `F0` | Seletor de função (combina com `F1`) |
| **4** | `F1` | Seletor de função (combina com `F0`) |
| **3** | `ENA` | Habilita entrada A (se `0`, $A$ é tratado como `0`) |
| **2** | `ENB` | Habilita entrada B (se `0`, $B$ é tratado como `0`) |
| **1** | `INVA` | Inverte a entrada A bit a bit (se `1`, aplica o operador NOT a $A$) |
| **0** | `INC` | Carry In (se `1`, soma 1 ao resultado aritmético da ULA) |

### Tabela de Funções (`F0` e `F1`):
* `F0 = 0`, `F1 = 0` $\rightarrow$ Operação AND lógica ($A \text{ AND } B$)
* `F0 = 0`, `F1 = 1` $\rightarrow$ Operação OR lógica ($A \text{ OR } B$)
* `F0 = 1`, `F1 = 0` $\rightarrow$ Inversão lógica de B ($\text{NOT } B$)
* `F0 = 1`, `F1 = 1` $\rightarrow$ Soma aritmética ($A + B + \text{INC}$)

---

## Estrutura de Diretórios

A estrutura de arquivos do projeto para esta etapa está organizada da seguinte maneira:

```text
mic1-arch/
├── README.md                 # Este arquivo de documentação
└── Etapa_1/
    ├── main.py               # Ponto de entrada e fluxo principal do simulador
    ├── src/                  # Módulos de suporte ao simulador
    │   ├── instruction.py    # Controle e decodificação do Instruction Register (IR)
    │   ├── loader.py         # Leitura e validação do arquivo de programa
    │   ├── logger.py         # Geração do log formatado do ciclo de execução
    │   └── ula.py            # Implementação das operações lógicas/aritméticas da ULA
    ├── data/                 # Arquivos de dados e gabarito
    │   ├── programa_etapa1.txt # Instruções de teste de 6 bits
    │   └── saida_etapa1.txt   # Exemplo/gabarito de log contendo as saídas esperadas
    └── saida/                # Diretório onde os arquivos de log são gerados
        └── saida_simulador.txt # Log gerado dinamicamente pela execução atual
```

---

## Como Executar

Para executar o simulador e ver a geração de logs em ação, siga os passos abaixo:

### Pré-requisitos
* Ter o **Python 3** instalado em sua máquina.

### Execução
A partir da raiz do repositório, execute o script principal `main.py` localizado em `Etapa_1`:

```bash
python3 Etapa_1/main.py
```

### Resultados
Após a execução do comando, o console exibirá uma mensagem de conclusão e os logs gerados com a simulação serão gravados em:
* `Etapa_1/saida/saida_simulador.txt`

Você pode comparar o arquivo gerado `saida_simulador.txt` com o gabarito oficial em `Etapa_1/data/saida_etapa1.txt` para validar a corretude das operações simuladas.
