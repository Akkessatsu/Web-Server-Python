#!/usr/bin/env python 3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unit1 = form.getvalue('unidade1')
unit2 = form.getvalue('unidade2')
result_final: str

unities = {
    'mg': 'Miligramas',
    'gr': 'Gramas',
    'kg': 'Kilogramas'
}
consts_of_conversion = { 
    'to_gram': {
        'mg': 10 ** (-3),
        'gr':  1  ,
        'kg': 10 ** 3
        },
    'from_gram': {
        'mg': 10 ** 3,
        'gr': 1,
        'kg': 10 ** (-3)
    }
}


def analyzing_value(value) -> int:
    """Returns the argument if it is not void
    
        Args:
            value: 
                Value to be tested obtained through the getvalue method of
                html form
                
        Returns:
            If the value is not void, it is converted to int and returned
            If it is void, return -1
    """
    if value:
        return int(value)
    else:
        return -1

def convert_to_gram(value: int, unit: str) -> float:
    """Returns the quantity in grams
    
    Args:
        value: The value of the quantity to be converted
        unity: The unit of the quantity to be converted to grams
    """
    return value * consts_of_conversion['to_gram'][unit]

def convert_from_gram(value: int, unit: str) -> float:
    """Returns the value in grams to other unit of mass
    
    Args:
        value: The value of the quantity in grams to be converted
        unity: The unit of the quantity to be converted
    """
    return value * consts_of_conversion['from_gram'][unit]

def convert_units(value: int, unit1: str, unit2: str) -> str:
    """Returns a string with the result of the conversion

    Args:
        value: The value of the quantity to be converted
        unit1: The unit of the original quantity
        unit2: The unit of the converted quantity

    Returns:
        A string containing the information of the conversion
        in the format:
        
        '[Original Value] [Original Unit] = [Converted Value] [Unit of conversion]'
        
        Example:
        
        '10 Quilogramas = 10000.00 Gramas'
        
    Raises:
        KeyError: An error occoured when a passed unit
        is not a valid key for the dict 'consts_of_conversion'
    """
    if value != -1 and value != 'typeError':
        
        if unit1 == unit2 and unit1 != 'sel':
            return f'Unidades iguais => {value:.2f} {unities[unit1]}'
        
        try:
            value_in_grams = convert_to_gram(value, unit1)
            converted = convert_from_gram(value_in_grams, unit2)
            
            return  f'{value} {unities[unit1]} = {converted} {unities[unit2]}'
        except:
            return 'Erro: Selecione uma unidade !'

    elif value == 'typeError':
        return 'Erro: Tipo de Valor Inesperado !'
    
    else: 
        return 'Erro: Campo sem valores !'
        

try:
    value = analyzing_value(received)
except:
    value = 'typeError'
    
try:
    result_final = convert_units(value, unit1, unit2)
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
