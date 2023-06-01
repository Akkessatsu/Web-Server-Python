#!/usr/bin/env python 3
import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unit1 = form.getvalue('unidade1')
unit2 = form.getvalue('unidade2')
result_final:str = None
unities = {
    'cel': 'Graus Celsius',
    'fah': 'Graus Fahrenheit',
    'kel': 'Kelvin' 
}

def analyzing_value(value):
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
        return float(value)
    else:
        return -1


def convert_to_celsius(value: int, unit1: str):
    """Returns the quantity in Celsius Degree

    Args:
        value: The value of the quantity to be converted
        unit1: The unit of the quantity to be converted to Celsius Degree
    """
    match unit1:
        case 'cel':
            return value
        case 'fah':
            return (value - 32) * 5/9
        case 'kel':
            return value - 273.15

def convert_units(value: int, unit1: str, unit2: str):
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
        
        '0 Graus Celsius = 273.15 Kelvin'
        
    Raises:
        KeyError: An error occoured when a passed unit
        is not a valid key for the dict 'consts_of_conversion'
    """
    if value != -1 and value != 'typeError':
        converted = convert_to_celsius(value, unit1)

        if converted == None:
            return 'Erro: Selecione uma unidade !'
        
        match unit2:
                case 'fah':
                    converted = (converted * 9/5) + 32
                case 'kel':
                    converted -= 273.15
                case 'sel':
                        return 'Erro: Selecione uma unidade !'
                case unity1:
                    if unity1 != 'sel':
                        return f'Unidade iguais => {value:.2f} {unities[unit1]}'
                    else:
                        return 'Erro: Selecione uma unidade !'
                        
        return f'{value} {unities[unit1]} = {converted:.2f} {unities[unit2]}'

    elif value == 'typeError':
        return 'Erro: Tipo de Valor inesperado !'
    else:
        return 'Erro: Campos sem valores !'
    
try:
    value = analyzing_value(received)
except:
    value = 'typeError'

try:
    result_final = convert_units(value, unit1, unit2)
except:
    result_final = 'Erro Inesperado'

print("Content-Type:text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Temperatura</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print(f'<h2>{result_final}</h2>')
print('<a class="back" href="../temperatura.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")

