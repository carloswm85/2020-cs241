class Time:
  def __init__(self):
    self._hour = 0
    self._min = 0
    self._sec = 0

	def get_hour(self):
		return self._hour

	def set_hour(self, value):
		if value > 23:
			self._hour = 23
		elif value < 0:
			self._hour = 0
		else:
			self._hour = value
	
	def get_min(self):
		return self._min

	def set_min(self, value):
    if value > 59:
      self._min = 60
    elif value < 0:
      self._min = 0
    else:
		  self._min = value
	
	def get_sec(self):
		return self._sec

	def set_sec(self, value):
    if value > 59:
      self._sec = 60
    elif value < 0:
      self._sec = 0
    else:
		  self._sec = value
		

def main():
	clock = Time()
	
	hour = int(input('Enter hours: '))
	min = int(input('Enter minutes: '))
	sec = int(input('Enter seconds: '))

	clock.set_hour(hour)
  clock.set_min(min)
  clock.set_sec(sec)

	print(clock.get_hour())
	print(clock.get_min())
	print(clock.get_sec())
	

if __name__ == '__main__':
	main()



	