def calcular_apartamento(qtd_quartos):
    return 700.00 + (200.00 * qtd_quartos)


def calcular_casa(qtd_quartos):
    return 900.00 + (250.00 * qtd_quartos)


def calcular_estudio(qtd_quartos):
    return 1200.00 + (300.00 * qtd_quartos)


# 
def aplicar_desconto_sem_crianca(valor, possui_crianca):
    if not possui_crianca:
        return valor * 0.995   
    return valor


# 
def aplicar_parcelamento(valor):
    if valor >= 2000.00:
        parcela = valor / 5
        return True, parcela
    return False, valor


# 
def calcular_valor(tipo_imovel, qtd_quartos, possui_crianca):

    if tipo_imovel == 'A':
        valor = calcular_apartamento(qtd_quartos)

        
        valor = aplicar_desconto_sem_crianca(valor, possui_crianca)

    elif tipo_imovel == 'C':
        valor = calcular_casa(qtd_quartos)

    elif tipo_imovel == 'E':
        valor = calcular_estudio(qtd_quartos)

    
    parcelado, valor_parcela = aplicar_parcelamento(valor)

    return valor, parcelado, valor_parcela
