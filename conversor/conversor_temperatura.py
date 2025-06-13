# conversor/conversor_temperatura.py (converte entre Celsius e Fahrenheit)
class conversorTemperatura:
    def celsius_para_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_para_celsius(self, f):
        return (f - 32) * 5/9
    
