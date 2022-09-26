import config


class DranSite:

	def __init__(self, RU, DU, CU):
		self.RU 			= RU
		self.DU 			= DU
		self.CU 			= CU
		self.N_ru 			= 3
		self.coem_percent 	= config.OEM_PERCENT
		self.cw_percent 	= config.COMISSION_WORK_PERCENT
		self.mast_cost 		= config.SITE_MAST_INSTALL
		self.cooling        = config.DRAN_COOLING_BUY_COST
		self.rent_per_year  = config.SITE_RENT_PER_YEAR
		self.cooling_power_per_year = config.DRAN_COOLING_POWER_CONSUMPTION*config.HOURS_PER_YEAR
		self.swu_percent 	= config.SOFTWARE_UPDATE_PERCENT

	def equipment_cost(self):
		return (self.N_ru*self.RU.cost +
			   self.cu_du_cost +
			   self.DU.cpri +
			   self.cooling +
			   self.mast_cost)
		
	equipment_cost = property(equipment_cost)

	@property
	def cu_du_cost(self):
		return self.DU.cost + 0.5*self.CU.cost

	@property
	def comission_works(self):
		return self.cw_percent*(self.N_ru*self.RU.cost +
			   self.cu_du_cost)

	@property
	def coem(self):
		return self.coem_percent*(self.equipment_cost - self.mast_cost)

	@property
	def software_update_per_year(self):
		return self.swu_percent*(self.N_ru*self.RU.cost + self.cu_du_cost)

	@property
	def power_per_year(self):
		usage_coeff = 0.6
		cudu_power_consumption_per_year = config.DRAN_DU_CU_POWER_CONSUMPTION*\
                                              config.HOURS_PER_YEAR

		return usage_coeff*(self.N_ru*self.RU.power_per_year + 
							cudu_power_consumption_per_year + 
							self.cooling_power_per_year)

class RU:
	cost = config.DRAN_RU_BUY_COST
	power_per_year = config.DRAN_RU_POWER_CONSUMPTION*config.HOURS_PER_YEAR

class DU:
	cost = config.DRAN_DU_BUY_COST
	cpri = config.DRAN_CPRI_BUY_COST

class CU:
	cost = config.DRAN_CU_BUY_COST

class FiveGCore:

	def __init__(self):
		self.cooling_cost 	= config.CORE_COOLING_BUY_COST
		self.core_cost 	  	= config.CORE_BUY_COST
		self.cw_percent 	= config.COMISSION_WORK_PERCENT
		self.Coem_percent	= config.OEM_PERCENT
		self.swu_percent 	= config.SOFTWARE_UPDATE_PERCENT
		self.core_power_per_year = config.CORE_POWER_CONSUMPTION*config.CORE_COOLING_POWER_CONSUMPTION	
		self.cooling_power_per_year = config.CORE_COOLING_POWER_CONSUMPTION*config.CORE_COOLING_POWER_CONSUMPTION

	@property
	def equipment_cost(self):
		return self.cooling_cost + self.core_cost

	@property
	def comission_works(self):
		return self.cw_percent*self.equipment_cost

	@property
	def coem(self):
		return self.Coem_percent*self.equipment_cost

	@property
	def software_update_per_year(self):
		return self.swu_percent*self.core_cost

	@property
	def power_per_year(self):
		return self.core_power_per_year + self.cooling_power_per_year

class DranOptic:

	def __init__(self, total_fronthaul_length, total_backhaul_length):
		self.total_fronthaul_length = total_fronthaul_length
		self.total_backhaul_length 	= total_backhaul_length
		self.C_dig_per_km 			= config.OPTIC_1_KM_DIG
		self.C_rol_per_km 			= config.OPTIC_1_KM_ROLL
		self.maintenance_per_year_per_km = config.OPTIC_1_KM_MAINTENANCE

	@property
	def total_cost(self):
		return (self.total_fronthaul_length +
				self.total_backhaul_length)*\
				(self.C_dig_per_km + self.C_rol_per_km)

	@property
	def maintenance_per_year(self):
		return (self.total_fronthaul_length +
				self.total_backhaul_length)*\
				(self.maintenance_per_year_per_km)


class OranSite:

	def __init__(self, RU):
		self.RU = RU