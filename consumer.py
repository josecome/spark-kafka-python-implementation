from kafka import KafkaConsumer
import sqlalchemy
import json

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/kafka')
consumer = KafkaConsumer('my_favorite_topic', bootstrap_servers='localhost:9092',api_version=(0,1,0))

def saving_data():
    for message in consumer:
        result = ''
        ms = message.value
        json_data = json.loads(ms.decode('utf-8'))
        firstname = json_data['firstname']
        lastname = json_data['lastname']
        stmt = f"INSERT INTO persons (firstname, lastname) VALUES ('{firstname}', '{lastname}')"
        with engine.connect() as conn:
            result = conn.execute(stmt)
            #conn.commit()
        # print(message)
        # print(message.value)

if __name__ == "__main__":
    saving_data()
