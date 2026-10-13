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

## Consigna 4

## c) Ejecución (capturando en loopback con el filtro tcp.port == 12000)

Imagen del testeo de ejecución adjunta en la carpeta Evidencia con el nombre de TEST_Cliente_Server

## d) Tabla de llamadas y tráfico generado


| Llamada | ¿Dónde se ejecuta? | ¿Genera tráfico? | Segmentos que observan |
|---|---|---|---|
| socket() | servidor y cliente | No | Ninguno. Solo crea una estructura en memoria del SO. |
| bind() | servidor | No | Ninguno. Asocia IP y puerto locales. |
| listen() | servidor | No | Ninguno. Deja al SO listo para responder un SYN con SYN-ACK. |
| connect() | cliente | Si | 109 (SYN), 110 (SYN, ACK) y 111 (ACK): el three-way handshake. |
| accept() | servidor | No genera segmentos propios | Se completa con el ACK 111. El handshake lo hace el SO. |
| sendall() | servidor | Si | 114 (PSH, ACK, 23 bytes) con la respuesta. El ACK 113 lo manda el SO al recibir el mensaje. En el cliente, sendall() produce el 112 (PSH, ACK, 13 bytes). |
| recv() | servidor | No | Ninguno. Lee del buffer del SO el mensaje ya recibido (112). El ACK 113 sale por el SO, no por recv(). |
| close() | ambos | Si | Cliente: 116 (FIN, ACK) y luego 119 (ACK). Servidor: 118 (FIN, ACK), enviado tras detectar el FIN del cliente, y 117 (ACK). |



