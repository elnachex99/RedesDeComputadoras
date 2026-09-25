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

## Consigna 1.a
Las redes informaticas se clasifican generalmente por su extension geografica o radio de cobertura,
Podemos clasificarlas de la siguiente manera.
1) PAN (Personal Area Network) - (Redes de area personal)
    Su alcance es de uno pocos metros usualmente menos de diez metros.
    Diseñada para interconectar dispositivos individuales centrados en una persona (teléfonos móviles, auriculares, computadoras portátiles, periféricos). Suele emplear tecnologías inalámbricas de bajo consumo (**WPAN**) como *Bluetooth*, *Zigbee* o *NFC*, o cableadas como *USB*

2) LAN (Local Area Network) - (Redes de area local)
    Generalmente su alcance es de una habitacion, oficina, hogar hasta un edificio completo. 
    Su alcance es usualmente de 1km 
    Propiedad privada de una misma organización o usuario6. Destaca por sus altas velocidades de transmisión (de $10\text{Mbps}$ a $10\text{Gbps}$ o más)7 y bajas tasas de error. Utiliza medios guiados (cables UTP Cat 5e/6/6A, fibra óptica) o inalámbricos (WLAN / Wi-Fi).

3) CAN (Campus Area Network - Red de area de campus)
    Su alcance es de 1km hasta los 5km 
    Interconecta múltiples redes LAN distribuidas en diversos edificios dentro de una misma propiedad (ej. un campus universitario, complejo industrial o base militar) mediante enlaces troncales (*backbones*) de alta velocidad, típicamente de fibra óptica.

4) MAN (Metropolitan Area Network - Redes de area metropolitana)
    Generalmente su alcance es de 5km a 50km.
    Conecta múltiples redes LAN dentro de una ciudad o zona metropolitana. Son operadas habitualmente por proveedores de telecomunicaciones o consorcios de empresas públicas/privadas utilizando tecnologías como *Metro Ethernet* o anillos de fibra óptica.

5) WAN (Wide Area Network - Redes de area amplia)
    Su alcance es regional,nacional,continental o global. No tiene limite fisico por ejemplo internet
    Cubre extensas áreas geográficas mediante infraestructura pública o alquilada a proveedores de servicios de telecomunicación (*ISPs*). Utiliza tecnologías de conmutación de paquetes, líneas dedicadas, satélites y enlaces submarinos. Sus velocidades son variables y presenta mayores retardos de propagación que una LAN.

6) SAN (Storage Area Network - Red de area de almacenamiento)
    Tiene un alcance local dentro de salas de computo o salas de servidores. 
    Es una red dedicada exclusivamente a interconectar servidores con dispositivos de almacenamiento masivo como por ejemplo arreglos de discos a muy alta velocidad utilizando protocolos como *Fibre Channel* o *iSCS*

El orden en que se ordenarian seria masomenos asi
PAN $\rightarrow$ LAN $\rightarrow$ CAN $\rightarrow$ MAN $\rightarrow$ WAN

## Consigna 1.b
**¿Que es una VLAN?¿Como se clasifican?**
Una **VLAN** (Red de Área Local Virtual) es una subdivisión lógica en la Capa de Enlace (Capa 2) que permite definir **múltiples redes de área local virtuales sobre una única infraestructura física de conmutación**
técnicamente, se define como un conjunto de puertos en un conmutador (*switch*) Ethernet configurados por el administrador de red para formar un único dominio de difusión independiente (**broadcast domain**)

Las VLAN se pueden clasificar segun su metodo de interconexion y su asignacion
Una posible clasificacion podria ser la siguiente 
 - VLAN basada en puerto: Asigna los dispositivos a una VLAN según el puerto físico del switch al que están conectados.                                            
 - VLAN basada en MAC:Asigna los dispositivos a una VLAN según su dirección MAC.                                                                               
 - VLAN basada en aplicación: Asigna el tráfico a una VLAN según la aplicación o tipo de servicio utilizado.                                                           
 - VLAN Tagged (etiquetada):Utiliza etiquetas **802.1Q** para identificar a qué VLAN pertenece cada trama.                                                           
 - VLAN Untagged (sin etiquetar):Las tramas se transmiten sin etiqueta VLAN, normalmente en puertos de acceso.                                                            
 - VLAN nativa:Es la VLAN utilizada para transportar tráfico sin etiquetar en un enlace **trunk**.                                                      
 - VLAN híbrida:Combina tráfico etiquetado y sin etiquetar en un mismo puerto, permitiendo trabajar con diferentes VLAN.                                 
 - VLAN de gestión:Se utiliza para administrar dispositivos de red como switches, routers y puntos de acceso.                                               
 - VLAN de control: Se utiliza para transportar tráfico relacionado con funciones de control y operación de la red.                                          
- VXLANTecnología: que permite crear redes virtuales sobre una infraestructura IP, utilizada principalmente en redes grandes y centros de datos. 

## Consigna 1.c
**Protocolo IEEE 802.1Q**

El protocolo IEEE 802.1Q (conocido como Dot1q) es un protocolo utilizado para identificar y transmitir tramas de múltiples VLANs (Redes de Área Local Virtuales) por medio de una red Ethernet compartida. Este protocolo agrega un Tag en las tramas Ethernet para que los dispositivos de red puedan reconocer a qué red lógica pertenece cada trama.

La relación con las VLANs radica en que el estándar 802.1Q es el que permite que una misma VLAN pueda extenderse a través de varios switches, transportando sus tramas etiquetadas por enlaces troncales.

Además podemos destacar dos características:
- **Habilitación de Enlaces Troncales (Trunking):** Sin este protocolo, un cable de red entre 2 switches no podría transportar tráfico de más de una VLAN. El 802.1Q permite crear "puertos troncales" que pueden multiplexar el tráfico de múltiples VLANs a través de un solo cable físico.
- **VLAN Nativa:** Existe una VLAN específica cuyo tráfico viaja por el enlace troncal sin la etiqueta 802.1Q. En muchos switches, la VLAN 1 está configurada por defecto como VLAN nativa.

## Consigna 1.d
**Tagging (Etiquetado)** 

El Tagging es el proceso de insertar un campo adicional, denominado etiqueta VLAN, dentro de un paquete de datos. Según el estándar IEEE 802.1Q, esta etiqueta se ubica después de la dirección MAC de origen y contiene el número de VLAN asignado al puerto por donde ingresó la trama.   
El ciclo de vida de esta etiqueta sigue estas reglas:

- **Transparencia:** Las computadoras conectadas a un switch envían y reciben las tramas sin contener ninguna etiqueta VLAN.
- **Uso interno y remoción:** La etiqueta se utiliza exclusivamente de forma interna. Una vez que el switch selecciona el puerto de salida hacia el dispositivo final, la etiqueta es eliminada antes de transmitir la trama.
- **Excepción (enlaces entre switches):** Un administrador puede configurar puertos específicos para que no eliminen las etiquetas VLAN al enviar tramas. Esto permite que dos o más switches compartan sus configuraciones y operen en conjunto como un único gran conmutador.   

