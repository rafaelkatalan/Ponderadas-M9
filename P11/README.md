# Simulador de Sensor MQTT

Este é um simulador de sensor MQTT que simula leituras aleatórias do MiCS-6814 e as publica em um tópico MQTT. Um Kafka Producer irá ler as mensagens do tópico e publicá-las em um cluster Kafka online. Em seguida, as mensagens são consumidas por um Kafka Consumer e salvas em um banco de dados SQLite local.

## Instalação

### 1. **Clonar o Repositório:**

```bash
git clone https://github.com/rafaelkatalan/Ponderadas-M9/tree/master/P11
```
Navegue até o diretório clonado no terminal.

### 2. **Instalar Dependências:**

```bash
pip install paho-mqtt
pip install confluent-kafka
```
   
## Uso

### 2. **Executar o Simulador:**

Para executar o simulador, é necessário que tanto o Kafka quanto o broker MQTT estejam configurados e rodando corretamente no Confluent Cloud e no HiveMQ. Os dados de autenticação devem estar corretos e com acesso aos respectivos serviços no `client.properties` e no `.env`.

**MQTT Publisher**:

```bash
python3 mqtt-publisher.py
```

**Kafka Producer**:

Em outro terminal:

```bash
python3 kafka-producer.py
```

**Kafka Consumer**

Em outro terminal:

```bash
python3 kafka-consumer.py
```

O simulador do Publisher começará a gerar leituras aleatórias e as publicará no tópico MQTT especificado. Enquanto isso, o Kafka Producer lerá os dados publicados e os colocará no Kafka. O Kafka Consumer consumirá as mensagens do Kafka e as salvará em um banco de dados SQLite local.

## Vídeo Demonstrativo

[Clique aqui para ver o video demonstrativo](https://drive.google.com/file/d/1TzHrBJmcmmUp4Wb-v2M_8PzsdSi1TlHO/view?usp=sharing)