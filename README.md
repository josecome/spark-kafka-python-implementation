# Kafka-python-implementation
This project aim to demostrate implementation of kafka (with Flask and Spark) in real world using Python environment

## What is Kafka
Kafka is used for data integration through real-time streaming data pipelines 

## Installation
Download and install JDK: https://docs.oracle.com/en/java/javase/11/install/installation-jdk-microsoft-windows-platforms.html

Download and extract Kafka: https://kafka.apache.org/downloads
Copy and put in `C:`, rename the folder to kafka

## Configuration
Go to `zookeeper.proprieties` and set path for zookeeper log files
Go to `server.proprieties` and set path for kafka log files

## Running Zookeeper and Kafka
First run Zookeeper, in Commandline go to where you installed kafka:
#### `cd C:\kafka`
#### `C:\kafka>.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`

Run Kafka
#### `cd C:\kafka\bin\windows`
#### `C:\kafka\bin\windows>kafka-server-start.bat C:\kafka\config\server.properties`

## Testing Kafka
Producer
#### `C:\kafka\bin\windows>kafka-console-producer.bat --topic TEST-TOPIC --broker-list localhost:9092`
`>Test Message`

Consumer
#### `kafka-console-producer.bat --topic my_favorite_topic --broker-list localhost:9092`
`>Test Message`

Now run Flask project by type in Commandline:
#### `py run.py`

App will be running on [http://127.0.0.1:5002/form]