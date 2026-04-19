import pandas as pd
import os

def analisar_dados():
    print("--- Iniciando Processamento de Dados Governamentais ---\n")
    
    # Nomes dos ficheiros que estão na sua pasta
    file_2023 = 'tabela_2023.xlsx'
    file_pag = '2026_Pagamento.csv'
    
    try:
        # Carregar dados de 2023
        df_2023 = pd.read_excel(file_2023)
        print(f"✔ Ficheiro 2023 carregado: {len(df_2023)} registos.")
        
        # Análise por Cargo (Baseado nos seus dados)
        if 'Cargo' in df_2023.columns:
            print("\n[Insight] Média de gasto por Cargo (Top 5):")
            # Ajuste 'Valor' para o nome exato da coluna de custo na sua planilha
            coluna_valor = 'Despesa Total' if 'Despesa Total' in df_2023.columns else df_2023.select_dtypes(include=['number']).columns[0]
            print(df_2023.groupby('Cargo')[coluna_valor].mean().sort_values(ascending=False).head(5))

        # Carregar Pagamentos 2026
        # sep=None com engine='python' deteta automaticamente se é vírgula ou ponto e vírgula
        df_2026 = pd.read_csv(file_pag, sep=None, engine='python', encoding='utf-8')
        print(f"\n✔ Ficheiro 2026 carregado: {len(df_2026)} registos de pagamentos.")

    except Exception as e:
        print(f"Erro ao processar: {e}")
        print("Dica: Verifique se os nomes das colunas e ficheiros estão corretos.")

if __name__ == "__main__":
    analisar_dados()
