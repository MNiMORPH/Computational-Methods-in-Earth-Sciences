# Using Ulmo for all of the gauges along the Mississippi

"""
url = 'http://hydroportal.cuahsi.org/nwisdv/cuahsi_1_1.asmx?WSDL'

csites = ulmo.cuahsi.wof.get_sites(url)

Mississippi_Gauges = []

for k in csites:
  v = csites[k]
  if 'MISSISSIPPI R' in v['name']:
     Mississippi_Gauges.append(k)
     
for k in Mississippi_Gauges:
  ulmo.cuahsi.wof.get_values(wsdl_url=url, site_code=k, variable_code
"""

import ulmo
import pandas as pd
import numpy as np

UMR_HUC = '07'
Q_daily_code = '00060:00003'

usgs_gauges = ulmo.usgs.nwis.get_sites(huc=UMR_HUC)

Mississippi_Gauges = []

for k in usgs_gauges:
  v = usgs_gauges[k]
  if 'MISSISSIPPI R' in v['name']:
     Mississippi_Gauges.append(k)

for gauge in Mississippi_Gauges:
  print gauge, usgs_gauges[gauge]['name']

Q_mean = []
lat = []
lon = []
HUC = []
ID = []
LenRecord = []
for gauge in Mississippi_Gauges:
  try:
    tmp = ulmo.usgs.nwis.get_site_data(gauge, service="daily", period="all")
    tmp2 = tmp['00060:00003']
    tmp3 = tmp2['values']
    tmplist = []
    for item in tmp3:
      tmplist.append(float(item['value']))
    tmplist = np.array(tmplist)
    Q_mean.append(np.mean(tmplist[tmplist>0]) * 0.0283168466) # ft3/s to m3/s
    lat.append(tmp2['site']['location']['latitude'])
    lon.append(tmp2['site']['location']['longitude'])
    HUC.append(tmp2['site']['huc'])
    ID.append(gauge)
    LenRecord.append(len(tmplist[tmplist>0]))
  except:
    pass
    """
    Q_mean.append(np.nan)
    lat.append(np.nan)
    lon.append(np.nan)
    HUC.append(np.nan)
    ID.append(gauge)
    """

out = np.array([ID, lat, lon, HUC, Q_mean, LenRecord]).transpose()
# Add drainage area in km2 by hand, from
# https://water.usgs.gov/GIS/huc_name.html
np.savetxt('MississippiQA.csv', out, delimiter=',', fmt='%s')

