# Simulador de Sensor MQTT

Este é um simulador de sensor MQTT que simula leituras aleatórias do MiCS-6814 e as publica em um tópico MQTT. Esse projeto é útil para testar e demonstrar a comunicação MQTT entre dispositivos e servidores.

## Instalação

### 1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/rafaelkatalan/Ponderadas-M9/tree/master/P5
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

## 3. Visualização no Metabase
Com o Metabase, você pode explorar seus dados de sensores de forma intuitiva e interativa!

Siga estas etapas simples para começar:

### Inicie o Metabase:

Bash
```
sudo docker run -d -p 3000:3000 -v ~/<caminho para repositório clonado>/sensor_data.db:/sensor_data.db --name metabase metabase/metabase
```

### Acesse o Metabase:

Abra seu navegador e acesse http://localhost:3000.

### Conecte-se ao seu banco de dados:

Selecione SQLite como tipo de banco de dados.
Insira o caminho completo para o arquivo sensor_data.db no campo Conectar um arquivo .db.
Clique em Conectar.

### Explore seus dados:

O Metabase carregará automaticamente suas tabelas de dados.
Clique em uma tabela para visualizar seus dados em uma grade.
Use os filtros e ferramentas de visualização para explorar seus dados e identificar insights.

## Vídeo Demonstrativo

Assista ao vídeo de demonstração [aqui](https://photos.app.goo.gl/juFF74VnDdUqMDtq9).

