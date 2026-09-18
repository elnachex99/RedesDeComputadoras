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
 PC-A ───── SW-1 ───── SW-2 ───── PC-B    

Las direcciones IP utilizadas inicialmente fueron:

| Dispositivo |  Interfaz | Direccion IP | Mascara       | 
|:------------|:----------|:-------------|:--------------|
| SW-1        | VLAN 1    | 192.168.1.11 | 255.255.255.0 |  
| SW-2        | VLAN 1    | 192.168.1.12 | 255.255.255.0 |
| PC-A        | NIC       | 192.168.10.3 | 255.255.255.0 |   
| PC-B        | NIC       | 192.168.10.4 | 255.255.255.0 |      

- ***PC-A:***
![Configuracion de ip de PC-A](./Capturas%20de%20Pantalla/Configuracion%20de%20IP%20de%20la%20PC-A.PNG)

- ***PC-B:***
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

- ***SWITCH 1:***
![Configuracion del SW-1](./Capturas%20de%20Pantalla/Configuracion%20del%20Switch-1.PNG)

- ***SWITCH 2:***
![Configuracion del SW-2](./Capturas%20de%20Pantalla/Configuracion%20del%20Switch-2.PNG)

---

## Consigna 2.d
Configuramos las redes VLAN para ambos switches. Inicialmente, se configuró la interfaz virtual correspondiente a VLAN 1 para permitir la administración de los switches. De esta manera, cada switch contó con una dirección IP que permitió identificarlo dentro de la red de administración

- ***SWITCH 1:*** 
    * ip address: _**192.168.1.11**_
    * mascara: _**255.255.255.0**_


    ![Configuracion de la VLAN inicial del SW-1](./Capturas%20de%20Pantalla/Configuracion%20de%20la%20IP%20de%20administración%20de%20SW-1.PNG)

- ***SWITCH 2:***
    * ip address: _**192.168.1.12**_
    * mascara: _**255.255.255.0**_


    ![Configuracion de la VLAN inicial del SW-2](./Capturas%20de%20Pantalla/Configuracion%20de%20la%20IP%20de%20administracion%20de%20SW-2.PNG)

---

## Consigna 2.e
Procedimos a desconectar/deshabilitar las interfaces que no estaban siendo utilizadas, tal que:

- ***SWITCH 1:***
![Shutdown de interfaces NO utilizadas en el SW-1 (Parte 1)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-1%20(parte%201).PNG)
![Shutdown de interfaces NO utilizadas en el SW-1 (Parte 2)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-1%20(parte%202).PNG)
![Shutdown de interfaces NO utilizadas en el SW-1 (Parte 3)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-1%20(parte%203).PNG)

