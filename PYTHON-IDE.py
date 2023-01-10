from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Multiline(size=(190,40),key='texto_do_arquivo')],
    [sg.Button('Salvar',key='salvar'), sg.Button('Abrir projeto', key='abrir_arquivo')]
]

layoutsec = [
    [sg.Text('Seu projeto foi salvo no diretorio python-ide! Feche esta janela.')]
]

def open_file() -> str:
    try:
        filename: str = sg.popup_get_file("Open File", no_window=True)
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "r") as f:
            janela["texto_do_arquivo"].update(value=f.read())
    return filename

janela = sg.Window('IDE PYTHON', layout)

janelasec = sg.Window('Projeto salvo', layoutsec)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'salvar':

        projetopy = 'fixed'

        with open ('projetopy.py', 'w') as arquivo:
            for valor in valores:
                arquivo.write(valores.get('texto_do_arquivo'))

                janelasec.read()

    if eventos == 'abrir_arquivo':
        open_file()
