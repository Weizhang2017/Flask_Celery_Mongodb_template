import requests

class Test:
	def add_test():
		r = requests.post(
						'http://127.0.0.1:5000/add/',
						json={'1':3, '2':4}
						).json()
		print(r)

if __name__ == '__main__':
	Test.add_test()
