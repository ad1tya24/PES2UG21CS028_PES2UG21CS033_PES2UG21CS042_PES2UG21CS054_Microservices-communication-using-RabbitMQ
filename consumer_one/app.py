from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify(status='ok')

# Example endpoint for receiving messages from RabbitMQ
@app.route('/receive_message')
def receive_message():
    # Logic to receive a message from RabbitMQ
    # This logic might involve using a library like pika to consume messages from RabbitMQ
    # Example code:
    import pika
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    method_frame, header_frame, body = channel.basic_get(queue='my_queue')
    
    if method_frame:
        message = body.decode('utf-8')
        return jsonify(message=message)
    else:
        return jsonify(message='No message available')

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')