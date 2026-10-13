# Laboratorio 5

> **Asignatura:** Redes de Computadoras - Universidad Nacional de Córdoba (FCEFyN)
>
> **Integrantes:**
> - Baigorria, Ramiro Javier
> - Urrestarazu, Juan Ignacio 
> - Mena, Franco Grabiel 
> - Herrera, Mauricio Agustin
> - Ciruzzi, Martina
> - Montes, Franco Leonel 
> - Valla Tello, Desiderio Jesus 
>
> **Profesor:**
> - Santiago Martin Henn 

---

## Consigna 3
Hasta ahora observamos protocolos que usa el sistema operativo. Ahora vamos a *comunicar* dos procesos _(dos programas)_ sin escribir código todavía. ncat es un programa que toma lo que escribimos en el teclado y lo manda por la red _(y viceversa)_. La idea es empezar a generar tráfico cada vez más a bajo nivel _(primero generamos tráfico con Packet Tracer, luego con la terminal del SO, ahora con un software a través de la CLI y finalmente ejecutaremos algunos scripts)_.

## Consigna 3.a: ¿Qué significa "establecer una conexión"? ¿Dónde "existe" una conexión TCP: en los cables, en los routers o en los extremos?
**"Establecer una conexion"** significa realizar/iniciar una negociación previa o una comunicación lógica entre dos extremos para que puedan intercambiar datos. Antes de transmitir información, ambos extremos realizan un procedimiento de negociación llamado three-way handshake (establecimiento en tres pasos), mediante el intercambio de segmentos SYN, SYN-ACK y ACK
Una conexión TCP no existe físicamente en los cables ni requiere que los routers mantengan un estado propio de esa conexión. Existe principalmente en los extremos de la comunicación, es decir, en los equipos que ejecutan TCP. Allí se mantiene información sobre la conexión, como los números de secuencia, los números de confirmación y los parámetros de control.

_Los cables y routers transportan y encaminan los paquetes, pero TCP administra la conexión lógica entre los extremos_

## Consigna 3.b: ¿Qué es un puerto? ¿Qué identifica el par (IP, puerto)?
Un puerto es un número lógico utilizado por los protocolos de transporte TCP y UDP para identificar una aplicación o servicio dentro de un equipo. Por otro lado, la dirección IP identifica al equipo dentro de la red, el puerto permite distinguir a qué aplicación deben entregarse los datos.
El par (IP, puerto) identifica un punto de comunicación asociado a un equipo y a un servicio o aplicación.

## Consigna 3.c: ¿Qué significa que un proceso esté "escuchando" en un puerto?
Que un proceso esté escuchando en un puerto significa que una aplicación ha solicitado al sistema operativo que mantenga ese puerto disponible para recibir comunicaciones entrantes. En TCP, un servidor normalmente permanece escuchando hasta que llega una solicitud de conexión de un cliente. Entonces puede aceptar la conexión y comenzar a intercambiar datos.

_Escuchar en un puerto no significa que ya exista una conexión TCP establecida. Significa que el proceso está preparado para recibir solicitudes de conexión._

---

# Experimentos TCP y UDP

## Capturas iniciales del experimento 

- ***Mensaje enviado desde la terminal A:***

![Mensaje A](./Evidencias/Mensaje%20A.PNG)

- ***Mensaje enviado desde la terminal B:***

![Mensaje B](./Evidencias/Mensaje%20B.PNG)

- ***Captura del trafico usando WireShark:***

![Captura de trafico](./Evidencias/Captura%20de%20Trafico.PNG)

- ***Experimento UDP enviando un mensaje en cada sentido:***

![Conexion Previa](./Evidencias/Experimento%20mensaje%20en%20cada%20terminal.PNG)

## a) ¿Qué pasó en la red cuando ejecutaron el comando del cliente, antes de escribir el primer mensaje? Compárenlo con TCP

- ***Conexion previa de las terminales:***

![Conexion Previa](./Evidencias/Conexion%20Previa.PNG)

- ***Trafico Post Conexion UDP:***

![Trafico Post Conexion UDP](./Evidencias/Trafico%20Post%20Conexion.PNG)

