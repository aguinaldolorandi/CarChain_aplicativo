import json
import warnings
warnings.filterwarnings("ignore")
from sinesp_client import SinespClient

class Consulta_Placa:
    '''
    Classe que busca placa na API do Sinesp e devolve um json com os dados do veículo
    '''
    def __init__(self, placa):
        self.placa = placa

    def sinesp(self):
        # sc = SinespClient(proxy_address='168.228.28.69', proxy_port=4145)
        sc = SinespClient()
        result = sc.search(self.placa)
        json_result = json.dumps(result)
        y = json.loads(json_result)
        x = str(y["status_message"]).upper()
        return x, y

    def result(self):
        x, y = __class__.sinesp(self)
        modelo_sinesp = y["model"].split('/')
        marca_i = modelo_sinesp[0]
        modelo_i = modelo_sinesp[1].split(' ')
        if marca_i == 'I' or marca_i == 'IMP' or marca_i == 'JTA':
            marca = modelo_i[0]
            if len(modelo_i) > 1 and len(modelo_i) < 2:
                modelo = modelo_i[1]
            if len(modelo_i) >= 2:
                modelo = str(modelo_i[1]) + ' ' + str(modelo_i[2])
            else:
                modelo = ''
        else:
            marca = marca_i
            print('a')
            if len(modelo_i) >= 2 and len(modelo_i) <= 3:
                modelo = str(modelo_i[0]) + ' ' + str(modelo_i[1])
            if len(modelo_i) > 3:
                modelo = str(modelo_i[0]) + ' ' + str(modelo_i[1]) + ' ' + str(modelo_i[2])
            if len(modelo_i) <= 1:
                modelo = modelo_i[0]

        return [{"PLACA": self.placa, "CONDIÇÃO": x,
                 "CHASSI": y["chassis"],
                 "MODELO_DETRAN": y["model"],
                 "MARCA": marca,
                 "MODELO": modelo,
                 "ANO": y["year"],
                 "ANO/MODELO": y["model_year"],
                 "COR": str(y["color"]).upper(),
                 "CIDADE": y["city"],
                 "ESTADO": y["state"],
                 "CONSULTA": y["date"]}]

