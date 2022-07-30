# -machine-learning-on-streaming-data-using-Kafka-and-Docker
I have completed my first project that machine learning on streaming data using Kafka and Docker. You can check-up my GitHub repository for codes.


# Steps of process:
##### 1- install vscode
##### 2- install anaconda
##### 3- create nev envoirement on conda
##### 4- install docker
##### 5- install docker-compose
##### 6- install docker desktop (https://www.youtube.com/watch?v=Vplj9b0L_1Y)
##### 7- download docker-compose.yaml (https://github.com/cigdemkadakoglu/apache-kafka)
##### 8- docker-composeup -d
##### 9- you can check containers with docker ps or docker stats -a
##### 10- create topic 
  * I am really hardned with creating topic. Because of sh bash or another concepts are far to my domain. 
  * But, our container named kafdrop also have create topic function. 
  * You can write on the browser bar: https://localhost:9000/
  ![Screenshot from 2022-07-31 00-03-18](https://user-images.githubusercontent.com/85236337/181996082-3a1e92fe-f819-4b06-8061-4e79b4085e4a.png)
  * create a new topic it is easier way for create topics. 
 
 ##### 11- I love pycaret library 
       * setup()
       * create_model()
       * tune_model()
       * save_model()
        * Here is complex at API docs, you have to save the model with path_name just like pandas save function.
       * load_model()
        * And also when loading model, you must take path_name.
       * How it easy, yeah?
 
 ##### 11 - I created random data generator named as data_generator.py
          * I used iris dataset, you can change this.
 ##### 12 - I used this module for producer.py
            * same topic, proper ports
 ##### 13 - Then, I used consumer.py
            * same topic, proper ports
            * load_model
            * print result
 ##### 
 # Coming soon....
 ## Send data to MongoDB
