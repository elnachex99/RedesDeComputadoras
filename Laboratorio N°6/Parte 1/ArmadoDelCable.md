# Trabajo Práctico N° 6: Laboratorio de Capa Física, Redes LAN y Tráfico de Red

**Asignatura:** Redes de Computadoras - Universidad Nacional de Córdoba (FCEFyN)  
**Grupo:** WAN-direction  
**Profesor:** Santiago Martin Henn  
**Integrantes:**
- Baigorria, Ramiro Javier
- Urrestarazu, Juan Ignacio
- Mena, Franco Grabiel
- Herrera, Mauricio Agustin
- Ciruzzi, Martina
- Montes, Franco Leonel
- Valla Tello, Desiderio Jesus

---

## Parte 1: Armado y verificación del cable

### 1. Marco Teórico

#### 1.1 El medio físico: Cable de Par Trenzado (UTP Cat5e)
El cable de par trenzado no blindado (**UTP** - *Unshielded Twisted Pair*) Categoría 5e consta de 8 conductores de cobre aislados, agrupados en 4 pares trenzados entre sí. 

El propósito fundamental del trenzado es reducir las interferencias electromagnéticas externas y, fundamentalmente, la diafonía entre los pares adyacentes del mismo cable. Cada par tiene un paso de trenzado ligeramente distinto para cancelar el acoplamiento inductivo y capacitivo.

#### 1.2 Conectores y Estándares de Cableado 
Para la terminación física en redes Ethernet (100BASE-TX y 1000BASE-T) se utilizan conectores modulares RJ-45 (8P8C). 

El ordenamiento de los pines está regido por los estándares de telecomunicaciones TIA/EIA:

- **Norma T568A:** Blanco/Verde, Verde, Blanco/Naranja, Azul, Blanco/Azul, Naranja, Blanco/Marrón, Marrón.
- **Norma T568B:** Blanco/Naranja, Naranja, Blanco/Verde, Azul, Blanco/Azul, Verde, Blanco/Marrón, Marrón.

| Pin | Norma T568B | Función (100BASE-TX) |
|:---:|:---|:---:|
| 1 | Blanco / Naranja | Transmisión + (Tx+) |
| 2 | Naranja | Transmisión - (Tx-) |
| 3 | Blanco / Verde | Recepción + (Rx+) |
| 4 | Azul | Sin uso en 100M / Datos en 1G |
| 5 | Blanco / Azul | Sin uso en 100M / Datos en 1G |
| 6 | Verde | Recepción - (Rx-) |
| 7 | Blanco / Marrón | Sin uso en 100M / Datos en 1G |
| 8 | Marrón | Sin uso en 100M / Datos en 1G |

- **Cable Directo (*Straight-Through*):** Lleva la misma norma en ambos extremos (por ejemplo, T568B en ambos lados). Se emplea para conectar dispositivos de diferente nivel funcional (por ejemplo, PC a Switch o Router a Switch).
- **Cable Cruzado (*Crossover*):** Lleva T568A en una punta y T568B en la otra. Cruza los pines 1-2 con 3-6 para conectar directamente dos equipos del mismo tipo (PC a PC o Switch a Switch) cuando no se cuenta con *Auto MDI-X*.

---

### 2. Instrumental y Materiales Empleados

- Cable UTP Categoría 5e de 4 pares.
- Conectores modulares RJ-45 (8P8C).
- Capuchones / botas protectoras de goma (color verde) para alivio de tensión.
- Pinza crimpeadora con módulo de corte, pelacables y prensado RJ-45.
- Tester / comprobador de continuidad para cables Ethernet con LEDs indicadores.

---

### 3. Desarrollo Práctico y Armado de Cables
Siguiendo las consignas del trabajo práctico,empezamos con el armado respectivo del cable.

#### 3.1 Primer Cable: 
En el armado del primer cable cometimos un error al pelar mas cable del necesario,generando que los cables individuales queden expuestos en el aire.

Esto puede ocasionar un riesgo de corte frente a tirones y una mayor exposición al ruido.

![Intento (1)](<Imagenes/Intento (1).jpeg>)  
![Intento (5)](<Imagenes/Intento (5).jpeg>)  


Para corregirlo decidimos cortar el cabezal defectuoso con la pinza. 
Emparejamos cortando el excedente y volviendo a pelar correctamente.
Posteriormente colocamos la bota protectora verde en el cable.

Tras crimpar nuevamente y calzar el capuchón verde,el cable quedó firme y prolijo.

![NuestroCable(6)](<Imagenes/NuestroCable(6).jpeg>)  
![NuestroCable (3)](<Imagenes/NuestroCable (3).jpeg>)  

---

#### 3.2 Segundo Cable
Por amor al arte,armamos otro cable así todos los compañeros podian poner en práctica sus habilidades manuales.

![SegundoCable (1)](<Imagenes/SegundoCable (1).jpeg>)  
![SegundoCable (4)](<Imagenes/SegundoCable (4).jpeg>)  

---


### 4. Verificación con multímetro
La verificación de la continuidad y el mapa de pines se realizó utilizando un tester de cableado Ethernet.

- Se conectó cada extremo del cable a las interfaces maestra y remota del comprobador.
- En ambos cables fabricados, la secuencia de LEDs del 1 al 8 se encendió de forma correlativa, sincronizada y sin saltos ni luces apagadas (`1-1`, `2-2`, `3-3`, `4-4`, `5-5`, `6-6`, `7-7`, `8-8`). 

Esto comprobó:
  * Ausencia de conductores cortados (circuitos abiertos).
  * Ausencia de cortocircuitos entre conductores adyacentes.
  * Correcta correspondencia de pines (sin inversiones de pares ni cruces).

*(Nota: Disculpe profe nos olvidamos de sacarle foto al multímetro.Le juramos que el cable funcionó...ninguna placa de red murió en este trabajo práctico).*

---

### 5. Intercambio de Cables
Intercambiamos uno de nuestros cables con el grupo que estaba a nuestra derecha para realizar una inspección visual cable:

![OtroGrupo(3)](<Imagenes/OtroGrupo(3).jpeg>)  
![OtroGrupo (2)](<Imagenes/OtroGrupo (2).jpeg>)  

Observaciones Técnicas sobre el Cable del Otro Grupo:

1. El ordenamiento de colores respetó la norma establecida y los pines hicieron contacto hasta el extremo del conector,lo que permitió que el cable tuviera continuidad eléctrica.
2.  Al igual que en nuestro primer intento, se observó que el cable fue cortado de más quedando los cables individuales descubiertos. 
3. El cable funciona a nivel eléctrico para pruebas de laboratorio pero a su vez, se corre peligro ya que el movimiento cotidiano provocará una posible rotura.

---
