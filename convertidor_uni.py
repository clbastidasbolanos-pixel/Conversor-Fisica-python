import sys

# Configuración
DECIMALES_MOSTRADOS = 2

def main():
    print("--- Conversor de Unidades ---")
    while True:
        print("\n" + "-"*30)
        tipo_medida = input("Pregunta 1: tipo_medida (temp o dist): ").strip().lower()
        
        try:
            valor_origen = float(input("Pregunta 2: valor_origen: "))
        except ValueError:
            print("[ALERTA] Valor inválido. Debes ingresar un número.")
            continue

        unidad_destino = input("Pregunta 3: unidad_destino (C/F o KM/MI): ").strip().upper()

        resultado = 0
        unidad_origen = ""

        if tipo_medida == "temp":
            if unidad_destino == "F":
                resultado = (valor_origen * 9/5) + 32
                unidad_origen = "C"
            elif unidad_destino == "C":
                resultado = (valor_origen - 32) * 5/9
                unidad_origen = "F"
            else:
                print("[ALERTA] Unidad no reconocida. Usa solo C, F, KM o MI.")
                continue
        elif tipo_medida == "dist":
            if unidad_destino == "MI":
                resultado = valor_origen * 0.621371
                unidad_origen = "KM"
            elif unidad_destino == "KM":
                resultado = valor_origen / 0.621371
                unidad_origen = "MI"
            else:
                print("[ALERTA] Unidad no reconocida. Usa solo C, F, KM o MI.")
                continue
        else:
            print("[ALERTA] Tipo de medida no reconocido. Usa 'temp' o 'dist'.")
            continue

        print(f"\n> Resultado: {valor_origen:.{DECIMALES_MOSTRADOS}f} {unidad_origen} equivalen a {resultado:.{DECIMALES_MOSTRADOS}f} {unidad_destino}.")
        
        # Pregunta de control
        continuar = input("\n¿Deseas realizar otra conversión? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Nos vemos!")
            break

if __name__ == "__main__":
    main()