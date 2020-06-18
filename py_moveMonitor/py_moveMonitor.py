import math
class moveMonitor:
	def __init__(self, critical_delta, windows_critical):
		self.critical_delta = critical_delta
		self.windows_critical = windows_critical
		self.first_in = True
		self.is_stop = True
		self.is_moving = False
		self.stop_cycle = 0
		self.odo_sum = 0
		self.odo_window_counter = 0
		self.odo_time_window_data = []
		for i in range(0,50):
			self.odo_time_window_data.append(0.0)

	def update(self, encoder_cnt):
		if self.first_in:
			self.first_in = False
			self.last_cnt = encoder_cnt
			return False
		
		# //data filter.
		# //give up encoder data with large noise.
		if(math.fabs(encoder_cnt - self.last_cnt) > 2000000):
			# Message::Instance()->postMsg("encoder of driver%d value jumps too large : %d !!!", _canID, _encoderCnt);
			self.last_cnt = encoder_cnt
			return False
		
		self.is_moving = False
		is_wheel_rotate = False
		delta_cnt = encoder_cnt - self.last_cnt
		self.last_cnt = encoder_cnt
		
		if(math.fabs(delta_cnt) > self.critical_delta):
			is_wheel_rotate = True
			self.is_stop = False
			self.stop_cycle = 0

		# // check the sum
		self.odo_sum = self.odo_sum - self.odo_time_window_data[self.odo_window_counter] + delta_cnt

		# // replace by new value
		self.odo_time_window_data[self.odo_window_counter] = delta_cnt

		# // check if the vehicle is moving
		if math.fabs(self.odo_sum) > self.windows_critical:
			self.is_moving = True

		# // run the counter
		self.odo_window_counter = self.odo_window_counter + 1
		if (self.odo_window_counter >= 50):
		 	self.odo_window_counter = 0

		if(not is_wheel_rotate):
			if self.stop_cycle >= 20:
				self.stop_cycle = 20
			else:
				self.stop_cycle = self.stop_cycle + 1

			if self.stop_cycle >= 20:
				self.is_stop = True

		return (self.is_stop and (not self.is_moving))


class calcCriticalBase:
	def __init__(self, encorderline, reduction_ratio, radius):
		self.encorderline = encorderline
		self.reduction_ratio = reduction_ratio
		self.radius = radius
		self.scale = encorderline * 4.0 * reduction_ratio / (2.0 * math.pi * radius)

	def getCritical(self):
		pass

	def getCriticalWindow(self):
		pass

class calcCriticalWalk(calcCriticalBase):
	def getCritical(self):
		self.critical = self.scale * 0.000015
		return self.critical

	def getCriticalWindow(self):
		self.critical_window = self.getCritical() * 5.0
		return self.critical_window 

if __name__ == "__main__":
    tt = calcCriticalWalk(8000.0, 20.0, 0.09)
    print(tt.getCritical())
    print(tt.getCriticalWindow())