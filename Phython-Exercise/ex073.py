colocacao = ('Palmeiras','Bragantino','Atlético-MG','Fortaleza','Athletico-PR','Bahia','Fluminense','Flamengo','Santos','Atlético-GO','Ceará','Corinthians','Juventude','São Paulo','Internacional','América-MG','Sport','Cuiabá','Chapecoense','Grêmio')
print(f'Lista de times do Brasileirão: {colocacao}')
print('-='*50)
print(f'Os 5 primeiros são: {colocacao[:5]}')
print('-='*50)
print(f'Os 4 últimos são: {colocacao[-4:]}')
print('-='*50)
print(f'Times em ordem alfabetica: {sorted(colocacao)}')
print('-='*50)
print(f'O chapecoense está na {colocacao.index("Chapecoense")+1}ª posição')
print('-='*50)
