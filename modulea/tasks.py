from celery import shared_task


@shared_task
def add(x, y):
    return x + y


if __name__ == '__main__':
    a= add.delay(2,1)

    print(a.state)

    print(a.traceback)