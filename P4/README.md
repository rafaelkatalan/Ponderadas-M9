# Simulador de Sensor MQTT

Este é um simulador de sensor MQTT que simula leituras aleatórias do MiCS-6814 e as publica em um tópico MQTT. Esse projeto é útil para testar e demonstrar a comunicação MQTT entre dispositivos e servidores.

## Instalação

### 1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/rafaelkatalan/Ponderadas-M9/tree/master/P4
   ```
   Vá até o repositorio no terminal.

### 2. **Instalar Dependências:**

   ```bash
   pip install paho-mqtt
   ```
   
## Uso


### 2. **Executar o Simulador:**

**Publisher**:

   ```bash
   python3 publisher.py
   ```
**Subscriber**:

Em um outro terminal:

   ```bash
   python3 subscriber.py
   ```

   O simulador do Publisher começará a gerar leituras aleatórias e as publicará no tópico MQTT especificado.Enquanto isso o subscriber fará a leitura dos dados publicados.

## Vídeo Demonstrativo

Assista ao vídeo de demonstração [aqui](https://drive.google.com/file/d/17irjAb4RDKSUwc7pyyxgyCC8XaWSpC6o/view?usp=sharing).

