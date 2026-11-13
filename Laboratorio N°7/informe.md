# Trabajo Práctico N°7: Captura, de-codificación y recuperación de datos

> Asignatura: Redes de Computadoras - Universidad Nacional de Córdoba (FCEFyN)
> 
> Integrantes (WAN-DIRECTION):
> * Baigorria, Ramiro Javier
> * Urrestarazu, Juan Ignacio
> * Mena, Franco Grabiel
> * Herrera, Mauricio Agustin
> * Ciruzzi, Martina
> * Montes, Franco Leonel
> * Valla Tello, Desiderio Jesus
 
> Profesor: Santiago Martin Henn
> * Santiago Martin Henn

## Configuraciones Generales
* **IP y Máscara:** 192.168.8.189/255.255.255.0
* **Broadcast (IP y MAC):** 
  * **IP de broadcast calculada:** `192.168.8.255`. 
  * **MAC de broadcast:** `ff:ff:ff:ff:ff:ff`. Verificado en la capa de enlace Ethernet II de la misma captura.

## Estructura y formato del mensaje
**Datos de origen y transmisión:**
 * **Protocolo de transporte:** UDP
 * **IP de origen:** 192.168.8.150
 * **Puerto de origen:** 64385


**Formato del mensaje:** Utiliza *JSON* caracterizado por estructurar la información en pares de clave-valor encerrados entre {}
* **Campos y representación:**
  * `"SIZE"`: Indica las dimensiones (filas y columnas) que tendrá la matriz de datos.
  * `"PL"` (Payload): Representa la carga útil, es decir, los unos y ceros que conforman los datos que llenarán la matriz.
  * `"CHECK"`: Contiene los bits de control (paridad bidimensional) enviados por el transmisor para detectar y ubicar los posibles errores.
* **Interpretación de los datos:** Para poder decodificar el mensaje se debe leer el tamaño de la matriz es decir filas x columnas, de esa forma solo se saca la cantidad de bits indicada del PL organizándolas secuencialmente hasta completar la matriz llenándola de a filas y luego las del check
* filas+columnas, teniendo en cuenta que los primeros bits serán los de las filas, de arriba hacia abajo y los demás de las columnas, de izquierda a derecha.

## Tercera Trama
**Captura con Wireshark**

![Captura](evidenciasTercerReto/capturaTrama3.png)

### Interpretación de la dimensión de la matriz
*La matriz indicada era de "4,4" pero el PL era de **112 bits** y el 'CHECK' **32 bits** Si la matriz fuera de 4×4 bits (16 bits), no alcanzarían ni los datos ni los bits de control. 

La lectura consistente es que `SIZE` cuenta **caracteres de 7 bits**: una matriz de 4×4 caracteres, es decir, **4 filas × 28 columnas de bits**.

$$
\frac{112}{28} = 4 filas
$$

La verificación con `CHECK` también cierra: 4 bits de paridad de filas + 28 de columnas = **32 bits**. Es la única forma de que coincidan, ya que R × C = 112 y R + C = 32 solo tienen solución con 4 y 28.

### Verificación de la paridad (síndrome)

Se calcularon las paridades y se compararon con las de `CHECK`:
* **Filas que fallan:** 1, 2, 3 y 4
* **Columnas que fallan:** 7, 11, 15 y 20

![Check](evidenciasTercerReto/CheckTrama3.png)

Este método de la paridad bidimensional es útil para reconstruir un mensaje con un bit fallado; con más de uno se podría saber qué falló mas no cuál es para corregirlo.

## Decodificación sin corregir
Como la paridad no ayudó para corregirlo, se decodificó tal cual para ver si el contexto ayudaba

![DecoSinCorregir](evidenciasTercerReto/decoSinCorregir.png)

Resultado: Qr3mi8!:)1p-dIgZ se puede intuir que el mensaje original era Pr3mi0!:)10-dIeZ

### Corrección 
Se modificaron los bits correspondientes a esta interpretación y se recalculó su paridad:

![Matriz de paridad calculada y corregida](evidenciasTercerReto/paridadCalculaCorregida.png)

### Comprobación
Se comprobó que el check coincide con la nueva paridad

![Comprobación](evidenciasTercerReto/checkYaCorregido.png)

### Resultado
![Resultado](evidenciasTercerReto/decoCorregida.png)

> **`Pr3mi0!:)10-dIeZ`**

## Segunda Trama

**Captura en Wireshark**

![CapturaTrama2](evidenciasSegundoReto/CapturaTrama2.jpeg)

### Interpretación de la dimensión de la matriz

Las dimensiones de la matriz son 10 filas por 6 columnas, con una `PL` de 420 bits y un `CHECK` de 52 bits. Teniendo estos datos y siguiendo la misma línea que para el 3er caso: 

$$
\frac{420 bits}{10 filas} = 42 bits/fila      
$$

entonces para 6 columnas, son : 

$$
\frac{42 bits}{6 columnas} = 7 bits/columna     
$$

y 42 + 10 = 52 que es la cantidad de bits del `CHECK`.

### Verificación de la paridad (síndrome)

Se armó la matriz, se calculó la paridad y se comparó con  el `CHECK`
* **Filas que fallan:** 1, 5, 6 y 8
* **Columnas que fallan:** 3, 12, 18 y 25

![sindrome](evidenciasSegundoReto/CheckYparidadSinCorregir.png)

Lo que dio varios bits erróneos lo que no permite corregirlos usando la paridad. 

### Decodificación sin corrección

Decodificamos la trama para ver si el contexto ayudaba y obtuvimos:

xttps://youtube.com/shortw/WCi5h}1EqqI?featurm=share  

Un link a youtube, que a simple vista estaba mal en su formato, por lo que buscamos en la trama y corregimos:

* `x` -> `h`
* `w` -> `s`
* `}` -> `u`  una ID de youtube no puede llevar una llave
* `m` -> `e`

Luego de corregir x, w y m se buscó en la matriz el } y uno de sus bits coincidía en fila y columna con un error en la paridad por lo que se invirtió ese bit quedando en lugar de la llave una u

### Comprobación

![verificacion con correcciones](evidenciasSegundoReto/CheckyParidadCorregida.png)

Esta vez coincidiendo todos los bits.

### Resultado

Se decodificó y obtuvimos el link del short:

https://youtube.com/shorts/WCi5hu1EqqI?feature=share 


