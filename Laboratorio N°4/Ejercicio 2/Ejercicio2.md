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

## Consigna 2.a
    En esta actividad se implementó en Cisco Packet Tracer una red local compuesta por dos switches, SW-1 y SW-2, y dos computadoras, PC-A y PC-B, tal que:

    ![Implementacion](C:\Users\ramir\OneDrive\Escritorio\Rami\Facu\Cuarto Año - Segundo Semestre - Plan Nuevo\Redes de Computadoras\Repo GITHUB\Laboratorio N°4\Ejercicio 2\Implementacion del punto 2.PNG)

    La topologia implementada fue: 
    PC-A ───── SW-1 ───── SW-2 ───── PC-B

    Las direcciones IP utilizadas inicialmente fueron:
    | Dispositivo |  Interfaz | Direccion IP | Mascara       | 
    |:------------|:----------|:-------------|:--------------|
    | SW-1        | VLAN 1    | 192.168.1.11 | 255.255.255.0 |  
    | SW-2        | VLAN 1    | 192.168.1.12 | 255.255.255.0 |
    | PC-A        | NIC       | 192.168.10.3 | 255.255.255.0 |   
    | PC-B        | NIC       | 192.168.10.4 | 255.255.255.0 |        