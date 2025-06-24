import pandas as pd

#leer datos
df = pd.read_csv('data/inventario.csv')

#Calcular variacion de stock
df['variacion'] = df['stock_actual'] - df['stock_inicial']

#Producto mas vendido
producto_top = df.sort_values(by='salidas', ascending=False).iloc[0]

#Mostrar resultados
print("📦 Análisis de Inventario")
print(df[['producto', 'stock_inicial', 'entradas', 'salidas', 'stock_actual', 'variacion']])

print("\n🔝 Producto más vendido:")
print(f"{producto_top['producto']} con {producto_top['salidas']} salidas")