# Parcial Hecho por: Juan David Marceles - Sharon Orozco - Amir Manotas

import pandas as pd

info = pd.read_csv('resultados.csv')

promedioNacional = info['PUNT_MATEMATICAS'].mean()
Barranquilla = info[info['ESTU_MCPIO_RESIDE'] == 'BARRANQUILLA']
promedioBarranquilla = Barranquilla['PUNT_MATEMATICAS'].mean()
oficiales = info[info['COLE_NATURALEZA'] == 'OFICIAL']
promedioOficiales = oficiales['PUNT_MATEMATICAS'].mean()
noOficiales = info[info['COLE_NATURALEZA'] == 'NO OFICIAL']
promedioNoOficial = noOficiales['PUNT_MATEMATICAS'].mean()

primerResultado = None
segundoResultado = None

if promedioBarranquilla > promedioNacional:
    primerResultado = (promedioBarranquilla, "LOCAL")
elif promedioNacional > promedioBarranquilla:
    primerResultado = (promedioNacional, "NACIONAL")
else:
    primerResultado = "No se encontro ninguno de los 2 promedios"

if promedioOficiales > promedioNoOficial:
    segundoResultado = (promedioOficiales, "OFICIAL")
elif promedioNoOficial > promedioOficiales:
    segundoResultado = (promedioNoOficial, "NO OFICIAL")
else:
    segundoResultado = "No se encontro ninguno de los 2 promedios"

dicc = {'nacional_math': promedioNacional,
        'performance_math': primerResultado, 'mejor_resultado': segundoResultado}
print(dicc)
