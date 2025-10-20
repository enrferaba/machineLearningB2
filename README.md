# Machine Learning B2

Este repositorio contiene un cuaderno muy sencillo que sigue la teoría básica del temario "Machine Learning 1" (nivel B2). Todo está escrito en inglés desde el punto de vista de una persona novata para que los pasos sean fáciles de replicar.

## Contenido principal

### Ejercicio B2 con `train.csv`

- `Machine Learning 1/b2/train.csv`: subconjunto sintético del dataset de Kaggle *Music Genre Classification* (`train.csv`) con las mismas columnas numéricas (`danceability`, `energy`, `loudness`, etc.), generado con semilla 90 para mantener la práctica autocontenida.
- `Machine Learning 1/b2/b2_python.ipynb`: cuaderno principal que desarrolla el boletín oficial siguiendo estas ideas:
  1. Carga del CSV, chequeos de filas reales, valores ausentes y distribución de géneros.
  2. Preparación de dos vistas del dataset (regresión para `popularity` y clasificación para `genre`) y estandarización solo sobre el conjunto de entrenamiento.
  3. Implementación desde cero de los modelos ZeroR, OneR (con discretización en bins) y k-NN para k = 3, 5 y 10, respetando la semilla 90.
  4. Comparativa con hold-out 75/25, diez repetidos hold-out, validación cruzada de 5 pliegues, métricas completas (MAE, MSE, RMSE, R², accuracy, kappa, precision/recall/F1) y matrices de confusión con filas = predicciones.
  5. Obtención de la regla final de OneR usando todo el dataset y resolución del ejercicio extra de k-NN manual (k = 2 y k = 5) indicado en el PDF.

## Requisitos

- Python 3. No se necesitan librerías externas porque todo el código usa únicamente funciones de la librería estándar.

## Cómo ejecutar el cuaderno

1. Abre `Machine Learning 1/b2/b2_python.ipynb` con Jupyter.
2. Ejecuta cada celda en orden. El cuaderno busca automáticamente `Machine Learning 1/b2/train.csv` en la misma carpeta o desde el directorio raíz.
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
│   └── train.csv              Subconjunto autocontenido del dataset musical.
README.md                      Este archivo descriptivo.
tests/run_notebook.py          Script que comprueba el cuaderno.
```

Este material está pensado como punto de partida directo para el boletín B2 usando el dataset `train.csv` indicado en la práctica.
