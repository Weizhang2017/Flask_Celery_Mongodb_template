from __future__ import absolute_import, unicode_literals
from celery import Celery
from app_config import config

celery = Celery(
			'app',
             broker=config['development'].broker_url,
             backend=config['development'].result_backend,
             include=config['development'].worker_module
             )

# Optional configuration, see the application user guide.
celery.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    celery.start()
