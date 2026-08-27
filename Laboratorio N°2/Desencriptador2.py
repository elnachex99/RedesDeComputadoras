from pathlib import Path


ARCHIVO = "frames.bin"


def bytes_a_hex(datos):
    """Convierte bytes a hexadecimal."""
    return " ".join(f"{byte:02X}" for byte in datos)


def bytes_a_ascii(datos):
    """Convierte bytes a ASCII."""
    return "".join(
        chr(byte) if 32 <= byte <= 126 else "."
        for byte in datos
    )


def obtener_group(nombre):
    """
    GROUP = primeros 5 caracteres del nombre del grupo 
    (respeta mayúsculas/minúsculas para casos especiales).
    """
    nombre = nombre.strip()

    if len(nombre) < 5:
        raise ValueError(
            "El nombre del grupo debe tener al menos 5 caracteres."
        )

    group = nombre[:5]

    return group.encode("ascii")


def buscar_paquetes(datos, group):
    """
    Busca paquetes con la estructura:

    GROUP   = 5 bytes
    SEQ     = 1 byte
    LENGTH  = 1 byte
    PAYLOAD = LENGTH bytes
    """

    paquetes = []
    posicion = 0

    while posicion <= len(datos) - 7:

        # Buscar GROUP
        if datos[posicion:posicion + 5] != group:
            posicion += 1
            continue

        offset = posicion

        # Verificar que existan SEQ y LENGTH
        if posicion + 7 > len(datos):
            break

        seq = datos[posicion + 5]
        length = datos[posicion + 6]

        inicio_payload = posicion + 7
        fin_payload = inicio_payload + length

        # Verificar que el payload exista completo
        if fin_payload > len(datos):
            print()
            print("ADVERTENCIA:")
            print(
                f"Se encontró GROUP en offset {offset}, "
                "pero el PAYLOAD está incompleto."
            )
            posicion += 1
            continue

        payload = datos[inicio_payload:fin_payload]

        paquete = {
            "offset": offset,
            "seq": seq,
            "length": length,
            "payload": payload
        }

        paquetes.append(paquete)

        # Avanzar después de la trama
        posicion = fin_payload

    return paquetes


def mostrar_paquetes(paquetes, group):
    """Muestra los paquetes encontrados."""

    print()
    print("=" * 90)
    print("PAQUETES ENCONTRADOS")
    print("=" * 90)

    print(f"GROUP: {group.decode('ascii')}")
    print(f"HEX:   {bytes_a_hex(group)}")
    print()

    for numero, paquete in enumerate(paquetes, start=1):

        print(f"Paquete #{numero}")
        print("-" * 50)

        print(f"Offset:       {paquete['offset']}")
        print(f"Offset HEX:   0x{paquete['offset']:04X}")

        print(f"GROUP:        {group.decode('ascii')}")
        print(f"SEQ:          {paquete['seq']}")
        print(f"LENGTH:       {paquete['length']}")

        print(
            f"PAYLOAD HEX:   "
            f"{bytes_a_hex(paquete['payload'])}"
        )

        print(
            f"PAYLOAD ASCII: "
            f"{bytes_a_ascii(paquete['payload'])}"
        )

        print()


def reconstruir(paquetes):
    """
    Ordena los paquetes por SEQ
    y concatena los PAYLOAD.
    """

    ordenados = sorted(
        paquetes,
        key=lambda paquete: paquete["seq"]
    )

    mensaje = b""

    for paquete in ordenados:
        mensaje += paquete["payload"]

    return ordenados, mensaje


def mostrar_resultado_final(ordenados, mensaje):

    print()
    print("=" * 90)
    print("PAQUETES ORDENADOS POR SEQ")
    print("=" * 90)

    for paquete in ordenados:

        print(
            f"SEQ={paquete['seq']:3d} | "
            f"LENGTH={paquete['length']:3d} | "
            f"PAYLOAD={bytes_a_ascii(paquete['payload'])}"
        )

    print()
    print("=" * 90)
    print("INFORMACIÓN FINAL RECONSTRUIDA")
    print("=" * 90)
    print()

    try:
        texto = mensaje.decode("ascii")
    except UnicodeDecodeError:
        texto = mensaje.decode("ascii", errors="replace")

    print(texto)
    print()
    print("HEX:")
    print(bytes_a_hex(mensaje))


def main():

    print("=" * 90)
    print("             ANALIZADOR DE frames.bin")
    print("=" * 90)

    ruta = Path(ARCHIVO)

    if not ruta.exists():
        print()
        print(f"ERROR: No se encontró '{ARCHIVO}'.")
        print()
        print("Asegurate de tener:")
        print()
        print("    carpeta/")
        print("    ├── analizador.py")
        print("    └── frames.bin")
        print()
        return

    datos = ruta.read_bytes()

    print()
    print(f"Archivo: {ARCHIVO}")
    print(f"Tamaño: {len(datos)} bytes")

    print()
    nombre = input(
        "Ingrese el nombre completo del grupo: "
    )

    try:
        group = obtener_group(nombre)
    except ValueError as error:
        print()
        print(f"ERROR: {error}")
        return
    except UnicodeEncodeError:
        print()
        print(
            "ERROR: El nombre contiene caracteres "
            "que no pueden representarse en ASCII."
        )
        return

    print()
    print("=" * 90)
    print("IDENTIFICACIÓN DEL GRUPO")
    print("=" * 90)

    print(f"Nombre ingresado: {nombre}")
    print(f"Primeros 5 caracteres: {nombre[:5]}")
    print(
        f"GROUP hexadecimal: "
        f"{bytes_a_hex(group)}"
    )

    paquetes = buscar_paquetes(datos, group)

    if not paquetes:
        print()
        print("=" * 90)
        print("RESULTADO")
        print("=" * 90)
        print()
        print(
            f"No se encontraron paquetes válidos "
            f"para el grupo '{nombre}'."
        )
        print(
            f"GROUP buscado: "
            f"{group.decode('ascii')}"
        )
        return

    print()
    print("=" * 90)
    print("RESULTADO")
    print("=" * 90)
    print()
    print(
        f"Se encontraron {len(paquetes)} "
        f"paquetes válidos."
    )

    mostrar_paquetes(paquetes, group)

    ordenados, mensaje = reconstruir(paquetes)

    mostrar_resultado_final(
        ordenados,
        mensaje
    )


if __name__ == "__main__":
    main()