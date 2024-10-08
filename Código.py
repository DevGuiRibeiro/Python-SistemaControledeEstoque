alimentos = 50
bebidas = 75
limpeza = 30

nome_do_produto = input('nome do produto: ')
categoria = input('categoria: ')
qtde_estoque = input('quantidade atual em estoque: ')

if nome_do_produto == '' or categoria == '' or qtde_estoque == '':
    print('Preencher corretamente os espaços vazios')

if categoria == 'bebidas':
    if int(qtde_estoque) < 75:
        print('Solicitar {} à equipe de compras, temos apenas {} unidades de estqoue'.format(nome_do_produto,qtde_estoque))

if categoria == 'alimentos':
    if int(qtde_estoque) < 50:
        print('Solicitar {} à equipe de compras, temos apenas {} unidades de estqoue'.format(nome_do_produto,qtde_estoque))
        
if categoria == 'limpeza':
    if int(qtde_estoque) < 30:
        print('Solicitar {} à equipe de compras, temos apenas {} unidades de estqoue'.format(nome_do_produto,qtde_estoque))