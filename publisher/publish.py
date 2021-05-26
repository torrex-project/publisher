#!/usr/bin/env python

import os
import time

import pika
import fileinput


RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
RABBITMQ_USER = os.environ.get("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD")
RABBITMQ_QUEUE = os.environ.get("RABBITMQ_QUEUE", "torrex-raw")

RABBITMQ_DURABLE = True
RABBITMQ_DELIVERY_MODE = 2

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
)
channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE, durable=RABBITMQ_DURABLE)

for line in fileinput.input():
    if line == "running, it may take a few minutes...":
        continue
    try:
        message = str(int(time.time())) + ";" + line
        channel.basic_publish(
            exchange='',
            routing_key=RABBITMQ_QUEUE,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=RABBITMQ_DELIVERY_MODE,
            )
        )
        print(message)
    except:
        pass

connection.close()
