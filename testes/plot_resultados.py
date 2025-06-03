import pandas as pd
import matplotlib.pyplot as plt
import os

def plotar(resultados_csv):
    df = pd.read_csv(resultados_csv)

    tipos = df["Tipo"].unique()
    algoritmos = df["Algoritmo"].unique()

    os.makedirs("resultados/graficos", exist_ok=True)

    for tipo in tipos:
        df_tipo = df[df["Tipo"] == tipo]
        plt.figure(figsize=(8, 6))

        for alg in algoritmos:
            df_alg = df_tipo[df_tipo["Algoritmo"] == alg]
            plt.plot(df_alg["Tamanho"], df_alg["Tempo (s)"], label=alg, marker='o')

        plt.title(f"Tempo de Execução - Vetor {tipo.capitalize()}")
        plt.xlabel("Tamanho do Vetor")
        plt.ylabel("Tempo (s)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"resultados/graficos/{tipo}.png")
        plt.close()

if __name__ == "__main__":
    plotar("resultados/tempos.csv")
