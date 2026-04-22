# GA1-220501093-04-AA1-EV01 - Fundamentos de Python

Este repositorio contiene la solucion de los laboratorios de Fundamentos de Python (secciones 1 a 4), incluyendo ejercicios de:

- Funcion `print()` y formato de salida.
- Literales de cadena y caracteres de escape.
- Operadores aritmeticos y prioridad de operaciones.
- Variables, expresiones y conversiones.

## Estructura del proyecto

```
fundamentos_python/
├── README.md
├── operadores.md
├── src/
│   └── puntaje_final_jugador.py
├── seccion1/
│   ├── lab.py
│   ├── lab1_trabajando_con_print.py
│   ├── lab2_print_sep_end.py
│   └── lab3_formato_salida.py
├── seccion2/
│   └── lab1_literales_cadenas.py
├── seccion3/
│   └── lab1_operadores_matematicos.py
└── seccion4/
    ├── lab0_variables.py
    ├── lab1_convertidor_simple.py
    ├── lab2_operadores_expresiones.py
    └── lab3_ejercicios_algoritmos.py
```

## Solucion de ejercicios de operadores matematicos

La logica aplicada en todos los ejercicios es:

1. Resolver parentesis.
2. Resolver potencias.
3. Resolver multiplicacion, division y modulo.
4. Resolver suma y resta.

Resultados finales:

1. `5 + 3 * 2 = 11`
2. `8 / 2 + 4 * 3 = 16.0`
3. `(7 + 3) * 2 - 5 = 15`
4. `10 - 4 + 2 * 3 = 12`
5. `(10 / 2) * (3 + 2) - 4 = 21.0`
6. `2 + 3 * (4 - 1) = 11`
7. `5 * 2 ** 3 = 40`
8. `6 + 4 / 2 ** 2 = 7.0`
9. `10 % 3 + 2 * 5 = 11`
10. `(8 + 2) * 3 ** 2 = 90`
11. `7 + 2 * (3 + 5) / 4 = 11.0`
12. `2 ** 3 * 4 / 2 = 16.0`
13. `9 - 6 + 3 ** 2 = 12`
14. `(7 - 2) * 5 + 3 ** 2 = 34`
15. `4 * 2 ** 3 / 8 + 1 = 5.0`

El desarrollo paso a paso de cada ejercicio esta documentado en `operadores.md`.

## Como ejecutar los programas

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta cualquier script con:

```bash
python ruta/del/archivo.py
```

Ejemplos:

```bash
python seccion1/lab2_print_sep_end.py
python seccion4/lab1_convertidor_simple.py
python src/puntaje_final_jugador.py
```

## Ejemplos de salida

### Seccion 1 - LAB print con `sep` y `end`

Comando:

```bash
python seccion1/lab2_print_sep_end.py
```

Salida:

```text
Programming***Essentials***in...Python
```

### Seccion 4 - LAB convertidor simple

Comando:

```bash
python seccion4/lab1_convertidor_simple.py
```

Salida:

```text
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
```

## Evidencia de aprendizaje

- Cada laboratorio tiene su script correspondiente por seccion.
- Los ejercicios de operadores estan documentados en este `README.md` y ampliados en `operadores.md`.
- Se incluye un script adicional en `src/puntaje_final_jugador.py` para la estructura solicitada.
