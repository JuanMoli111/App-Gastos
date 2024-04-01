import PySimpleGUI as sg

lista_tipos = [
        "Coca",
        "Frutillas",
        "Bidon de agua",
        "Milanesa",
        "Racion_Comedor",
        "Alquiler",
        "Expensas",
        "Luz",
        "Gas",
        "Credito",
        "Deuda",
        "Banana",
        "Naranja",
        "Pan",
        "Harina",
        "Detergente",
        "Lavandina",
        "Manteca",
        "Leche",
        "Chia",
        "Lechuga",
        "Tomate",
        "Don_satur",
        "Mana_rellenas",
        "Magdalenas",
        "Esponja",
        "Virulana",
        "Jabon",
        "Pasta_dental",
        "Shampoo",
        "Acondicionador",
        "Papel_higienico",
        "Rollo_cocina",
        "Aceite",
        "Azucar",
        "Yerba",
        "Miel",
        "CervezaArtesanal",
        "Vino",
        "Peluqueria",
        "Encendedor",
        "Desodorante",
        "Zapallito",
        "Papa",
        "Calabaza",
        "Cebolla",
        "Cebolla_morada",
        "Cebolla_verdeo",
        "Berenjena",
        "Morron_rojo",
        "Morron_verde",
        "Morron_amarillo",
        "Batata",
        "Manzana",
        "Ajo",
        "ComidaGatos",
        "Piedras_gatos",
        "Sube"
    ]
min_substring_length_filter = 2

def filter_types(typed_value):
    typed_value_lower = typed_value.lower()

    if len(typed_value_lower) < min_substring_length_filter:
        return lista_tipos

    matches = []

    for tipo in lista_tipos:
        product_lower = tipo.lower()
        match_count = 0
        matching_substrings = set()

        for i in range(len(typed_value_lower) - (min_substring_length_filter - 1)):
            substring = typed_value_lower[i:i + min_substring_length_filter] 
            if substring in product_lower:
                match_count += 1
                matching_substrings.add(substring)

        if match_count > 0:
            matches.append((tipo, match_count, sorted(matching_substrings)))

    # Sort matches based on the number of matches and product names
    matches.sort(key=lambda x: (x[1], x[0]), reverse=True)

    return [match[0] for match in matches]

layout = [
    [sg.Text('Select Type:')],
    [sg.Input(key='-tipo-', enable_events=True), sg.Listbox(values=lista_tipos, size=(20, 5), key='-list_tipo-', enable_events=True)],
    [sg.Button('OK'), sg.Button('Exit')]
]

window = sg.Window('Listbox Example', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-list_tipo-':
        # When an item in the listbox is clicked, update the input field
        selected_item = values['-list_tipo-'][0]
        window['-tipo-'].update(value=selected_item)

        

    elif event == '-tipo-':
        typed_value = values['-tipo-'].strip()

        filtered_types = filter_types(typed_value)

        window['-list_tipo-'].update(values=filtered_types)

window.close()
