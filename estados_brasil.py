
class Estados_Brasil():
    def __init__(self,estado_sigla):
        self.estado_sigla = estado_sigla
    def sigla(self):
        estados = {
                    'AC':'Acre',
                    'AL':'Alagoas',
                    'AP':'Amapá',
                    'AM':'Amazonas',
                    'BA':'Bahia',
                    'CE':'Ceará',
                    'DF':'Distrito Federal',
                    'ES':'Espírito Santo',
                    'GO':'Goiás',
                    'MA':'Maranhão',
                    'MT':'Mato Grosso',
                    'MS':'Mato Grosso do Sul',
                    'MG':'Minas Gerais',
                    'PA':'Pará',
                    'PB':'Paraíba',
                    'PR':'Paraná',
                    'PE':'Pernambuco',
                    'PI':'Piauí',
                    'RJ':'Rio de Janeiro',
                    'RN':'Rio Grande do Norte',
                    'RS':'Rio Grande do Sul',
                    'RO':'Rondônia',
                    'RR':'Roraima',
                    'SC':'Santa Catarina',
                    'SP':'São Paulo',
                    'SE':'Sergipe',
                    'TO':'Tocantins'
                }
        return estados[self.estado_sigla]

    def sigla_ML(self):
        estados = {
                    'AC':'acre',
                    'AL':'alagoas',
                    'AP':'amapa',
                    'AM':'amazonas',
                    'BA':'bahia',
                    'CE':'ceara',
                    'DF':'distrito federal',
                    'ES':'espirito santo',
                    'GO':'goias',
                    'MA':'maranhao',
                    'MT':'mato grosso',
                    'MS':'mato grosso do sul',
                    'MG':'minas gerais',
                    'PA':'para',
                    'PB':'paraiba',
                    'PR':'parana',
                    'PE':'pernambuco',
                    'PI':'piaui',
                    'RJ':'rio de janeiro',
                    'RN':'rio grande do norte',
                    'RS':'rio grande do sul',
                    'RO':'rondonia',
                    'RR':'roraima',
                    'SC':'santa catarina',
                    'SP':'sao paulo',
                    'SE':'sergipe',
                    'TO':'tocantins'
                }
        return estados[self.estado_sigla]

