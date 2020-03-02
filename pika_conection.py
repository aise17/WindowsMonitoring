import sys
import json
import time

import pika
from wmi_handler import Monitor

class SendTask(object):
    queue = 'latidos'
    connection_pika = ''
    channel = ''

    def __init__(self):
        self.connexionUp()


    def connexionUp(self):
        credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
        self.connection_pika = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',
                                                                                 port=5672, virtual_host='/',
                                                                                 credentials=credentials))
        self.channel = self.connection_pika.channel()
        self.channel.queue_declare(queue=self.queue, durable=True)

    def publicar(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(" [x] Sent %r" % message )
        self.connection_pika.close()


if __name__ == '__main__':



    while True:
        monitor = Monitor()
        sendtask = SendTask()
        time.sleep(2.5)
        menssage = monitor.get_result_monitor()

        _json = json.dumps(menssage)
        print(type(_json))
        sendtask.publicar(_json)