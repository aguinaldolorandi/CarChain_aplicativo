import requests
from bs4 import BeautifulSoup
from municipios_brasileiros import Latitude_Longitude
from estados_brasil import Estados_Brasil

class Webmotors:
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
                    'anode': self.ano,
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
            0] == 'Nenhum':
            print('Nenhum carro econtrado')
            soup = None
        else:
            json = [{},{},{},{},{},{},{},{}]

            veiculo_detalhe = [detalhe.string for i in range(0, 3) for detalhe in
                               soup.findAll('div', class_="info-veiculo-detalhe")[i] if detalhe.string != ' ']

            atributos = [atributo.string for atributo in soup.findAll('div', class_="mrg-left attributes")[0] if
                         atributo.string != ' ']

            json[0]['Marca'] = soup.find(class_='make-model-financiamento').string
            json[1]['Modelo'] = soup.find(class_='version').string
            json[2]['Preço mínimo'] = soup.find(class_='price-novo space-preco').span.next_element.next_element
            json[3]['Detalhes'] = veiculo_detalhe
            json[4]['Atributos'] = atributos
            json[5]['Cidade'] = soup.find('div', class_="card-footer-novo").span.string
            json[6]['Anunciados'] = soup.find(class_='dis-tc valign-m title').span.string.replace('\t','').replace('\r\n','')
            json[7]['Link do anúncio'] = soup.find('a', class_ = "nn tipo1 c-after")['href']
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








