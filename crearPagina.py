colors = {
    'procedimientos': '#cd5c5c',
    'cuerpos': '#99ccff',
    'afecciones': '#ffa500'
}

body = f'''
        <p>
        {doc}
        </p>
        <br>
        '''
for titulo in titulos:
    body = body.replace(titulo,f'<span style="background-color: #99ccff">{titulo}</span>')
with open('titulos.html', 'w') as f:
    f.write(body)

