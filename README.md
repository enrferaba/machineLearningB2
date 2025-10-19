# Machine Learning B2

Este repositorio contiene un cuaderno muy sencillo que sigue la teoría básica del temario "Machine Learning 1" (nivel B2). Todo está escrito en inglés desde el punto de vista de una persona novata para que los pasos sean fáciles de replicar.

## Contenido principal

### Ejercicio B2 con `train.csv`

- `Machine Learning 1/b2/train.csv`: extracto del fichero Titanic `train.csv` que usamos en clase para practicar clasificación binaria.
- `Machine Learning 1/b2/b2_python.ipynb`: cuaderno principal que desarrolla el boletín siguiendo estas ideas:
  1. Carga del CSV, chequeos de filas reales y revisión de valores ausentes.
  2. Preparación de características básicas (edad, familiares, tarifa, clase, puerto y sexo) con imputación sencilla y estandarización.
  3. Implementación desde cero de los modelos ZeroR, OneR y k-NN (k = 3) respetando la semilla 90.
  4. Comparativa con hold-out, matriz de confusión (filas = predicciones, columnas = valores reales) y repetición del hold-out en cinco barajados.
  5. Validación cruzada manual de 3 pliegues, obtención de la regla final de OneR y ejemplo manual de k-NN.

## Requisitos

- Python 3. No se necesitan librerías externas porque todo el código usa únicamente funciones de la librería estándar.

## Cómo ejecutar el cuaderno

1. Abre `Machine Learning 1/b2/b2_python.ipynb` con Jupyter.
2. Ejecuta cada celda en orden. El cuaderno busca automáticamente `Machine Learning 1/b2/train.csv` en la misma carpeta.
3. Sigue los textos en inglés para relacionar cada paso con la teoría del temario.

## Comprobación rápida

Incluimos un pequeño script para ejecutar el cuaderno de principio a fin y asegurarnos de que no falla ninguna celda:

```bash
python tests/run_notebook.py
```

El script carga el fichero indicado (por defecto `Machine Learning 1/b2/b2_python.ipynb`) y lanza una excepción si encuentra algún error. Si todo va bien mostrará un mensaje de confirmación.

## Estructura del repositorio

```
Machine Learning 1/            Documentación original del curso y el nuevo material práctico.
├── 1. Introduccion.pdf        Apuntes proporcionados por el profesor.
├── 2. Modelos de negocio...   Segundo documento del temario.
├── B2_python.pdf              Boletín oficial a seguir.
├── b2/                       Carpeta del boletín B2.
│   ├── b2_python.ipynb        Cuaderno con el desarrollo paso a paso.
│   └── train.csv              Extracto del dataset Titanic.
README.md                      Este archivo descriptivo.
tests/run_notebook.py          Script que comprueba el cuaderno.
```

Este material está pensado como punto de partida directo para el boletín B2 usando el mismo dataset `train.csv` que indicó el profesor.
