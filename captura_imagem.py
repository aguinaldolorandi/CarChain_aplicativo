import requests
import base64
import json

class Captura_Imagem:
    def __init__(self, imagem):
        self.imagem = imagem

    def alpr(self):
        IMAGE_PATH = self.imagem
        SECRET_KEY = 'sk_521f1bbec81d0405ee387103'
        # Captura de imagem da placa:
        with open(IMAGE_PATH, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())
        url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=0&country=br&secret_key=%s' % (SECRET_KEY)
        r = requests.post(url, data=img_base64)
        results = r.json()
        return results

    def placa(self):
        results = __class__.alpr(self)
        placa = results['results'][0]['plate']
        return placa
