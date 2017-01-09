
class Observer(object):
	# Represents each Observer (subscriber) that is monitoring changes in the subject
	# class variable used as counter
	observer_id_tracker = 0

	def __init__(self, stock_grabber):
		self.stock_grabber = stock_grabber
		Observer.observer_id_tracker += 1
		self.observer_id = Observer.observer_id_tracker
		self.ibm_price = None
		self.appl_price = None
		self.goog_price = None

		print ("New observer", self.observer_id)
		stock_grabber.register(self)

	def update(self, ibm_price, appl_price, goog_price):
		self.ibm_price = ibm_price
		self.appl_price = appl_price
		self.goog_price = goog_price

		print("IBM, APPL, GOOG: ", self.ibm_price, self.appl_price, self.goog_price)


class StockGrabber(object):
	# This is our subject (publisher) class. We will maintain a list of dependents.
	# Changes are done here and observers (subscribers) are notified.

	def __init__(self):
		# list of observers
		self.observers = []

		# Default price
		self.ibm_price = None
		self.appl_price = None
		self.goog_price = None

	def register(self, observer):
		self.observers.append(observer)

	def unregister(self, observer):
		self.observers.remove(observer)
		print("Deleted observer", observer.observer_id)

	def notify_observer(self):
		for observer in self.observers:
			observer.update(self.ibm_price, self.appl_price, self.goog_price)

	def set_ibm_price(self, ibm_price):
		self.ibm_price = ibm_price
		self.notify_observer()

	def set_appl_price(self, appl_price):
		self.appl_price = appl_price
		self.notify_observer()
	
	def set_goog_price(self, goog_price):
		self.goog_price = goog_price
		self.notify_observer()

def main():
	# This is our driver program

	stockgrabber = StockGrabber()
	observer1 = Observer(stockgrabber)

	stockgrabber.set_ibm_price(150)
	stockgrabber.set_appl_price(700)
	stockgrabber.set_goog_price(800)

	observer2 = Observer(stockgrabber)

	stockgrabber.set_ibm_price(155)
	stockgrabber.set_appl_price(705)
	stockgrabber.set_goog_price(805)

	stockgrabber.unregister(observer1)

	stockgrabber.set_ibm_price(160)
	stockgrabber.set_appl_price(710)
	stockgrabber.set_goog_price(810)


if __name__ == '__main__':
	main()

