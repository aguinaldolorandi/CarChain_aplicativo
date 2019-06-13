import requests
from bs4 import BeautifulSoup
from municipios_brasileiros import Latitude_Longitude
from estados_brasil import Estados_Brasil

class Webmotors_Moto:
    def __init__(self, veiculo, marca, modelo, ano, cidade, estado_sigla):
        self.veiculo = veiculo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cidade = cidade
        self.estado_sigla = estado_sigla

    def get_req(self):

        header = {
            'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 ',
            'Referer': 'https://www.webmotors.com.br/',
            'Accept': 'text / html, application / xhtml + xml,aplication / xml;q = 0.9, * / *;q = 0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'pt - BR, pt; q = 0.8, en - US; q = 0.5, en; q = 0.3',
            'Host': 'www.webmotors.com.br'
             }

        latitude = Latitude_Longitude(self.cidade).lat_long()[0]
        longitude = Latitude_Longitude(self.cidade).lat_long()[1]
        km = 100
        localizacao = '{},{}x{}km'.format(latitude, longitude, km)
        estadocidade = '{}-{}'.format(Estados_Brasil(self.estado_sigla).sigla().lower(),self.cidade.lower())

        parametros = {'tipoveiculo': self.veiculo.lower(),
                    'marca1': self.marca.lower(),
                    'anode': int(self.ano) -1,
                    'anoate': int(self.ano) + 2,
                    'anunciante': 'concessionária|loja|pessoa física',
                    'precode': 2000,
                    'precoate': '',
                    'palavrachave': self.modelo.lower(),
                    'kmde': 0,
                    'kmate': '',
                    'localizacao': localizacao,
                    'estadocidade': estadocidade,
                    'o': 5,
                    'p': 1,
                    'qt': 36
                     }

        url = 'https://www.webmotors.com.br/{}/{}-{}/{}/de.{}?'.format(self.veiculo.lower(),self.estado_sigla.lower(),self.cidade.lower(),self.marca.lower(),self.ano)
        try:
            req = requests.get(url, params=parametros, headers=header, timeout=10)
            return req
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout,
                requests.exceptions.TooManyRedirects, requests.exceptions.RequestException) as e:
            print(str(e))
            req = None
        except Exception as e:
            raise

    def soup(self):
        req = __class__.get_req(self)
        soup = BeautifulSoup(req.text, 'lxml')


        if (soup.find(class_='dis-tc valign-m title').span.string.replace('\t', '').replace('\r\n', '')).split(' ')[
            0] == 'Nenhuma':
            print('Nenhuma moto econtrada')
            soup = None
        else:
            json = [{},{},{},{},{},{},{},{},{},{},{}]

            atributos = [atributo.string for atributo in soup.findAll('div', class_="mrg-left attributes")[0] if
                         atributo.string != ' ']

            json[0]['Marca'] = soup.find(class_='make-model').string
            json[1]['Modelo'] = soup.find(class_='version').string
            json[2]['Preço mínimo'] = soup.find(class_='price').span.next_element.next_element
            json[3]['Ano/modelo'] = soup.find(class_="spr-resultado-busca ico-year").next_element.string
            json[4]['KM'] = soup.find(class_="spr-resultado-busca ico-km").next_element.string
            json[5]['Cor'] = soup.find(class_="spr-resultado-busca ico-color").next_element.string
            json[6]['Motor'] = soup.find(class_="spr-resultado-busca ico-engine").next_element.string
            json[7]['Atributos'] = atributos
            json[8]['Cidade'] = soup.find('div', class_="card-footer").span.string
            json[9]['Anunciados'] = soup.find(class_='dis-tc valign-m title').span.string.replace('\t','').replace('\r\n','')
            json[10]['Link do anúncio'] = soup.find('a', class_ = "nn tipo1 c-after")['href']
            return json










'''
        print(soup.find('a', class_="nn tipo1 c-after")['href'])


        lista1 = []
        for i in soup.find_all(class_='price-novo space-preco'):
            lista1.append(float((str(i.span.next_element.next_element)).replace('\n', '').replace('.', '')))
        print('Preço Máximo', max(lista1))
        print('Preço Mínimo', min(lista1))
        # print(round(np.mean(lista1),2))

        lista = []
        for i in soup.find_all(class_="resultado-busca-ico-km"):
            if i.next_element.next_element.string != ' N/I':
                km = ((str(i.next_element.next_element.string)).replace('km', '').replace('.', ''))
                lista.append(float(km))

        print('KM máxima', max(lista))
        print('KM mínima', min(lista))
        # print(round(np.mean(lista2),2))
'''








