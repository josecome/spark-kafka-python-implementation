from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,1,0))

# producer.send('my_favorite_topic', b'some_message_bytes')
for _ in range(10):
    producer.send('my_favorite_topic', b'some_message_bytes')
    producer.flush()
