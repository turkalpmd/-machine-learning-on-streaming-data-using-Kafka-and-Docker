import time 
import json 
import random 
from datetime import datetime
from  data_generator  import iris_data_creator
from kafka import KafkaProducer

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    # producer should contact to bootstrap initial cluster metadata
    bootstrap_servers=['localhost:9092'],
    # client_id (str) – a name for this client. 
    client_id = "kafka-python-producer-#", #this id is default
    # used to convert user-supplied message values to bytes.
    # key_serializer (callable) – used to convert user-supplied keys to bytes 
    # value_serializer (callable) – used to convert user-supplied message values to bytes.
    value_serializer=serializer,
    # The number of acknowledgments the producer requires the leader to have received before considering a request complete. 
    # 0: Producer will not wait for any acknowledgment from the server.
    # 1: Wait for leader to write the record to its local log only.
    # all: Wait for the full set of in-sync replicas to write the record.
    acks = "all",
    # for more knowledge: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.htm
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = iris_data_creator()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('iris_pycaret', dummy_message)
        
        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 2)
        time.sleep(time_to_sleep)
 