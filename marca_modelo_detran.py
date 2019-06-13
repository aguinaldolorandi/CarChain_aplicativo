
class Marca_Modelo_Detran:

    def __init__(self, marca, veiculo):
        self.marca = marca
        self.veiculo = veiculo

    def marca_detran(self):

        carro_fipe_detran = {'ACURA': 'ACURA', 'AGRALE': 'AGRALE', 'ALFA ROMEO': 'ALFA ROMEO', 'AM GEN': 'AM GEN',
                             'ASIA MOTORS': 'ASIA MOTORS', 'ASTON MARTIN': 'ASTON MARTIN', 'AUDI': 'AUDI', 'BMW': 'BMW',
                             'BRM': 'BRM', 'BUGGY': 'BUGGY', 'BUGRE': 'BUGRE', 'CADILLAC': 'CADILLAC',
                             'CBT JIPE': 'CBT JIPE', 'CHANA': 'CHANA', 'CHANGAN': 'CHANGAN', 'CHERY': 'CHERY',
                             'CHEVROLET': 'CHEVROLET', 'CHRYSLER': 'CHRYSLER', 'CITROËN': 'CITROËN',
                             'CROSS LANDER': 'CROSS LANDER', 'DAEWOO': 'DAEWOO', 'DAIHATSU': 'DAIHATSU',
                             'DODGE': 'DODGE', 'EFFA': 'EFFA', 'ENGESA': 'ENGESA', 'ENVEMO': 'ENVEMO',
                             'FERRARI': 'FERRARI', 'FIAT': 'FIAT', 'FIBRAVAN': 'FIBRAVAN', 'FORD': 'FORD',
                             'FOTON': 'FOTON', 'FYBER': 'FYBER', 'GEELY': 'GEELY', 'GM': 'GM',
                             'GREAT WALL': 'GREAT WALL', 'GURGEL': 'GURGEL', 'HAFEI': 'HAFEI', 'HONDA': 'HONDA',
                             'HYUNDAI': 'HYUNDAI', 'ISUZU': 'ISUZU', 'JAC': 'JAC', 'JAGUAR': 'JAGUAR', 'JEEP': 'JEEP',
                             'JINBEI': 'JINBEI', 'JPX': 'JPX', 'KIA MOTORS': 'KIA MOTORS', 'LADA': 'LADA',
                             'LAMBORGHINI': 'LAMBORGHINI', 'LAND ROVER': 'LAND ROVER', 'LEXUS': 'LEXUS',
                             'LIFAN': 'LIFAN', 'LOBINI': 'LOBINI', 'LOTUS': 'LOTUS', 'MAHINDRA': 'MAHINDRA',
                             'MASERATI': 'MASERATI', 'MATRA': 'MATRA', 'MAZDA': 'MAZDA', 'M.BENZ': 'MERCEDES-BENZ',
                             'MERCURY': 'MERCURY', 'MG': 'MG', 'MINI': 'MINI', 'MMC': 'MITSUBISHI', 'MIURA': 'MIURA',
                             'NISSAN': 'NISSAN', 'PEUGEOT': 'PEUGEOT', 'PLYMOUTH': 'PLYMOUTH', 'PONTIAC': 'PONTIAC',
                             'PORSCHE': 'PORSCHE', 'RAM': 'RAM', 'RELY': 'RELY', 'RENAULT': 'RENAULT',
                             'ROLLS-ROYCE': 'ROLLS-ROYCE', 'ROVER': 'ROVER', 'SAAB': 'SAAB', 'SATURN': 'SATURN',
                             'SEAT': 'SEAT', 'SHINERAY': 'SHINERAY', 'SMART': 'SMART', 'SSANGYONG': 'SSANGYONG',
                             'SUBARU': 'SUBARU', 'SUZUKI': 'SUZUKI', 'TAC': 'TAC', 'TOYOTA': 'TOYOTA',
                             'TROLLER': 'TROLLER', 'VOLVO': 'VOLVO', 'VW': 'VOLKSWAGEN', 'WAKE': 'WAKE', 'WALK': 'WALK',
                             'WILLYS': 'WILLYS'}

        moto_fipe_detran = {'ADLY': 'ADLY', 'AGRALE': 'AGRALE', 'AMAZONAS': 'AMAZONAS', 'APRILIA': 'APRILIA',
                            'ATALA': 'ATALA', 'BAJAJ': 'BAJAJ', 'BEE': 'BEE', 'BENELLI': 'BENELLI', 'BETA': 'BETA',
                            'BIMOTA': 'BIMOTA', 'BMW': 'BMW', 'BRANDY': 'BRANDY', 'BRAVA': 'BRAVA', 'BRP': 'BRP',
                            'BUELL': 'BUELL', 'BUENO': 'BUENO', 'BYCRISTO': 'BYCRISTO', 'CAGIVA': 'CAGIVA',
                            'CALOI': 'CALOI', 'DAELIM': 'DAELIM', 'DAFRA': 'DAFRA', 'DAYANG': 'DAYANG',
                            'DAYUN': 'DAYUN', 'DERBI': 'DERBI', 'DUCATI': 'DUCATI', 'EMME': 'EMME', 'FOX': 'FOX',
                            'FYM': 'FYM', 'GARINNI': 'GARINNI', 'GAS GAS': 'GAS GAS', 'GREEN': 'GREEN',
                            'HAOBAO': 'HAOBAO', 'HAOJUE': 'HAOJUE', 'HARLEY DAVIDSON': 'HARLEY DAVIDSON',
                            'HERO': 'HERO', 'HONDA': 'HONDA', 'HUSABERG': 'HUSABERG', 'HUSQVARNA': 'HUSQVARNA',
                            'INDIAN': 'INDIAN', 'IROS': 'IROS', 'JIAPENG VOLCANO': 'JIAPENG VOLCANO',
                            'JOHNNYPAG': 'JOHNNYPAG', 'JONNY': 'JONNY', 'JTZ': 'JTZ', 'KAHENA': 'KAHENA',
                            'KASINSKI': 'KASINSKI', 'KAWASAKI': 'KAWASAKI', 'KTM': 'KTM', 'KYMCO': 'KYMCO',
                            "L'AQUILA": "L'AQUILA", 'LANDUM': 'LANDUM', 'LAVRALE': 'LAVRALE', 'LERIVO': 'LERIVO',
                            'LIFAN': 'LIFAN', 'LON-V': 'LON-V', 'MAGRÃO TRICICLOS': 'MAGRÃO TRICICLOS',
                            'MALAGUTI': 'MALAGUTI', 'MIZA': 'MIZA', 'MOTO GUZZI': 'MOTO GUZZI', 'MOTOCAR': 'MOTOCAR',
                            'MOTORINO': 'MOTORINO', 'MRX': 'MRX', 'MV AGUSTA': 'MV AGUSTA', 'MVK': 'MVK',
                            'ORCA': 'ORCA', 'PEGASSI': 'PEGASSI', 'PEUGEOT': 'PEUGEOT', 'PIAGGIO': 'PIAGGIO',
                            'REGAL RAPTOR': 'REGAL RAPTOR', 'RIGUETE': 'RIGUETE', 'ROYAL ENFIELD': 'ROYAL ENFIELD',
                            'SANYANG': 'SANYANG', 'SHINERAY': 'SHINERAY', 'SIAMOTO': 'SIAMOTO', 'SUNDOWN': 'SUNDOWN',
                            'SUZUKI': 'SUZUKI', 'TARGOS': 'TARGOS', 'TIGER': 'TIGER', 'TRAXX': 'TRAXX',
                            'TRIUMPH': 'TRIUMPH', 'VENTO': 'VENTO', 'WUYANG': 'WUYANG', 'YAMAHA': 'YAMAHA',
                            'H.DAVIDSON': 'HARLEY DAVIDSON'}

        if self.veiculo == 'motos':
            marca_detran = moto_fipe_detran[self.marca]
        else:
            marca_detran = carro_fipe_detran[self.marca]

        return marca_detran
