import time
import random
import csv
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algoritmos.insertion_sort import insertion_sort
from algoritmos.quick_sort import quick_sort
from tqdm import tqdm

def gerar_vetores(tamanho):
    crescente = list(range(tamanho))
    decrescente = list(range(tamanho, 0, -1))
    aleatorio = random.sample(range(tamanho * 10), tamanho)
    return {
        "crescente": crescente,
        "decrescente": decrescente,
        "aleatorio": aleatorio
    }

def medir_tempo(algoritmo, vetor):
    inicio = time.perf_counter()
    algoritmo(vetor.copy())  # Evita modificar o vetor original
    fim = time.perf_counter()
    return fim - inicio

def salvar_csv(resultados, nome_arquivo):
    with open(nome_arquivo, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Algoritmo", "Tamanho", "Tipo", "Tempo (s)"])
        for linha in resultados:
            writer.writerow(linha)

def main():
    tamanhos = [50, 500, 5000, 50000]
    algoritmos = [
        ("Insertion-Sort", insertion_sort),
        ("Quick-Sort", quick_sort)
    ]
    resultados = []

    total_testes = len(tamanhos) * len(algoritmos) * 3  # 3 tipos de vetor por combinação
    pbar = tqdm(total=total_testes, desc="Executando testes", ncols=100)

    for tamanho in tamanhos:
        vetores = gerar_vetores(tamanho)
        for nome_alg, funcao_alg in algoritmos:
            for tipo, vetor in vetores.items():
                print(f"🔄 {nome_alg} | {tipo} | tamanho={tamanho}... ", end="", flush=True)
                tempo = medir_tempo(funcao_alg, vetor)
                print(f"✅ {tempo:.6f}s")
                resultados.append([nome_alg, tamanho, tipo, tempo])
                pbar.update(1)

    pbar.close()
    salvar_csv(resultados, "resultados/tempos.csv")
    print("\n📈 Resultados salvos em resultados/tempos.csv")
    
if __name__ == "__main__":
    main()
