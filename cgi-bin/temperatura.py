#!/usr/bin/env python 3
import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
result_final = None
unities = {
    'cel': 'Graus Celsius',
    'fah': 'Graus Fahrenheit',
    'kel': 'Kelvin' 
}

def analyzing_value(value):
    if value:
        return float(value)
    else:
        return -1

try:
    value = analyzing_value(received)

except:
    value = 'typeError'

def convert_to_celsius(value, unity1):
        match unity1:
            case 'cel':
                return value
            case 'fah':
                return (value - 32) * 5/9
            case 'kel':
                return value - 273.15
            case 'sel':
                return 'Erro: Selecione uma unidade !'

def convert_units(value, unity1, unity2):
    if value != -1 and value != 'typeError':
        converted = convert_to_celsius(value, unity1)

        if type(converted) == str:
            return converted
        
        match unity2:
                case 'fah':
                    converted = (converted * 9/5) + 32
                case 'kel':
                    converted -= 273.15
                case 'sel':
                        return 'Erro: Selecione uma unidade !'
                case unity1:
                    if unity1 != 'sel':
                        return f'Unidade iguais => {value:.2f} {unities[unity1]}'
                    else:
                        return 'Erro: Selecione uma unidade !'
                        
        return f'{value} {unities[unity1]} = {converted:.2f} {unities[unity2]}'
    
    elif value == 'typeError':
        return 'Erro: Tipo de Valor inesperado !'
    else:
        return 'Erro: Campos sem valores !'

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

