# Laboratorio 4

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

## Consigna 2
En esta actividad se implementó en Cisco Packet Tracer una red local compuesta por dos switches, SW-1 y SW-2, y dos computadoras, PC-A y PC-B, tal que:

![Implementacion](./Capturas%20de%20Pantalla/Implementacion%20del%20punto%202.PNG)

La topologia implementada fue: 
           ── SW-1 ───── SW-2 ───
         /                        \
PC-A ───                            ── PC-B

Las direcciones IP utilizadas inicialmente fueron:

| Dispositivo |  Interfaz | Direccion IP | Mascara       | 
|:------------|:----------|:-------------|:--------------|
| SW-1        | VLAN 1    | 192.168.1.11 | 255.255.255.0 |  
| SW-2        | VLAN 1    | 192.168.1.12 | 255.255.255.0 |
| PC-A        | NIC       | 192.168.10.3 | 255.255.255.0 |   
| PC-B        | NIC       | 192.168.10.4 | 255.255.255.0 |      

![Configuracion de ip de PC-A](./Capturas%20de%20Pantalla/Configuracion%20de%20IP%20de%20la%20PC-A.PNG)

![Configuracion de ip de PC-B](./Capturas%20de%20Pantalla/Configuracion%20de%20IP%20de%20la%20PC-B.PNG)

---

## Consigna 2.a.b.c.
Desde cada computadora (PC-A y PC-B) se accedió a la interfaz de línea de comandos (CLI) de SW-1 y de SW-2 respectivamente, ingresamos a la terminal y configuramos los switches de la siguiente forma:

* Se estableció el nombre del dispositivo mediante: _**hostname sw1**_ y _**hostname sw2**_ respectivamente. Por lo tanto, los switches quedaron identificados como sw1 y sw2
* Se configuraron/asignaron contraseñas para el modo privilegiado, la consola y las líneas VTY
  * Para el acceso privilegiado se utilizó: _**enable secret contrasena_exec**_
  * Para la consola se utilizó: _**password contrasena_consola**_
  * Para la consola se utilizó: _**password contrasena_vty**_
* Para evitar que las contraseñas configuradas aparezcan en texto plano dentro de la configuración del dispositivo, se utilizó: _**service password-encryption**_

![Configuracion del SW-1](./Capturas%20de%20Pantalla/Configuracion%20del%20Switch-1.PNG)

![Configuracion del SW-2](./Capturas%20de%20Pantalla/Configuracion%20del%20Switch-2.PNG)

---

## Consigna 2.d
Configuramos las redes VLAN para ambos switches. Inicialmente, se configuró la interfaz virtual correspondiente a VLAN 1 para permitir la administración de los switches. De esta manera, cada switch contó con una dirección IP que permitió identificarlo dentro de la red de administración

* SW-1: 
    * ip address: _**192.168.1.11**_
    * mascara: _**255.255.255.0**_
![Configuracion de la VLAN inicial del SW-1](./Capturas%20de%20Pantalla/Configuracion%20de%20la%20IP%20de%20administración%20de%20SW-1.PNG)

* SW-2: 
    * ip address: _**192.168.1.12**_
    * mascara: _**255.255.255.0**_
![Configuracion de la VLAN inicial del SW-2](./Capturas%20de%20Pantalla/Configuracion%20de%20la%20IP%20de%20administración%20de%20SW-2.PNG)

---

## Consigna 2.e
Procedimos a desconectar/deshabilitar las interfaces que no estaban siendo utilizadas, tal que:

![Shutdown de interfaces NO utilizadas en el SW-1 (Parte 1)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-1%20(parte%201).PNG)
![Shutdown de interfaces NO utilizadas en el SW-1 (Parte 2)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-1%20(parte%202).PNG)
![Shutdown de interfaces NO utilizadas en el SW-1 (Parte 3)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-1%20(parte%203).PNG)

![Shutdown de interfaces NO utilizadas en el SW-2 (Parte 1)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-2%20(parte%201).PNG)
![Shutdown de interfaces NO utilizadas en el SW-2 (Parte 2](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-2%20(parte%202).PNG)

---

## Consigna 2.f
Una vez que terminamos la configuracion de cada switch, guardamos la informacion usando el comando _**write memory**_

![Guardado de memoria del SW-1](./Capturas%20de%20Pantalla/Punto%202-f%20del%20SW-1.PNG)

![Guardado de memoria del SW-2](./Capturas%20de%20Pantalla/Punto%202-f%20del%20SW-2.PNG)

---

## Consigna 2.g
Finalmente, probamos la comunicacion mediante un ping, tal que:

* Desde PC-A: hacemos _**ping 192.168.10.4**_
![Ping desde PC-A](./Capturas%20de%20Pantalla/Punto%202-g%20PC-A.PNG)

* Desde PC-B: hacemos _**ping 192.168.10.3**_
![Ping desde PC-B](./Capturas%20de%20Pantalla/Punto%202-g%20PC-B.PNG)

---

## Consigna 2.h.i
Creamos las VLANs en los switches, tal que:

|  VLAN  |    NOMBRE    |              FUNCION              |
|:-------|:-------------|:----------------------------------|
|   10   | Laboratorio  | Red destinada al laboratorio      |  
|   20   | Bar          | Red destinada al sector Bar       |
|   99   | Management   | Red destinada a la administración |

![VLANs del SW-1](./Capturas%20de%20Pantalla/Creacion%20de%20las%20VLAN%20del%20SW-1.PNG)

![VLANs del SW-2](./Capturas%20de%20Pantalla/Creacion%20de%20las%20VLAN%20del%20SW-2.PNG)

_Tras analizar los datos, podemos decir que la VLAN utilizada por defecto por el switch es la VLAN 1_

---

## Consigna 2.j

---

## Consigna 2.k

--

## Consigna 2.l