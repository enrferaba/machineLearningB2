# Machine Learning B2

Este repositorio contiene un cuaderno sencillo que sigue la teoría básica del temario "Machine Learning 1" (nivel B2). El objetivo es practicar un flujo completo de aprendizaje supervisado con explicaciones en inglés escritas desde el punto de vista de una persona principiante.

## Contenido principal

- `B2/b2_first_steps.ipynb`: cuaderno Jupyter (formato `.ipynb`) donde, paso a paso, se muestra cómo:
  1. Registrar un pequeño conjunto de datos tipo Iris dentro del propio cuaderno.
  2. Calcular estadísticas descriptivas básicas (mínimo, máximo y media) para cada característica.
  3. Separar las muestras en entrenamiento y prueba para evaluar honestamente.
  4. Implementar un clasificador k-vecinos más cercanos (k-NN) solo con Python estándar.
  5. Medir la exactitud y hacer una predicción manual de ejemplo.

El tono de los comentarios es el de un estudiante novato que explica cada decisión con palabras sencillas.

## Requisitos

- Python 3. No se necesitan librerías externas porque los cálculos se resuelven con funciones básicas del lenguaje.

## Cómo ejecutar el cuaderno

1. Abre el archivo `B2/b2_first_steps.ipynb` en Jupyter Notebook, JupyterLab o Visual Studio Code con soporte para notebooks.
2. Ejecuta las celdas en orden para seguir todo el flujo. No hace falta descargar datasets ni instalar dependencias adicionales.
3. Revisa las explicaciones para conectar cada paso con la teoría del temario.

## Comprobación rápida

Para verificar automáticamente que las celdas se ejecutan sin errores puedes usar el pequeño script incluido:

```bash
python tests/run_notebook.py
```

El script recorre cada celda de código y lanza una excepción si encuentra algún problema. En caso contrario mostrará el mensaje `Notebook executed successfully.`

## Estructura del repositorio

```
Machine Learning 1/        Documentación original del curso (PDF).
B2/                        Carpeta con el cuaderno práctico de nivel B2.
tests/                     Utilidades para comprobar el cuaderno.
README.md                  Este archivo con la explicación general.
```

Este material está pensado como punto de partida. Una vez comprendido el ejemplo, se puede profundizar repitiendo el proceso con datasets más amplios o probando otros algoritmos del temario.
