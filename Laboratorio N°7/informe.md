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
> * [Tu Apellido], [Tu Nombre]
> 
> Profesor: Santiago Martin Henn
> * Santiago Martin Henn

## Configuraciones Generales
* **IP y Máscara:** 192.168.8.189/255.255.255.0
* **Broadcast (IP y MAC):** 
  * **IP de broadcast calculada:** `192.168.8.255`. 
  * **MAC de broadcast:** `ff:ff:ff:ff:ff:ff`. Verificado en la capa de enlace Ethernet II de la misma captura.

## Estructura y formato del mensaje
**Formato del mensaje:** Utiliza *JSON* caracterizado por estructurar la informacion en pares de clave-valor encerrados entre {}
* **Campos y representación:**
  * `"SIZE"`: Indica las dimensiones (filas y columnas) que tendrá la matriz de datos.
  * `"PL"` (Payload): Representa la carga útil, es decir, los unos y ceros que conforman los datos que llenarán la matriz.
  * `"CHECK"`: Contiene los bits de control (paridad bidimensional) enviados por el transmisor para detectar y ubicar los posibles errores.
* **Interpretación de los datos:** Para poder decodificar el mensaje se debe leer el tamaño de la matriz es decir filas x columnas, de esa forma solo se saca la cantiad de bits indicada del PL organizandolas secuencialmente hasta completar la matriz llenandola de a filas y luego las del check
* filas+columnas, teniendo en cuenta que los primero bits seran los de las filas, de arriba hacia abajo y los demas de las columnas, de izquierda a derecha.

##Trama1
