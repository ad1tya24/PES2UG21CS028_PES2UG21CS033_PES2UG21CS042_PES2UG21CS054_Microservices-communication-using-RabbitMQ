import mysql.connector
import pika 
import time

def connect_to_rabbitmq():
    connection = None
    while connection is None:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ is not ready. Waiting to retry...")
            time.sleep(5)  # wait for 5 seconds before trying to connect again
    return connection

def check_mysql():
    try:
        mysql_connection = mysql.connector.connect(host='mysql_host', user='root', password='password')
        mysql_connection.close()
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

connection = connect_to_rabbitmq()
channel = connection.channel()  # Create a new channel with the next available channel number.

check_mysql()

channel.exchange_declare(exchange='exchange', exchange_type='direct')
channel.queue_declare(queue='health check')

channel.queue_bind(exchange='exchange', queue='health check', routing_key='health check')

print("Waiting for messages... press CTRL+C to exit")

def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    print(f"Received message: {body}")

channel.basic_consume(queue='health check', on_message_callback=callback, auto_ack=True)
channel.start_consuming()