from .celery import app

from celery import group


@app.task
def add(x, y):
    return x + y


# Groups in signatures
@app.task
def sub(x, y):
    group(add.s(3, i) for i in range(10))().get()

    # Partial ones
    grp = group(add.s(i) for i in range(10))
    grp(10).get()


# Chains in signatures
@app.task
def mul(x, y):
    return x * y


# Chords in signatures
@app.task
def div(x, y):
    return x // y
