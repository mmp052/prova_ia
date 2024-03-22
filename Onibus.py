from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from aigyminsper.search.SearchAlgorithms import BuscaGananciosa
from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State

class Onibus(State):
    def __init__(self, op: str, cidade_atual: str, km: int, cidade_meta: str, tranportando_carga: bool, passar_estrategica: bool, carga: bool, estrategica: bool):
        if op == "":
            self.operator = f"sair de {cidade_atual}"
        else:
            self.operator = op
        self.cidade_atual = cidade_atual
        self.km = km
        self.cidade_meta = cidade_meta
        self.transportando_carga = tranportando_carga
        self.carga = carga
        self.passar_estrategica = passar_estrategica
        self.estrategica = estrategica
        self.mapa = {
        'São Paulo': [[(104, 'Sorocaba'), (59, 'Jundiaí'), (72, 'Santos'), (92, 'São José dos Campos')], [False, False]],
        'Taubaté':[[(43,'São José dos Campos'),(97,'Ubatuba')], [False, False]],
        'São José dos Campos':[[(43,'Taubaté'),(139,'Ubatuba'),(92,'São Paulo')], [False, False]],
        'Ubatuba':[[(97,'Taubaté'),(139,'São José dos Campos'),(238,'Santos')], [True, False]],
        'Santos':[[(238,'Ubatuba'),(72,'São Paulo')], [False, False]],
        'Sorocaba':[[(104,'São Paulo'),(89,'Campinas'),(93,'Jundiaí')], [False, True]],
        'Jundiaí':[[(59,'São Paulo'),(39,'Campinas'),(93,'Sorocaba')], [False, False]],
        'Campinas':[[(89,'Sorocaba'),(39,'Jundiaí'),(142,'São Carlos'),(70,'Piracicaba'),(59,'Limeira')], [False, False]],
        'São Carlos':[[(142,'Campinas'),(62,'Rio Claro'),(152,'Bauru')], [True, False]],
        'Limeira':[[(59,'Campinas'),(28,'Rio Claro')], [False, True]],
        'Rio Claro':[[(62,'São Carlos'),(28,'Limeira'),(186,'Bauru')], [False, False]],
        'Bauru':[[(152,'São Carlos'),(186,'Rio Claro'),(194,'Piracicaba')], [False, False]],
        'Piracicaba':[[(70,'Campinas'),(194,'Bauru')], [False, False]]
        }


    def successors(self):
        successors = []

        for cidade in self.mapa[self.cidade_atual][0]:
            if  self.mapa[self.cidade_atual][1][0]:
                self.estrategica = True
            if self.mapa[self.cidade_atual][1][1]:
                self.carga = True
            successors.append(Onibus(f"ir para {cidade[1]}", cidade[1], cidade[0], self.cidade_meta, self.transportando_carga, self.passar_estrategica, self.carga, self.estrategica))
        
        return successors
    
    def is_goal(self):
        if self.passar_estrategica and self.transportando_carga:
            return self.estrategica and self.carga and self.cidade_atual == self.cidade_meta
        else:
            if self.transportando_carga:
                return self.carga and self.cidade_atual == self.cidade_meta
            elif self.passar_estrategica:
                return self.estrategica and self.cidade_atual == self.cidade_meta
            else:
                return self.cidade_atual == self.cidade_meta
    
    def description(self):
        return "resposta do exe do onibus"
    
    def cost(self):
        return 0.5 * self.km
    
    def print(self):
        return str(self.operator)
    
    def env(self):
        return f"{self.cidade_atual} {self.carga} {self.estrategica}"
    
def main():
    state = Onibus("", "Taubaté", 0, "Campinas", False, False, False, False)
    algoritimo = BuscaCustoUniforme()
    result = algoritimo.search(state, trace=True)
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print("não achou solução")

main()

