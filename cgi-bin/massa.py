#!/usr/bin/env python 3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
result_final = None

unities = {
    'mg': 'Miligramas',
    'gr': 'Gramas',
    'kg': 'Kilogramas'
}
consts_of_conversion = { 
    0: {
        'mg': 10 ** (-3),
        'gr':  1  ,
        'kg': 10 ** 3
        },
    1: {
        'mg': 10 ** 3,
        'gr': 1,
        'kg': 10 ** (-3)
    }
}


def analyzing_value(
    value
    ) -> int:
    """Retorna o valor como parâmetro se o mesmo for válido (não vazio)
    
        Args:
            value: 
                Valor a ser testado obtido por meio do método getvalue do
                formulário html
        Returns:
            Se o valor for não vazio, é convertido para float e retornado.
            Se for um valor vazio, é retornado -1
    """
    if value:
        return float(value)
    else:
        return -1
    
def convert_units(
    value: float,
    unity1: str,
    unity2: str
    ) -> str:
    """Retorna o resultado da conversão de unidades

        Args:
            value: Valor a ser convertido
            unity1: Unidade de medida do valor a ser convertido
            unity2: Unidade de medida da conversão

        Returns:
            Uma string que relaciona o valor e unidades de medidas 
            originais com o resultado da conversão. Por exemplo:

            '600 Segundos = 10.0 Minutos'

            Em que à esquerda temos o valor original e à direita o 
            resultado da conversão
    """
    if value != -1 and value != 'typeError':
        if unity1 == unity2 and unity1 != 'sel':
            result = f'Unidades iguais => {value:.2f} {unities[unity1]}'
        try:
            value_in_grams = value * consts_of_conversion[0][unity1] #Valor em gramas
            converted = value_in_grams * consts_of_conversion[1][unity2]

            result = f'{value} {unities[unity1]} = {converted} {unities[unity2]}'
        except:
            result = 'Erro: Selecione uma unidade !'

    elif value == 'typeError':
        result = 'Erro: Tipo de Valor Inesperado !'

    else: 
        result = 'Erro: Campo sem valores !'
        
    return result

try:
    value = analyzing_value(received)

except:
    value = 'typeError'


try:
    result_final = convert_units(value, unity1, unity2)

except:
    result_final = 'Erro Inesperado'

print("Content-Type: text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Massa</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print(f'<h2>{result_final}</h2>')
print('<a class="back" href="../massa.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")
