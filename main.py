from consulta_placa import Consulta_Placa
from captura_imagem import Captura_Imagem
from carro_ou_moto import Carro_ou_Moto
from marca_modelo_detran import Marca_Modelo_Detran
from webmotors import Webmotors
from webmotors_moto import Webmotors_Moto
from mercado_livre import Mercado_Livre

#Consulta placa Sinesp
placa_imagem = input('Digite "P" para PLACA ou "I" para IMAGEM: ').upper()
while placa_imagem!= 'P' or placa_imagem!= 'I':

    if placa_imagem == 'P':
        placa = input('Insira a Placa: ').upper()
        resultado = Consulta_Placa(placa).result()
        break
    if placa_imagem == 'I':
        imagem = input('Insira a imagem: ')
        resultado = Consulta_Placa(Captura_Imagem(imagem).placa()).result()
        break
    else:
        placa_imagem = input('Digite "P" para PLACA ou "I" para IMAGEM: ').upper()
print()
print('############################################################')
for i in resultado[0]:
    print(i,':',resultado[0][i])

#Marca e modelo do veículo
marca = resultado[0]['MARCA']
modelo = resultado[0]['MODELO']
ano = resultado[0]['ANO/MODELO']
cidade = resultado[0]['CIDADE']
estado = resultado[0]['ESTADO']
veiculo = Carro_ou_Moto(marca, modelo).veiculo()
marca_detran = Marca_Modelo_Detran(marca,veiculo).marca_detran()

# Veículos anunciados na Webmotors
if veiculo == 'carros':
    #Req = Webmotors(veiculo, marca_detran, modelo, ano, cidade, estado)
    #print('##########################################################')
    #print('Carro correspondente de menor valor anunciado na Webmotors')
    #if Req.soup():
     #   for i in Req.soup():
      #      print(i)
    Req_ML = Mercado_Livre(veiculo, marca_detran, modelo.replace(' ',''), ano, cidade, estado)
    print('##########################################################')
    print('Carro correspondente de menor valor anunciado no Mercado Livre')
    if Req_ML.soup():
        for i in Req_ML.soup():
            print(i)


else:
    veiculo == 'motos'
    Req = Webmotors_Moto(veiculo, marca_detran, modelo, ano, cidade, estado)
    print('#########################################################')
    print('Moto correspondente de menor valor anunciado na Webmotors')
    if Req.soup():
        for i in Req.soup():
            print(i)
    Req_ML = Mercado_Livre(veiculo, marca_detran, modelo.replace(' ',''), ano, cidade, estado)
    print('##########################################################')
    print('Carro correspondente de menor valor anunciado no Mercado Livre')
    if Req_ML.soup():
        for i in Req_ML.soup():
            print(i)

#print(Req.get_req().url)
'''

print('Refine sua busca')

marca2 = input('Insira a marca:')
modelo2 = input('insira o modelo:')
ano2 = input('insira o ano:')
Req2 = Webmotors('carros', marca2, modelo2, ano2, cidade,estado)

print()
if Req2.soup():
    for i in Req2.soup():
        print(i)
'''