- ***SWITCH 2:***
![Shutdown de interfaces NO utilizadas en el SW-2 (Parte 1)](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-2%20(parte%201).PNG)
![Shutdown de interfaces NO utilizadas en el SW-2 (Parte 2](./Capturas%20de%20Pantalla/Punto%202-e%20del%20SW-2%20(parte%202).PNG)

---

## Consigna 2.f
Una vez que terminamos la configuracion de cada switch, guardamos la informacion usando el comando _**write memory**_


- ***SWITCH 1:***
![Guardado de memoria del SW-1](./Capturas%20de%20Pantalla/Punto%202-f%20del%20SW-1.PNG)

- ***SWITCH 2:***
![Guardado de memoria del SW-2](./Capturas%20de%20Pantalla/Punto%202-f%20del%20SW-2.PNG)

---

## Consigna 2.g
Finalmente, probamos la comunicacion mediante un ping, tal que:

- ***DESDE PC-A:*** hacemos _**ping 192.168.10.4**_

![Ping desde PC-A](./Capturas%20de%20Pantalla/Punto%202-g%20PC-A.PNG)

- ***DESDE PC-B:*** hacemos _**ping 192.168.10.3**_

![Ping desde PC-B](./Capturas%20de%20Pantalla/Punto%202-g%20PC-B.PNG)

---

## Consigna 2.h.i
Creamos las VLANs en los switches, tal que:

|  VLAN  |    NOMBRE    |              FUNCION              |
|:-------|:-------------|:----------------------------------|
|   10   | Laboratorio  | Red destinada al laboratorio      |  
|   20   | Bar          | Red destinada al sector Bar       |
|   99   | Management   | Red destinada a la administración |


- ***SWITCH 1:***
![VLANs del SW-1](./Capturas%20de%20Pantalla/Creacion%20de%20las%20VLAN%20del%20SW-1.PNG)

- ***SWITCH 2:***
![VLANs del SW-2](./Capturas%20de%20Pantalla/Creacion%20de%20las%20VLAN%20del%20SW-2.PNG)

_Tras analizar los datos, podemos decir que la VLAN utilizada por defecto por el switch es la VLAN 1_

---

## Consigna 2.j
Para avanzar con los testeos, se asigno la PC-A a la VLAN Laboratorio (VLAN numero 10)

![PC-A a la VLAN Laboratorio](./Capturas%20de%20Pantalla/Asignar%20la%20PC-A%20a%20la%20VLAN%20Laboratorio.PNG)

Al seleccionar y utilizar el comando _**interface fastethernet 0/6**_ , conectamos la PC-A al puerto _**FastEthernet0/6**_ de SW-1. De esta manera, el puerto Fa0/6 quedó configurado como puerto de acceso perteneciente a la VLAN llamada "Laboratorio" (VLAN 10).

---

## Consigna 2.k.m
Posteriormente, se modificó la configuración de administración del switch, ya que desde la VLAN 1, removimos la IP de Management y la configuramos para que funcionara en la VLAN 99. Es decir, la dirección IP que inicialmente se encontraba asociada a la VLAN 1 fue eliminada, luego se configuró la interfaz virtual correspondiente a la VLAN 99
__En SW-2 se realizó el mismo procedimiento utilizando su dirección correspondiente__
De esta manera, la administración de ambos switches pasó de la VLAN 1 a la VLAN 99, tal que:


- ***SWITCH 1:***
![Administración del SW-1 de VLAN 1 a VLAN 99](./Capturas%20de%20Pantalla/Punto%202-K%20para%20el%20SW-1.PNG)

- ***SWITCH 2:***
![Administración del SW-2 de VLAN 1 a VLAN 99](./Capturas%20de%20Pantalla/Punto%202-K%20para%20el%20SW-2.PNG)

---

## Consigna 2.l
Verificamos el estado de las VLANs y las INTERFACES utilizando los comandos _**show vlan brief**_ y _**show ip interface brief**_ respectivamente, tal que:

![Estado de las VLANs y las INTERFACES](./Capturas%20de%20Pantalla/Punto%202-l.PNG)

---

## Consigna 2.n
Finalmente, para comprobar la correcta comunicacion y/o conectividad entre PC-A y PC-B utilizando las VLANs, realizamos un ping desde PC-A a la direccion _**192.168.10.4**_, y otro ping desde PC-B a la direccion _**192.168.10.3**_. Como resultado, obtuvimos lo siguiente:

![Conectividad entre PC-A y PC-B](./Capturas%20de%20Pantalla/Punto%202-n.PNG)

Estas pruebas permitieron comprobar, respectivamente, la comunicación entre los equipos pertenecientes a la VLAN 10 y la comunicación entre las interfaces de administración de los switches.

## Conclusion

En esta actividad pudimos implementar y configurar una red local utilizando una herramienta como lo es Cisco. Se realizo la configuracion basica de los switches, incluyendo nombres, contraseñas y "mecanismos" de proteccion de las mismas. 
Por otro lado, se crearon VLANs y se asignaron a puertos especificos. Posteriormente, la administracion de los switches fue trasladada desde la VLAN 1 hacia la VLAN 99.
Finalmente, se configuro el enlace entre los switches, el cual permitio el transporte de las VLANs y se realizaron pruebas de conectividad entre los distintos dispositivos usando _**ping**_.