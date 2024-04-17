from kafka import KafkaConsumer

consumer = KafkaConsumer('my_favorite_topic', bootstrap_servers='localhost:9092',api_version=(0,1,0))
for message in consumer:
    print(message)
    print(message.value)