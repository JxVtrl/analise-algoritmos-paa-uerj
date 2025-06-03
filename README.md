# 📊 Análise Experimental de Algoritmos de Ordenação

Projeto de análise comparativa entre os algoritmos **Insertion-Sort** e **Quick-Sort**, implementados em Python, com medição de desempenho para diferentes tamanhos e tipos de vetores.

---

## 🧑‍🎓 Informações

- **Aluno**: João Vinícius Vitral  
- **Matrícula**: 202010358111  
- **Disciplina**: Projeto e Análise de Algoritmos  
- **Universidade**: UERJ  
- **Entrega**: 13/06/2025

---

## 🧠 Objetivo

Implementar e comparar o desempenho dos algoritmos de ordenação `Insertion-Sort` e `Quick-Sort`, medindo o tempo de execução para vetores com:

- Tamanhos: `50`, `500`, `5000`, `50000`
- Tipos: **Crescente**, **Decrescente** e **Aleatório**

A análise experimental envolve geração de dados, execução controlada dos algoritmos e visualização por meio de gráficos.

---

## 🛠️ Estrutura do Projeto

```bash
analise-algoritmos/
├── algoritmos/               # Implementações dos algoritmos
│   ├── insertion_sort.py
│   ├── quick_sort.py
│   └── __init__.py
├── testes/                   # Scripts de teste e visualização
│   ├── teste_ordenacao.py
│   ├── plot_resultados.py
│   └── __init__.py
├── resultados/               # CSV e gráficos gerados
│   ├── tempos.csv
│   └── graficos/
├── leiametxt/                # Instruções básicas
│   └── leia_me.txt
├── relatorio/                # Relatório em PDF ou DOCX
│   └── Relatorio_Analise_Algoritmos_JoaoVitral.docx
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

---

## 💻 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/analise-algoritmos.git
    cd analise-algoritmos
   ```

2. **Crie um ambiente virtual (recomendado)**:
   ```bash
    python3 -m venv venv
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os testes**:
   ```bash
   python testes/teste_ordenacao.py
   ```

5. **Visualize os resultados**:
   ```bash
   python testes/plot_resultados.py
   ```

---

## 📌 Observações

- Não foram utilizadas funções prontas de ordenação (sorted, sort).

- Cada vetor é clonado antes da ordenação para manter a imparcialidade nos testes.

- Os tempos são medidos com precisão usando time.perf_counter().

- Os gráficos são gerados com Matplotlib e salvos na pasta `resultados/graficos/`.
