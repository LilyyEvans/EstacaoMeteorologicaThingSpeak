# Estação Meteorológica


Projeto de IoT desenvolvido para a matéria de Fundamento da Internet das Coisas, do curso de Análise e Desenvolvimento de Sistemas da PUCPR.

Estação Meteorológica construída usando uma placa ESP32-WROOM, um sensor de temperatura DHT22 e um relé 5V FL-3FF-S-Z.

A estação lê a temperatura do sensor e envia os dados para um canal do ThingSpeak.
O relé é acionado caso a temperatura chegue a 31º ou a umidade relativa do ar esteja acima de 70%.

Projeto realizado sem o uso de breadboard.


Conexões do ESP32:


| DHT22    | ESP32     |
| ---      | ---       |
| DAT      | 14        |
| VCC      | 3V3       |
| GND      | GND       |

| Relay    | ESP32     |
| ---      | ---       |
| GND      | GND       |
| VCC      | 5V        |
| IN       | 21        |



