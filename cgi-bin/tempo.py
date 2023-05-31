#!/usr/bin/env python 3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
unities = {
    'seg': 'Segundos',
    'min': 'Minutos',
    'hr': 'Horas'
}
consts_of_conversion = { 
    0: {
        'seg': 1,
        'min': 60,
        'hr': 3600
        },
    1: {
        'seg': 1,
        'min': 1/60,
        'hr': 1/3600
    }
}
def analyzing_value(value):
    if value:
        return int(value)
    else:
        return -1

try:
    value = analyzing_value(received)

except:
    value = 'typeError'

def convert_units(value, unity1, unity2):

    if value != -1 and value != 'typeError':

        if unity1 == unity2 and unity1 != 'sel':
            result = f'Unidades iguais => {value:.2f} {unities[unity1]}'

        try:
            value_in_seg = value * consts_of_conversion[0][unity1] 
            converted = value_in_seg * consts_of_conversion[1][unity2]

            result = f'{value} {unities[unity1]} = {converted} {unities[unity2]}'

        except:
            result = 'Erro: Selecione uma unidade !'

    elif value == 'typeError':
        result = 'Erro: Tipo de Valor Inesperado !'

    else: 
        result = 'Erro: Campo sem valores !'
        
    return result

try:
    result_final = convert_units(value, unity1, unity2)

except:
    result_final = 'Erro Inesperado'

print("Content-Type:text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Tempo</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print(f'<h2>{result_final}</h2>')
print('<a class="back" href="../tempo.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")

