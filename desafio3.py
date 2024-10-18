# Considerando o vetor já carregado com os dados de faturamento diário
faturamento_diario = [1000, 2000, 0, 3000, 2500, 0, 1500, 0]

# Filtrando os dias com faturamento maior que 0
faturamento_validos = [
    f for f in faturamento_diario if f > 0
]  # Utilizando comprehension para maior agilidade

# Menor valor de faturamento
menor_faturamento = min(faturamento_validos)

# Maior valor de faturamento
maior_faturamento = max(faturamento_validos)

# Calculando a média anual
media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

# Número de dias com faturamento acima da média
dias_acima_da_media = len(
    [f for f in faturamento_validos if f > media_faturamento]
)  # Utilizando comprehension para maior agilidade

# Exibindo os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Média de faturamento: {media_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
