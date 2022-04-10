import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

inp = pd.read_excel('movimentacao-2022-04-09-17-39-48.xlsx')

print(inp)

dic = {}
dic['Data operação']=[]
dic['Categoria']=[]
dic['Código Ativo']=[]
dic['Operação C/V']=[]
dic['Quantidade']=[]
dic['Preço unitário']=[]
dic['Corretora']=[]
dic['Corretagem']=[]
dic['Taxas']=[]
dic['Impostos']=[]
dic['IRRF']=[]

for i in range(len(inp)) :
    
    movimentacao = inp.iloc[i, 2]
    if movimentacao not in ['Transferência - Liquidação', 'Compra', 'Venda'] :
        continue

    data = inp.iloc[i, 1]
    codigo_ativo = (inp.iloc[i, 3].split('-'))[0].strip()
    
    categoria = ''
    if codigo_ativo == 'TAEE11' :
         categoria = 'Ações'
    elif codigo_ativo.startswith('Tesouro') :
        categoria = 'Tesouro Direto'
    elif codigo_ativo.endswith('11') :
        categoria = 'FII''s'
    else :
        categoria = 'Ações'


    entrada_saida = inp.iloc[i, 0]
    operacao = 'C' if  entrada_saida == 'Credito' else 'V'

    quantidade = inp.iloc[i, 5]

    preco_unitario = str(inp.iloc[i, 6]).replace('.', ',')

    corretora = 'NU INVEST CORRETORA DE VALORES'

    

    dic['Data operação'].append(data)
    dic['Categoria'].append(categoria)
    dic['Código Ativo'].append(codigo_ativo)
    dic['Operação C/V'].append(operacao)
    dic['Quantidade'].append(quantidade)
    dic['Preço unitário'].append(preco_unitario)
    dic['Corretora'].append(corretora)
    dic['Corretagem'].append('')
    dic['Taxas'].append('')
    dic['Impostos'].append('')
    dic['IRRF'].append('')
    

out = pd.DataFrame(dic)

print(out)

out.to_excel('saida_terceiro.xlsx')






