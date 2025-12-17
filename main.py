import pandas as pd
import os

def carregar_dataset():
    
    arquivo = 'dataset/HomeC.csv'
    
    if not os.path.exists(arquivo):
        print(f"❌ Erro: Arquivo '{arquivo}' não encontrado")
        return None
    
    if os.path.getsize(arquivo) == 0:
        print("❌ Erro: Arquivo está vazio")
        return None
    
    try:
        df = pd.read_csv(arquivo, sep=';')
        print(f"✅ Dataset carregado com sep=';'")
        
    except:
        try:
            df = pd.read_csv(arquivo, sep=',')
            print(f"✅ Dataset carregado com sep=','")
            
        except:
            try:
                df = pd.read_csv(arquivo)
                print(f"✅ Dataset carregado (separador automático)")
                
            except Exception as e:
                print(f"❌ Erro ao carregar dataset: {e}")
                return None
    
    if df.empty:
        print("❌ Erro: Dataset carregado mas está vazio")
        return None
    
    print(f"📊 {len(df)} linhas × {len(df.columns)} colunas")
    return df


if __name__ == "__main__":
    dados = carregar_dataset()
    
    if dados is not None:
        print("\n🎯 Dataset pronto para análise!")
        print(dados.head())