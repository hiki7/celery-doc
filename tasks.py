from celery import Celery

#the first argument is the name of the module/file, it's needed so that names can be automatically generated
#when the tasks are define in __main__

#the second argument is the broker keyword argument, specifying the url of the message broker
app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def add(x, y):
    return x + y