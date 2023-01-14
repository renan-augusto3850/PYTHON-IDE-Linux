from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Multiline(size=(190,40),key='texto_do_arquivo')],
    [sg.Button('Salvar',key='salvar'), sg.Button('Abrir projeto', key='abrir_arquivo')]
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

def salvar_pasta_em() -> str:
    try:
     filename: str = sg.popup_get_file(
            "Save File",
            save_as=True,
            no_window=True,
            default_extension=".py",
            file_types=(("Python File", ".py"),),
        )
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "w") as f:
            f.write(valores.get("texto_do_arquivo"))
    return filename

janela = sg.Window('IDE PYTHON', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'salvar':
      salvar_pasta_em()
    if eventos == 'abrir_arquivo':
        open_file()
