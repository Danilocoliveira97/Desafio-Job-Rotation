SP = 67.836
RJ =36.678
MG =29.229
ES =27.165
Outros = 19.849
def formata(*n):
    return f'{n:.2f}'
soma = SP+RJ+MG+ES+Outros

sp=(67.836/soma)*100
rj=(36.678/soma)*100
mg=(29.229/soma)*100
es=(27.165/soma)*100
outros=(19.849/soma)*100
print(f'o percentual do estado SP  foi de {round(sp)}%')
print(f'o percentual do estado RJ  foi de {round(rj)}%')
print(f'o percentual do estado MG foi de {round(mg)}%')
print(f'o percentual do estado ES foi de {round(es)}%')
print(f'o percentual dos outros estados de foi de {round(outros,2)}%')
