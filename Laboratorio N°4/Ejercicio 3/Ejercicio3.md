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
> **Profesor:** Santiago Martin Henn
> - Santiago Martin Henn 

---

# Consigna 3

En esta actividad se implementó en Cisco Packet Tracer una red LAN para simular la red de una aeronave.

La red se dividió en tres sectores:

| VLAN | Nombre | Red IP | Gateway | Acceso |
|:-----:|:-------|:-------|:--------|:-------|
| 10 | Turista | 10.10.10.0/24 | 10.10.10.1 | Solo servidor local |
| 20 | Business | 10.10.20.0/24 | 10.10.20.1 | Servidor local + Internet |
| 99 | Administración | 10.10.99.0/24 | 10.10.99.1 | Acceso total |

También se utilizó la red `200.0.0.0/30` para simular el enlace con el ISP.

## Topología y configuración

Primero se armó la topología general de la red con los dispositivos de las tres clases, el servidor de entretenimiento, el switch, el router de la aeronave y el router ISP.

![Mapa topologico inicial](./Registro%20con%20imagenes/1-Mapa%20topologico%20inicial.png)

En el switch se configuraron las VLAN 10, 20 y 99 y se asignaron los puertos correspondientes a cada sector.

![Configuracion del Switch](./Registro%20con%20imagenes/2-Configuración%20del%20Switch.png)

En el router de la aeronave se configuraron las subinterfaces correspondientes a cada VLAN, junto con DHCP, NAT y ACL para aplicar los distintos permisos de acceso.

![Configuracion Router Aircraft](./Registro%20con%20imagenes/3-Configuracion%20de%20Router-Aircraft.png)

![Configuracion Router Aircraft 2](./Registro%20con%20imagenes/3-Configuracion%20de%20Router-Aircraft2.png)

El segundo router se utilizó para simular el ISP.

![Configuracion Router ISP](./Registro%20con%20imagenes/4-Configuración%20de%20Router%20ISP.png)

También se configuró un servidor local con dirección `10.10.99.10` para representar el sistema de entretenimiento.

![Configuracion IP Server](./Registro%20con%20imagenes/5-Server_IPCONFIG.png)

Finalmente, los dispositivos se distribuyeron dentro del esquema del avión según el sector correspondiente.

![Distribucion Airplane](./Registro%20con%20imagenes/6-Distribucion_Airplane.png)

## Verificación de direccionamiento

Se comprobó que los dispositivos de cada sector recibieran correctamente una dirección IP mediante DHCP.

### Turista

![Config IP Turista](./Registro%20con%20imagenes/7-Config%20IP%20Turista.png)

### Business

![Config IP Business](./Registro%20con%20imagenes/8-Config%20IP%20Business.png)

### Administración

![Config IP Admin](./Registro%20con%20imagenes/9-Config%20IP%20Admin.png)

## Pruebas

### Turista

Se comprobó que la clase Turista puede acceder al servidor local, pero no al ISP.

![Test Ping Turista](./Registro%20con%20imagenes/10-Test%20Ping%20Turista.png)

También se verificó el acceso al servidor de entretenimiento mediante el navegador web.

![Test Web Turista](./Registro%20con%20imagenes/11-Test%20Web%20Turista.png)

### Business

Se comprobó que la clase Business puede acceder tanto al servidor local como al ISP.

![Test Ping Business](./Registro%20con%20imagenes/12-Test%20Ping%20Business.png)

También se verificó el acceso al servidor desde el navegador.

![Test Web Business](./Registro%20con%20imagenes/13-Test%20Web%20Business.png)

### Administración

Se verificó que Administración puede comunicarse con las distintas redes y con el ISP.

![Test Ping Admin 1](./Registro%20con%20imagenes/14-Test%20Ping%20Admin_1.png)

![Test Ping Admin 2](./Registro%20con%20imagenes/15-Test%20Ping%20Admin_2.png)

## Conclusion

En este punto se implementó una red dividida en tres sectores: Turista, Business y Administración.

Mediante las VLANs, DHCP, NAT y ACL se configuraron distintos niveles de acceso para cada sector. Las pruebas realizadas permitieron comprobar que Turista puede acceder al servidor local pero no a Internet, Business puede acceder al servidor y a Internet, y Administración tiene acceso completo a la red.

De esta manera se verificó que la segmentación y las restricciones configuradas funcionaron de acuerdo con lo esperado.