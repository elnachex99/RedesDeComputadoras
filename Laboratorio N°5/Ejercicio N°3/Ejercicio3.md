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