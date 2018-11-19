class Config:
	broker_url = 'amqp://localhost'
	result_backend = 'mongodb://localhost:27017'
	worker_module = ['app.tasks']


class DevelopmentConfig(Config):
	DEBUG = True
	LOG_FILE = 'development.log'


class ProductionConfig(Config):
	pass

config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
