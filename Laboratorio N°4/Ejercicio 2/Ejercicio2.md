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

![Configuracion de ip de PC-A](./Capturas%20de%20Pantalla/Configuracion%20de%20ip%20de%20la%20PC-A.PNG)

![Configuracion de ip de PC-B](./Capturas%20de%20Pantalla/Configuracion%20de%20ip%20de%20la%20PC-B.PNG)

---

## Consigna 2.a.b.c.
Desde cada computadora (PC-A y PC-B) se accedió a la interfaz de línea de comandos (CLI) de SW-1 y de SW-2 respectivamente, ingresamos a la terminal y configuramos los switches de la siguiente forma:

* Se estableció el nombre del dispositivo mediante: **hostname sw1** y **hostname sw2** respectivamente. Por lo tanto, los switches quedaron identificados como sw1 y sw2
* Se configuraron/asignaron contraseñas para el modo privilegiado, la consola y las líneas VTY
  * Para el acceso privilegiado se utilizó: **enable secret contrasena_exec**
  * Para la consola se utilizó: **password contrasena_consola**
  * Para la consola se utilizó: **password contrasena_vty**
* Para evitar que las contraseñas configuradas aparezcan en texto plano dentro de la configuración del dispositivo, se utilizó: **service password-encryption**

![Configuracion del SW-1](./Capturas%20de%20Pantalla/Configuracion%20del%20Switch-1.PNG)

![Configuracion del SW-2](./Capturas%20de%20Pantalla/Configuracion%20del%20Switch-2.PNG)

---

## Consigna 2.d

---

## Consigna 2.e

---

## Consigna 2.f

---

## Consigna 2.g

---

## Consigna 2.h

---

## Consigna 2.i

---

## Consigna 2.j

---

## Consigna 2.k

--

## Consigna 2.l