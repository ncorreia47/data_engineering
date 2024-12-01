import json
import random


fake = Faker()

producer = KafkaProducer(
    bootstrap_server='kafka:9093',
    api_version=(3, 8, 0),
    value_serializer = lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8')
)


def generete_temperature_data():

    return {
        'sensor_id': str(random.randint(1, 50)),
        'temperature': round(random.uniform(-10.0, 40.0), 2),
        'timestamp': fake.date_time().isoformat()
    }


if __name__ == '__main__':
    topic = 'temperature_sensor_topic'


    while True:
        data = generete_temperature_data()
        key = data['sensor_id']
        producer.send(topic, key=key, value=data)
        time.sleep(1)