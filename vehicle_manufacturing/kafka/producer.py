from kafka import KafkaProducer
from faker import Faker
import json
import time

# Configuração do Faker
fake = Faker()

# Função para gerar dados fictícios
def generate_fake_data():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "job": fake.job()
    }

# Configuração do Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9093',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Nome do tópico no Kafka
topic = 'test_topic'

# Enviando dados fictícios para o Kafka
while True:
    fake_data = generate_fake_data()
    print(f"Sending data: {fake_data}")
    producer.send(topic, fake_data)
    time.sleep(2)  # Envia uma nova mensagem a cada 2 segundos
