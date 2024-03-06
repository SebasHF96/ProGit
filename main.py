from datetime import datetime

tiempoActual  = datetime.now()

miCumple = datetime(2024,4,18)

tiempoFalta = miCumple-tiempoActual

print(tiempoFalta.days *60*60*24 + tiempoFalta.seconds)
