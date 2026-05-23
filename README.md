# 🔄 Conversor de Unidades en Python

Proyecto desarrollado como un módulo de código libre para la conversión de unidades de **temperatura** y **distancia**, pensado especialmente para uso académico (profesores y estudiantes de física).

---

## 📌 Información General

- **Proyecto:** Conversor de Unidades  
- **Lenguaje:** Python  
- **Repositorio:** https://github.com/clbastidasbolanos-pixel/Conversor-Fisica-python  
- **Licencia:** MIT  

---

## ⚙️ Requisitos

Para ejecutar este proyecto necesitas:

- Python **3.10 o superior**
- No requiere librerías externas

---

## ▶️ Ejecución del Programa

El archivo principal es `convertidor_uni.py`

Para ejecutarlo, usa el siguiente comando en la terminal:

```bash
python convertidor_uni.py
```

---

## 🔁 Funcionamiento del Sistema

El programa funciona de forma interactiva a través de la consola, solicitando información al usuario paso a paso:

```mermaid
flowchart TD
    A([Inicio]) --> B[Mostrar: Conversor de Unidades]
    B --> C[Pedir tipo_medida: temp o dist]
    C --> D[Pedir valor_origen]
    D --> E{Es numero valido?}
    E -- No --> F[ALERTA: Valor invalido]
    F --> C
    E -- Si --> G[Pedir unidad_destino: C/F o KM/MI]
    G --> H{tipo_medida?}
    H -- temp --> I{unidad_destino?}
    I -- F --> J[Convertir C a F]
    I -- C --> K[Convertir F a C]
    I -- otro --> L[ALERTA: Unidad no reconocida]
    L --> C
    H -- dist --> M{unidad_destino?}
    M -- MI --> N[Convertir KM a MI]
    M -- KM --> O[Convertir MI a KM]
    M -- otro --> P[ALERTA: Unidad no reconocida]
    P --> C
    H -- otro --> Q[ALERTA: Tipo no reconocido]
    Q --> C
    J & K & N & O --> R[Mostrar resultado]
    R --> S{Otra conversion? s/n}
    S -- s --> C
    S -- n --> T([Fin])
```

| Paso | Entrada            | Descripción |
|------|------------------|------------|
| 1    | `tipo_medida`     | Tipo de conversión: `temp` o `dist` |
| 2    | `valor_origen`    | Valor numérico que se desea convertir |
| 3    | `unidad_destino`  | Unidad final según el tipo seleccionado |

---

## 🌡️ Opciones de Conversión

### Temperatura (`temp`)
- `C` → Celsius  
- `F` → Fahrenheit  

### Distancia (`dist`)
- `KM` → Kilómetros  
- `MI` → Millas  

---

## ✅ Ejemplo de Uso

```bash
tipo_medida: temp
valor_origen: 100
unidad_destino: F
```

**Salida:**

```bash
Resultado: 100.00 C equivalen a 212.00 F
```

---

## ⚠️ Manejo de Errores

1. El sistema valida las unidades ingresadas.
2. Si el usuario introduce una unidad no válida, se mostrará:

```bash
[ALERTA] Unidad no reconocida. Usa solo C, F, KM o MI.
```

---

## 🔧 Configuración Avanzada

El número de decimales mostrados puede modificarse directamente en el código:

```python
DECIMALES_MOSTRADOS = 2
```

Puedes cambiarlo para mayor precisión, por ejemplo:

```python
DECIMALES_MOSTRADOS = 4
```

---

## 📂 Estructura del Proyecto

```
ConversorFisicaPython
 ┣ convertidor_uni.py
 ┗ README.md
```

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica académica en programación con Python.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**, lo que permite su uso, modificación y distribución libre.

---

## 💡 Notas Finales

- Proyecto ligero y fácil de usar.
- Ideal para aprendizaje de estructuras básicas en Python.
- No depende de librerías externas.
## Desarrolladores 

- EDWIN ESTEBAN ESCOBAR NACAVERA
- CLAUDIA LORENA BASTIDAS BOLAÑOS
- EMILIA QUINTERO LONDOÑO