Al ejecutar el comando del cliente antes de escribir el primer mensaje, podemos observar que no ocurrió nada hasta que se envió el primer mensaje, esto ocurre porque UDP es un protocolo _“ciego”_ no orientado a la conexión; simplemente envía los datagramas sin un proceso de validación. A diferencia de TCP, que antes de enviar cualquier dato, genera trafico para establecer la conexión mediante el dialogo en 3 pasos (Three-way handshake) y luego confirma la recepción de los segmentos.

- ***Trafico Post Conexion TCP:***

![Trafico Post Conexion TCP](./Evidencias/Trafico%20Post%20Conexion%20TCP.PNG)


## b) ¿Cuántos datagramas generó cada mensaje? ¿Hay algo parecido a un ACK?

Cada mensaje generó un datagrama. Por otro lado, no hay nada parecido a un ACK, ya que este no los utiliza. El emisor envía el datagrama y no sabe si llegó o no.

- ***Datagramas generados por cada mensaje:***

![Datagramas generados por cada mensaje](./Evidencias/Ejercicio%203b.PNG)

## c) Comparen el encabezado UDP con el encabezado TCP de un segmento con datos: ¿qué campos tiene cada uno? ¿Cuántos bytes ocupa cada encabezado? 

El encabezado UDP siempre mide 8 bytes, tiene 4 campos: Source Port, Destination Port, Length y Checksum.

- ***Encabezado UDP:***

![Encabezado UDP](./Evidencias/Ejercicio%203c.PNG)

El encabezado TCP mide al menos 20 bytes, es decir, tiene más campos que el anterior(UDP): Source Port, Destination Port, Sequence Number, Acknowledgment Number, Header Length, Flags (SYN, ACK, FIN, RST, PSH, etc), WIndows Size, Checksum, Urgent Pointer y Options.

- ***Encabezado TCP:***

![Encabezado TCP](./Evidencias/Ejercicio%203c%20parte%202.PNG)

## d) ¿Qué pasó en la red al cerrar el cliente con Ctrl+C? ¿Y en TCP?

Al cerrar el cliente con Ctrl+C, podemos observar que no paso nada en la red. No se envía ningún paquete, el programa solamente se cierra localmente.
Por otro lado, al cerrar de esta forma en TCP, vemos que se enviaron paquetes correspondientes al  cierre (FIN, ACK) y su confirmación de ACK, tal como se observa en la captura

- ***Evidencia del trafico tras cerrar el cliente en TCP:***

![Cerrar el cliente con Ctrl+C en TCP](./Evidencias/Ejercicio%203d.PNG)


## e) Para enviar la misma frase, ¿cuántos paquetes necesitaron en total con TCP y cuántos con UDP? ¿Qué "compran" con los paquetes extra de TCP?

En TCP se necesitaron nueve paquetes para poder enviar una frase, incluyendo los tres del Handshake para establecer la conexión, los dos paquetes del mensaje (el que contiene la frase y la confirmación de recepción)  y los cuatro de cierre

- ***Numero de paquetes enviado en TCP:***

![Numero de paquetes enviado en TCP](./Evidencias/Ejercicio%203e.PNG)

_(se puede observar los 3 paquetes para establecer conexión, 2 paquetes por mensaje, es decir 12 paquetes y los 4 de cierre)_

Por otro lado, en UDP se necesitó un solo paquete para poder enviar una frase

- ***Numero de paquetes enviado en UDP:***

![Numero de paquetes enviado en UDP](./Evidencias/Ejercicio%203e%20parte%202.PNG)

Podemos decir que, con los paquetes extra de TCP, *"compramos"* confiabilidad y control de errores. En TCP, si algún paquete se pierde, este lo sabría y pediría la retransmisión. En cambio, en UDP, directamente no se sabría si llegó el paquete o no.

## f) ¿Y si nadie escucha? 

En TCP al intentar conectarse se envia un SYN, pero el sistema operativo de la maquina destino responde con un [RST, ACK]  rechazando la conexion. El programa cliente se cierra indicando que la conexión fue rechazada.
En UDP el cliente no sabe que el puerto esta cerrado, asi que envía el datagrama con el msj, el sistema operativo destino responde utilizando el protocolo ICMP con un mensaje de tipo “Destination unreacheable (Port unreachable). 

- ***Resultado al intentar conectar sin abrir el puerto:***

![Nadie escucha](./Evidencias/Ejercicio%203f.PNG)

![Nadie escucha](./Evidencias/Ejercicio%203f%20parte%202.PNG)







