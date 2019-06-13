
class Carro_ou_Moto:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def veiculo(self):

        motos = [
            ['ADLY', 'AGRALE', 'AMAZONAS', 'APRILIA', 'ATALA', 'BAJAJ', 'BEE', 'BENELLI', 'BETA', 'BIMOTA', 'BMW', 'BRANDY',
             'BRAVA', 'BRP', 'BUELL', 'BUENO', 'BYCRISTO', 'CAGIVA', 'CALOI', 'DAELIM', 'DAFRA', 'DAYANG', 'DAYUN', 'DERBI',
             'DUCATI', 'EMME', 'FOX', 'FYM', 'GARINNI', 'GAS GAS', 'GREEN', 'HAOBAO', 'HAOJUE', 'HARLEY DAVIDSON', 'HERO',
             'HONDA', 'HUSABERG', 'HUSQVARNA', 'INDIAN', 'IROS', 'JIAPENG VOLCANO', 'JOHNNYPAG', 'JONNY', 'JTZ', 'KAHENA',
             'KASINSKI', 'KAWASAKI', 'KTM', 'KYMCO', "L'AQUILA", 'LANDUM', 'LAVRALE', 'LERIVO', 'LIFAN', 'LON-V',
             'MAGRÃO TRICICLOS', 'MALAGUTI', 'MIZA', 'MOTO GUZZI', 'MOTOCAR', 'MOTORINO', 'MRX', 'MV AGUSTA', 'MVK', 'ORCA',
             'PEGASSI', 'PEUGEOT', 'PIAGGIO', 'REGAL RAPTOR', 'RIGUETE', 'ROYAL ENFIELD', 'SANYANG', 'SHINERAY', 'SIAMOTO',
             'SUNDOWN', 'SUZUKI', 'TARGOS', 'TIGER', 'TRAXX', 'TRIUMPH', 'VENTO', 'WUYANG', 'YAMAHA', 'H.DAVIDSON']]

        moto_modelo_honda = [
            ['AMERICA CLASSIC 1600', 'BIZ110I', 'BIZ125 ES/ ES F.INJ./ES MIX F.INJECTION', 'BIZ125 EX/ 125 EX FLEX',
             'BIZ 125 FLEX', 'BIZ125 KS/ KS F.INJ./KS MIX F.INJECTION', 'BIZ125+', 'C100 BIZ+', 'C100 BIZ-ES',
             'C100 BIZ/ 100 BIZ KS', 'C100 DREAM', 'CB1000R', 'CB300R/ 300R FLEX', 'CB450 DX', 'CB500', 'CB500F',
             'CB500X', 'CB600F HORNET', 'CB650F', 'CB TWISTER/FLEXONE 250CC', 'CB1300 SUPER FOUR', 'CBR1000 F',
             'CBR1000 RR FIRE BLADE', 'CBR1100 XX SUPER BLACKBIRD', 'CBR250R', 'CBR450', 'CBR450 SR', 'CBR500R',
             'CBR600 F', 'CBR600 RR', 'CBR650F', 'CBR900 RR FIRE BLADE', 'CBX150 AERO', 'CBX200 STRADA',
             'CBX250 TWISTER', 'CBX750 FOUR', 'CBX 750 FOUR INDY', 'CBX 750 R', 'CG 125', 'CG125 CARGO ES',
             'CG125 CARGO ESD', 'CG125 CARGO/ CARGO KS/125I CARGO', 'CG 125 FAN / FAN KS / 125 I FAN', 'CG125 FAN ES',
             'CG125 FAN ESD', 'CG125 TITAN', 'CG 125 TITAN-ES', 'CG 125 TITAN-KS', 'CG125 TITAN-KSE', 'CG125 TODAY',
             'CG150 CARGO ESD FLEX', 'CG150 FAN ESDI/ 150 FAN ESDI FLEX', 'CG150 FAN ESI/ 150 FAN ESI FLEX',
             'CG150 SPORT', 'CG150 START FLEXONE', 'CG150 TITAN-ES', 'CG150 TITAN-ES MIX', 'CG50 TITAN-ESD MIX/FLEX',
             'CG150 TITAN-ESD/ TITAN SPECIAL EDITION', 'CG150 TITAN-EX MIX/FLEX', 'CG150 TITAN-KS MIX',
             'CG150 TITAN-KS/ TITAN-JOB', 'CG160 CARGO', 'CG160 FAN ESDI FLEXONE', 'CG160 FAN FLEX', 'CG160 START',
             'CG160 TITAN FLEXONE/ED.ESPECIAL 40 ANOS', 'CH125-R SPACY', 'CR125', 'CR250', 'CR80',
             'CRF1000L AFRICA TWIN', 'CRF1000L AFRICA TWIN TE', 'CRF110F', 'CRF 150F', 'CRF230 F', 'CRF250 X',
             'CRF250L', 'CTX 700N', 'DOMINATOR 650', 'GOLD WING 1500/ 1800', 'LEAD 110', 'MAGNA 750', 'NC700 X/ 700X ABS',
             'NC750X/NC 750X ABS', 'NX 150', 'NX 200', 'NX 350 SAHARA', 'NX400I FALCON', 'NX-4 FALCON 400',
             'NXR125 BROS ES', 'NXR 125 BROS KS', 'NXR 150 BROS ES', 'NXR150 BROS ES MIX/FLEX', 'NXR150 BROS ESD',
             'NXR150 BROS ESD MIX/FLEX', 'NXR150 BROS KS', 'NXR150 BROS KS MIX/FLEX', 'NXR160 BROS',
             'NXR160 BROS ESD FLEXONE', 'NXR160 BROS ESDD FLEXONE', 'PCX150 SPORT', 'PCX150/DLX', 'POP100 97CC',
             'POP110I', 'SH150I/DLX', 'SH 300I', 'SHADOW 1100 AC', 'SHADOW 1100 OURO', 'SHADOW AM 750', 'SHADOW VT 1100',
             'SUPERHAWK 1000', 'TRX350 FOURTRAX  FM QUADRICICLO', 'TRX 350 FOURTRAX  TM QUADRICICLO',
             'TRX420 FOURTRAX   TM 4X2 QUADRICICLO', 'TRX420 FOURTRAX  FM 4X4 QUADRICICLO', 'VALKYRIE 1500', 'VFR1200F',
             'VFR1200X CROSSTOURER', 'VT600 C SHADOW', 'VT750 SHADOW', 'VTX1800R/ 1800S/ 1800C 1795CC',
             'XL1000V VARADERO', 'XL 125 DUTY', 'XL 125 S', 'XL 700V TRANSALP', 'XLR125', 'XLR125 ES', 'XLX250 R',
             'XLX350 R', 'XR200 R', 'XR250 TORNADO', 'XR 650', 'XRE190', 'XRE300 ADVENTURE FLEX', 'XRE300 RALLY FLEX',
             'XRE 300/ 300 ABS/ FLEX']]

        moto_modelo_bmw = [
            ['C600 SPORT', 'C650 GT', 'F650', 'F650 CS', 'F650 GS/DAKAR', 'F700 GS', 'F800 GS 798CC', 'F800 GS ADVENTURE',
             'F800 GS TRIPLE BLACK/TROPHY', 'F800 R', 'F800 S 798CC', 'G310 GS', 'G310 R', 'G450 X', 'G650 GS',
             'G650 GS SERTÃO', 'G650 X CHALLENGE', 'G650 X COUNTRY', 'G650 X MOTO', 'K1100 LT', 'K1100 RS', 'K1200 GT',
             'K1200 LT', 'K1200 R', 'K1200 RS', 'K1200 S', 'K1300 GT', 'K1300 R', 'K1300 S', 'K1600 BAGGER', 'K1600 GT ',
             'K1600 GTL', 'K1600 GTL EXCLUSIVE', 'R1100 GS', 'R1100 GS-75', 'R1100 R', 'R1100 RS', 'R1100 RT', 'R1100 S',
             'R1150 GS', 'R1150 GS ADVENTURE', 'R1150 R/ R 1150 R ROCKSTER', 'R1150 RS', 'R1150 RT', 'R1200 C AVANTGARD',
             'R1200 C CLASSIC', 'R1200 C INDEPENDENT', 'R1200 CL', 'R1200 GS', 'R1200 GS ADVENTURE',
             'R1200 GS ADVENTURE RALLY', 'R1200 GS ADVENTURE TRIPLE BLACK', 'R1200 GS HP2', 'R1200 GS RALLYE',
             'R1200 GS TRIPLE BLACK', 'R1200 NINE T', 'R1200 R/ R CLASSIC', 'R1200 RT', 'S1000 R', 'S1000 RR', 'S1000 XR',
             'S1000 RR HP4 COMPETITION', 'S1000 RR HP4 STREET']]

        moto_modelo_suzuki = [
            ['ADDRESS/AE 50', 'ADDRESS/AG 100', 'AN 125 BURGMAN', 'BANDIT 1200S', 'BANDIT 1250S', 'BANDIT 600S/ 650S',
             'BANDIT N-1200', 'BANDIT N-1250', 'BANDIT N-600/ 650', 'BOULEVARD C1500', 'BOULEVARD M1500',
             'BOULEVARD M1500R', 'BOULEVARD M1800R', 'BOULEVARD M1800R B.O.S.S.', 'BOULEVARD M800', 'BOULEVARD M800R',
             'BURGMAN 400', 'BURGMAN 650 EXECUTIVE/ 650', 'BURGMAN I 125CC', 'DL 1000 V-STROM', 'DL 1000 XT V-STROM',
             'DL 650 V-STROM', 'DL 650XT V-STROM', 'DR350', 'DR350 SE', 'DR650 RE', 'DR650 RSE', 'DR800 S', 'DR-Z400E',
             'EN125 YES', 'EN125 YES CARGO', 'EN125 YES SE', 'FREEWIND XF 650', 'GLADIUS 650', 'GS 120', 'GS 500-E',
             'GSR 125', 'GSR 125S', 'GSR 150I', 'GSR 750', 'GSX  650F', 'GSX 1100 F', 'GSX 1250 F', 'GSX 1300 B-KING',
             'GSX 1300-R HAYABUSA', 'GSX 750 F', 'GSX-R 1000', 'GSX-R 1100 W', 'GSX-R 750 W', 'GSX-R 750 W SRAD',
             'GSX-S 1000', 'GSX-S 1000 F', 'GSX-S 750', 'INAZUMA 250CC', 'INTRUDER 125', 'INTRUDER 250', 'INTRUDER LC 1500',
             'INTRUDER VS 1400-GLP', 'INTRUDER VS 800-GLP/ 800-GL', 'KATANA 125', 'LETS II 50CC', 'LT 50 QUADRICICLO',
             'LT 80 QUADRICICLO', 'LT F160 QUADRICICLO', 'MARAUDER 800', 'RF 600 R', 'RF 900 R', 'RM 125', 'RM 250',
             'RM 80', 'RMX 250', 'SAVAGE LS 650', 'SV650', 'TL 1000 S', 'VX 800CC']]

        if self.marca.upper() in str(motos):
            veiculo = 'motos'
            if self.marca.upper() == 'HONDA':
                if self.modelo.upper() in str(moto_modelo_honda[0]):
                    veiculo = 'motos'
                else:
                    veiculo = 'carros'
            if self.marca.upper() == 'BMW':
                if self.modelo.upper() in str(moto_modelo_bmw[0]):
                    veiculo = 'motos'
                else:
                    veiculo = 'carros'
            if self.marca.upper() == 'SUZUKI':
                if self.modelo.upper() in str(moto_modelo_suzuki[0]):
                    veiculo = 'motos'
                else:
                    veiculo = 'carros'
        else:
            veiculo = 'carros'

        return veiculo