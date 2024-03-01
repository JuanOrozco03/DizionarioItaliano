from PyMultiDictionary import MultiDictionary
import random

dictionary = MultiDictionary()  

class dizionario:
    def __init__(self, parole):
        parole_correta = parole.partition("\n")
        self.lingua= 'it'
        self.parole= parole_correta[0]
        self.definizione = ""
        self.sinonimi = []
        self.traduzione = ""
        
    def trovare_definizioni(self):
        ricerca = dictionary.meaning(self.lingua, self.parole)
        definizione_it = ricerca[1].partition('La prima definizione')
        self.definizione = definizione_it[1]+definizione_it[2]
        
    
    def trovare_sinonimi(self):
        self.sinonimi = dictionary.synonym(self.lingua, self.parole)
        
    def traduzione_spagnolo(self):
        ricerca = dictionary.translate(self.lingua, self.parole)
        for trovare in ricerca:
            if trovare[0] == 'es':
                self.traduzione = "La traduzione al spagnolo è: {}".format(trovare[1])

class execute_dizionario:
    
    def chiamata_parole():
        listaParole = open("utils/risorse/paroleItaliane/paroleitaliane/1000_parole_italiane_comuni.txt", "r", encoding="utf8")
        posizione = 0
        parametro = random.randrange(1000)
        for parole in listaParole.readlines():
            if posizione == parametro:
                dizzionario = dizionario(parole)
                dizzionario.trovare_definizioni()
                dizzionario.trovare_sinonimi()
                dizzionario.traduzione_spagnolo()
                risposta = {
                    "Parole": dizzionario.parole,
                    "Definizione": dizzionario.definizione,
                    "Sinonimi": dizzionario.sinonimi,
                    "Traduzione": dizzionario.traduzione,
                }
                return risposta
                
            posizione+=1
    
    