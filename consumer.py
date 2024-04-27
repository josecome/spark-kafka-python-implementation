from kafka import KafkaConsumer
from queue import Queue 
from threading import Thread 
import sqlalchemy
import json
from time import sleep

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/kafka')
consumer = KafkaConsumer('my_favorite_topic', bootstrap_servers='localhost:9092',api_version=(0,1,0))

def getting_data(out_q, c):
    x = 0
    for message in consumer:
        ms = message.value
        out_q.put(ms.decode('utf-8'))
        x += 1
        c.put(x)
    
    x = 0

def saving_data(in_q, c):
    result = ''
    stmt = f"INSERT INTO persons (firstname, lastname) VALUES "
    sleep(10)
    j = 0
    while True:
        j += 1    
        data = in_q.get() 
        json_data = json.loads(data)
        firstname = json_data['firstname']
        lastname = json_data['lastname']

        stmt += f"('{firstname}', '{lastname}')"
        cc = int(c.get())
        if j < cc: stmt += ','
        if cc: break

    with engine.connect() as conn:
        print(stmt)
        result = conn.execute(stmt)


if __name__ == "__main__":
    # Create the shared queue and launch both threads
    q = Queue()
    c = Queue()
    t1 = Thread(target = getting_data, args =(q, c,))
    t2 = Thread(target = saving_data, args =(q, c,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Block until all tasks are done.
    # q.join()
