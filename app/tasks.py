from __future__ import absolute_import, unicode_literals
from .celery import celery


@celery.task
def _add(x, y):
    return x + y


@celery.task
def _multiply(x, y):
    return x * y


@celery.task
def _xsum(numbers):
    return sum(numbers)
