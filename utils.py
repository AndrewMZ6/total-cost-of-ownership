#from matplotlib import pyplot as plt

class TCO:

	def __init__(self, CAPEX, OPEX, N_years):
		self.CAPEX 		= CAPEX
		self.OPEX  		= OPEX
		self.N_years 	= N_years

	@property
	def total_cost(self):
		total_cost = list()
		for year in range(self.N_years + 1):
			total_cost.append((self.CAPEX + self.OPEX*year)/1e6)
		
		return total_cost

	#@classmethod