# conversor/conversor_moeda.py (converte entre Real e Dólar)
class conversorMoeda:
    def __init__(self, cotacao=5.0):
        self.cotacao = cotacao  # valor padrão, pode ser alterado

    def real_para_dolar(self, valor):
        return valor / self.cotacao

    def dolar_para_real(self, valor):
        return valor * self.cotacao