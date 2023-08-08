
### Control de Estructura (*contención*)

|  <!-- -->   | **List** | **Tuple** | **FrozenSet** | **Set** | **Dictionary** |
|:-----------:|:--------:|:---------:|:-------------:|:-------:|:--------------:|
|    Lista    |    x     |     x     |       x       |    x    |       x        |
|    Tuple    |    x     |     x     |       x       |    x    |       x        |
|  Frozenset  |          |           |               |         |                |
|     Set     |    -     |     x     |       x       |    -    |       -        |
| Diccionario |          |           |               |         |                |

### Control de Estructura (*Ordenamiento, Mutabilidad, Duplicidad*)

| <!-- -->  | **List** | **Tuple** | **FrozenSet** | **Set** | **Dictionary** |
|:---------:|:--------:|:---------:|:-------------:|:-------:|:--------------:|
|  Ordered  |    x     |     x     |       -       |    -    |       -        |
|  Mutable  |    x     |     -     |       -       |    x    |       x        |
| Duplicity |    x     |     x     |       -       |    -    |       -        |
