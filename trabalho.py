import calculos


nome = input('Informe seu nome: ')

tipo_de_imovel = ""

while tipo_de_imovel not in ['A', 'C','E']:

    tipo_de_imovel = input('''Infome o tipo de imovel
                  
(C) - Casa
(A) - Apartamento
(E) - Estudio
       
Digite a opção desejada: ''').upper()

Quantidade_quartos = 0 

while Quantidade_quartos < 1 or Quantidade_quartos > 9: 
    Quantidade_quartos = int(input ('''Informe a quantidade de quartos:
    (1) Quarto
    (2) Quartos
    (3) Quartos
    (4) Quartos
    (5) Quartos
    (6) Quartos
    (7) Quartos
    (8) Quartos
    (9) Quartos
'''))
print 
valor_ap = 700.00 + 200.00 * Quantidade_quartos
valor_casa = 900.00 + 250.00 * Quantidade_quartos
valor_estudio = 1200.00 + 300.00 * Quantidade_quartos


if tipo_de_imovel == 'A':
    print("\nResumo da locação")
    print("-------------------------")
    print("Nome:", nome)
    print("Tipo de Imóvel: Apartamento")
    print("Quantidade de Quartos:", Quantidade_quartos)
    print("Valor do Aluguel: R$", valor_ap)

elif tipo_de_imovel == 'C':
    print("\nResumo da locação")
    print("-------------------------")
    print("Nome:", nome)
    print("Tipo de Imóvel: Casa")
    print("Quantidade de Quartos:", Quantidade_quartos)
    print("Valor do Aluguel: R$", valor_casa)

elif tipo_de_imovel == 'E':
    print("\nResumo da locação")
    print("-------------------------")
    print("Nome:", nome)
    print("Tipo de Imóvel: Estudio")
    print("Quantidade de Quartos:", Quantidade_quartos)
    print("Valor do Aluguel: R$", valor_estudio)

