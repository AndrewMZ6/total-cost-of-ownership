import config
import utils
from matplotlib import pyplot as plt
from classes import ( RU, DU, CU,
					  DranSite, DranOptic,
					  FiveGCore )

N_site 	= config.BASE_STATION_AMOUNT
N_years = config.YEARS_PASSED
c_wh 	= config.WATT_HOUR_COST

dran_site = DranSite(RU, DU, CU)
core = FiveGCore()


assert N_site >= 3, 'N_site must be 3 or more'

C_oem = dran_site.coem*N_site + core.coem
N_staff = 1
C_wages = 12*config.WAGE_PER_MONTH*N_staff

R = config.BASE_STATION_COVER_RADIUS
L_backhaul = 3*R + (N_site - 3)*2*R

dran_optic = DranOptic(0, L_backhaul)


CAPEX_scenario_1_dran = N_site*(dran_site.equipment_cost +
							dran_site.comission_works) + \
						(dran_optic.total_cost + 
						core.equipment_cost + 
						core.comission_works)

OPEX_scenario_1_dran = N_site*(c_wh*(dran_site.power_per_year) +
							dran_site.rent_per_year +
							dran_site.software_update_per_year) + \
					   dran_optic.maintenance_per_year + \
					   core.software_update_per_year + \
					   c_wh*(core.power_per_year) + \
					   C_oem + C_wages

TCO_scenario_1 = utils.TCO(CAPEX_scenario_1_dran, 
				OPEX_scenario_1_dran, 8)













# comment






plt.plot(TCO_scenario_1.total_cost, label = 'D-RAN', linestyle = '-.', linewidth = 1.5)
plt.plot(list(range(9)), label = 'Open RAN', linestyle = '--', linewidth = 1.5)
plt.title('Total cost of ownership')
plt.ylabel('millions, USD')
plt.xlabel('time, years')
plt.legend()
plt.grid()
plt.show()