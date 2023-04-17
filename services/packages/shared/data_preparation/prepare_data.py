def prepare_data(data, hasLabels: bool):
    for row in data:
        if hasLabels is True:
            for key in ['idade', 'colesterol', 'pressao_arterial', 'acucar_sangue', 'risco_cardiovascular']:
                if key not in row:
                    row[key] = 0
        else:
            for key in ['idade', 'colesterol', 'pressao_arterial', 'acucar_sangue']:
                if key not in row:
                    row[key] = 0
        for key in ['genero', 'historico_familiar', 'historico_tabagismo', 'consumo_alcool', 'hipertensao']:
            if key not in row:
                row[key] = ''
    return data
