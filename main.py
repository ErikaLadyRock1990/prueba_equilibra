import os
import pandas as pd

print("\nCARGA DE FICHERO")
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, "datos_prueba_tecnica.csv")

data_frame = pd.read_csv(ruta_archivo, delimiter=";")

print("\nEJERCICIO 1")
hombres = data_frame[data_frame["sexo"] == "H"]
mujeres = data_frame[data_frame["sexo"] == "M"]

print("Total de hombres:", hombres.shape[0])
print("Total de mujeres:", mujeres.shape[0])

print("\nEJERCICIO 2")
trabajadores_alovera = data_frame[data_frame["ID Centro trabajo"] == "CT2"]
suma_salario_bruto = trabajadores_alovera["salario bruto anual"]
print("Salario anual total de los trabajadores de Alovera:", suma_salario_bruto.sum())

print("\nEJERCICIO 3")
trabajadores_rrhh = data_frame[data_frame["Nombre empresa"] == "Equilibrha RRHH"]
trabajadores_mayor_salario = trabajadores_rrhh[
    trabajadores_rrhh["salario bruto anual"] > 28000
]
trabajadores_mayor_salario = trabajadores_mayor_salario[
    [
        "id empleado",
        "nombre",
        "apellido1",
        "apellido2",
        "salario bruto anual",
        "Nombre empresa",
    ]
]
print("LISTADO")
print(trabajadores_mayor_salario)
