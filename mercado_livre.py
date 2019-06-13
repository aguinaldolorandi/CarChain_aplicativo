import requests
from bs4 import BeautifulSoup
from estados_brasil import Estados_Brasil

class Mercado_Livre:
    def __init__(self, veiculo, marca, modelo, ano, cidade, estado_sigla):
        self.veiculo = veiculo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cidade = cidade
        self.estado_sigla = estado_sigla

    def get_req(self):
        anos = '{}-{}'.format(self.ano, int(self.ano) + 2)
        estado = Estados_Brasil(self.estado_sigla).sigla_ML().replace(' ','-')
        cidade = str(self.cidade).lower()
        url = 'https://{}.mercadolivre.com.br/{}/{}/{}/{}/{}/_OrderId_PRICE_PriceRange_2000-0'.format(self.veiculo.lower(),self.marca.lower(),
                                                                                                      self.modelo.lower(),
                                                                                                      estado.lower(),
                                                                                                      cidade,
                                                                                                      anos)
        header = {
                    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:64.0) Gecko/20100101 Firefox/64.0',
                    'Referer': 'https://www.mercadolivre.com.br/',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Host': 'carros.mercadolivre.com.br'
                     }
        try:
            req = requests.get(url, headers=header)
            print(url)
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


        if soup.find('h3',class_='header__title') == 'Nesta categoria não há veículos que coincidam com a sua busca.':
            print('Nenhum veículo econtrado')
            soup = None
        else:
            json = [{},{},{},{},{},{}]

            json[0]['Título'] = soup.find('span', class_= "main-title").string
            json[1]['Atributos'] = soup.find('div', class_= "item__attrs").string
            json[2]['Preço mínimo'] = soup.find('span', class_= "price__fraction").string
            json[3]['Localização'] = soup.find('div', class_= "item__location").string
            json[4]['Anunciados'] = soup.find('div', class_= 'quantity-results').string
            json[5]['Link do anúncio'] = soup.find('a', class_= "item__info-link item__js-link")['href']
            return json




"""
        ano_inicial = 2008
        ano_final = 2010
        marca = 'honda'
        modelo = 'civiclxs'
        estado = 'sao-paulo'
        cidade = 'piracicaba'
        ano = '{}-{}'.format(ano_inicial, ano_final)
        Nesta categoria não há veículos que coincidam com a sua busca.
        print(soup.find('div', class_= 'quantity-results').string)
        print(soup.find('span', class_= "price__fraction").string)
        print(soup.find('div', class_= "item__attrs").string)
        print(soup.find('span', class_= "main-title").string)
        print(soup.find('div', class_= "item__location").string)
        print(soup.find('a', class_= "item__info-link item__js-link")['href'])
"""