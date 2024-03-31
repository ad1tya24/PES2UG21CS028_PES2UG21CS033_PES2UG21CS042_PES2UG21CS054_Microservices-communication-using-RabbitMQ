from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify(status='ok')

# Example endpoint for sending a message to RabbitMQ
@app.route('/send_message')
def send_message():
    # Logic to send a message to RabbitMQ
    # This logic might involve using a library like pika to publish messages to RabbitMQ
    # Example code:
    import pika
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    channel.basic_publish(exchange='', routing_key='my_queue', body='Hello, RabbitMQ!')
    connection.close()
    
    return jsonify(message='Message sent to RabbitMQ')

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')