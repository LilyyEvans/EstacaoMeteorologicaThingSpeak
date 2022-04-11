import dht
import machine
import time
import network
import urequests

r = machine.Pin(21, machine.Pin.OUT) # Define o PIN do relé
d = dht.DHT22(machine.Pin(14))       # Define o PIN do sensor DHT22

def conecta(ssid, senha):            # Função para conectar a rede Wi-Fi
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

station = conecta("SUA REDE", "SUA SENHA") # Parâmetros da rede Wi-Fi
if not station.isconnected():
    print("Não conectado")
else:
    print("Conectado")

while True:                          # Função de leitura de temperatura
    d.measure()
    print("Temperatura = {}; Umidadade = {}".format(d.temperature(), d.humidity())) # Exibe temperatura no console
    time.sleep(7)
    
    if d.temperature()>31 or d.humidity()>70:   # Função para ativar o relé acima de 31º
        r.value(1)
    else:
        r.value(0)
            result = urequests.get("https://api.thingspeak.com/update?api_key=SEU_LINK_DO_THINGSPEAK&field1={}&field2={}".format(d.temperature(), d.humidity())) # Função para exportar os dados obtidos para o ThingSpeak
    print(result.text)
    result.close()
station.disconnect
