import config
import utils
from matplotlib import pyplot as plt
from math import ceil
from classes import (DranSite, DranOptic,
					  FiveGCore, 
					  OranSite, OranDpc, OranOptic)


N_site 	= config.BASE_STATION_AMOUNT
N_years = config.YEARS_PASSED
c_wh 	= config.WATT_HOUR_COST

dran_site = DranSite()   # Зачем передавать классы (даже не экземпляры!) здесь, если можно их 
								   # сразу использовать в классе DranSite  (DONE)
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

TCO_scenario_1_dran = utils.TCO(CAPEX_scenario_1_dran, 
								OPEX_scenario_1_dran, 8)


# ----------- Open RAN

oran_site = OranSite()
oran_dpc  = OranDpc(N_site)

N_dpc = ceil(N_site/19)


L_fronthaul = 3*R + (N_site - 3)*2*R
oran_optic 	= OranOptic(L_fronthaul, 1)

C_oem = oran_site.coem*N_site + oran_dpc.coem + core.coem

CAPEX_scenario_1_oran = 	(oran_dpc.building_cost + 
							oran_dpc.software_cost + 
							oran_dpc.equipment_cost + 
							oran_dpc.comission_works) + \
						N_site*(oran_site.equipment_cost + 
								oran_site.software_cost + 
								oran_site.comission_works) + \
							oran_optic.total_cost + \
							(core.equipment_cost + 
							core.comission_works)

OPEX_scenario_1_oran = (c_wh*oran_dpc.power_per_year + 
							 oran_dpc.rent_per_year + 
							 oran_dpc.software_update_per_year) + \
						N_site*(c_wh*(oran_site.power_per_year) + 
									  oran_site.rent_per_year +
									  oran_site.software_update_per_year) + \
							oran_optic.maintenance_per_year + \
							core.software_update_per_year + \
							c_wh*core.power_per_year + \
							C_oem + C_wages + \
							N_dpc*oran_dpc.rent_per_year


TCO_scenario_1_oran = utils.TCO(CAPEX_scenario_1_oran, 
								OPEX_scenario_1_oran, 8)


print(CAPEX_scenario_1_dran, OPEX_scenario_1_dran)
print(CAPEX_scenario_1_oran, OPEX_scenario_1_oran)

print(TCO_scenario_1_dran.total_cost)
print(TCO_scenario_1_oran.total_cost)

plt.plot(TCO_scenario_1_dran.total_cost, label = 'D-RAN', linestyle = '-.', linewidth = 1.5)
plt.plot(TCO_scenario_1_oran.total_cost, label = 'Open RAN', linestyle = '--', linewidth = 1.5)
plt.title('Total cost of ownership')
plt.ylabel('millions, USD')
plt.xlabel('time, years')
plt.legend()
plt.grid()
plt.show()