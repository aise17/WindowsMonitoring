from celery import Celery, shared_task, Task, task




app = Celery('DjangoSmartiCityDevices', broker='pyamqp://rabbitmq:rabbitmq@localhost/', backend='amqp://rabbitmq:rabbitmq@rabbitmq')



@app.task
def add(x, y):
    return x + y

app.register_task = add

if __name__ == '__main__':
    a= add.delay(2,1)

    print(a.state)
    print(a.get(timeout=10))
    print(a.traceback)
