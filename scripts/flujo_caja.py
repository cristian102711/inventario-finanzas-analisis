import pandas as pd

# Cargar datos
df = pd.read_csv('data/movimientos_bancarios.csv')

#Total de ingresos y egresos
total_ingresos = df[df['tipo'] == 'ingreso']['monto'].sum()
total_egresos = df[df['tipo'] == 'egreso']['monto'].sum()

saldo_final = total_ingresos - total_egresos

#resumen
print("💰 Análisis de Flujo de Caja")
print(f"Ingresos totales: ${total_ingresos}")
print(f"Egresos totales:  ${total_egresos}")
print(f"Saldo final:      ${saldo_final}")

# Agrupar por categoría
print("\n📊 Gastos por categoría:")
print(df[df['tipo'] == 'egreso'].groupby('categoria')['monto'].sum())
