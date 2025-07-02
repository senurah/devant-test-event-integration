import pika
import json

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 5672  # Custom port
queue_name = 'order_queue'

# Message to send
message = {
    "order_id": "12345",
    "customer_name": "John Doe",
    "product": "Widget",
    "quantity": 10,
    "total_amount": 100.00
}

try:
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port)
    )
    channel = connection.channel()

    # Declare the queue (idempotent operation)
    channel.queue_declare(queue=queue_name, durable=True)

    # Publish the message
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2  # Make message persistent
        )
    )

    print(f"Message sent to queue '{queue_name}': {message}")

    # Close the connection
    connection.close()

except Exception as e:
    print(f"Failed to send message: {e}")
