import json 
import pandas as pd
from kafka import KafkaConsumer
from pycaret.classification import load_model
from pycaret.classification import*

# path name must be same with producer.
model = load_model('/home/izzet/Desktop/projects/basic_project/iris_model.pkl')

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'iris_pycaret', # topic name !!!!
        #  that the consumer should contact to bootstrap initial cluster metadata. 
        bootstrap_servers='localhost:9092',
        # A name for this client. 
        client_id = 'kafka-python-{version}', # Default
        # The name of the consumer group to join for dynamic partition assignment (if enabled), 
        # and to use for fetching and committing offsets. 
        group_id = None, #
        # key_deserializer
        # value_deserializer
        auto_offset_reset='earliest'
        # for other knowledges;
        # https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

    )

    for message in consumer:
        # firstly load to consumer data then transfer to pandas dataframe
        prediction_data = pd.read_json(json.loads(message.value))
        #print(prediction_data)
        print(predict_model(model,prediction_data))
        

