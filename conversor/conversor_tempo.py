# conversor.conversor_tempo.py (converte entre segundos, minutos, horas e dias)
class conversorTempo:
    def segundos_para_minutos(self, segundos):
        minutos = int(segundos // 60)
        segundos_restantes = int(segundos % 60)
        return f"{minutos}:{segundos_restantes:02d}"

    def minutos_para_segundos(self, minutos):
        return minutos * 60