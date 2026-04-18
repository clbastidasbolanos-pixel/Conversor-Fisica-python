# 🔄 Conversor de Unidades en Python

Proyecto desarrollado como un módulo de código libre para la conversión de unidades de **temperatura** y **distancia**, pensado especialmente para uso académico (profesores y estudiantes de física).

---

## 📌 Información General

- **Proyecto:** Conversor de Unidades  
- **Lenguaje:** Python  
- **Repositorio:** https://github.com/xxxxx/conversor-fisica-python.git  
- **Licencia:** MIT  

---

## ⚙️ Requisitos

Para ejecutar este proyecto necesitas:

- Python **3.10 o superior**
- No requiere librerías externas

---

## ▶️ Ejecución del Programa

El archivo principal es:

```bash
convertidor_uni.py
```

Para ejecutarlo, usa el siguiente comando en la terminal:

```bash
python convertidor_uni.py
```

---

## 🔁 Funcionamiento del Sistema

El programa funciona de forma interactiva a través de la consola, solicitando información al usuario paso a paso:

| Paso | Entrada            | Descripción |
|------|------------------|------------|
| 1    | `tipo_medida`     | Tipo de conversión: `temp` (temperatura) o `dist` (distancia) |
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
Resultado: 100.00 °C equivalen a 212.00 °F
```

---

## ⚠️ Manejo de Errores

El sistema valida las unidades ingresadas.

Si el usuario introduce una unidad no válida, se mostrará el siguiente mensaje:

```bash
[ALERTA] Unidad no reconocida. Usa solo C, F, KM o MI.
```

---

## 🔧 Configuración Avanzada

El número de decimales mostrados en los resultados puede ser modificado directamente en el código:

```python
DECIMALES_MOSTRADOS = 2
```

Puedes cambiar este valor, por ejemplo:

```python
DECIMALES_MOSTRADOS = 4
```

Esto es útil para obtener mayor precisión en contextos como laboratorios.

---

## 📂 Estructura del Proyecto

```bash
📁 conversor-fisica-python
 ┣ 📄 convertidor_uni.py
 ┗ 📄 README.md
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

---

✨ *Listo para ser usado, modificado y mejorado.*