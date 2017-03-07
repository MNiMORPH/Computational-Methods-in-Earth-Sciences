import ulmo
import numpy as np
from datetime import datetime as dt
from matplotlib import pyplot as plt

SITE_ID = '05211000'
Q_daily_code = '00060:00003'

usgs_gauge = ulmo.usgs.nwis.get_sites(sites=SITE_ID)[SITE_ID]

daily_request = ulmo.usgs.nwis.get_site_data(SITE_ID, service="daily", period="all")
daily_discharge = daily_request[Q_daily_code]['values']
Q = []
t = []
for row in daily_discharge:
  Q.append( float(row['value']) )
  t.append( dt.strptime(row['datetime'], '%Y-%m-%dT%H:%M:%S') )

Q = np.array(Q)
t = np.array(t)

nodata_value = float(daily_request.values()[0]['variable']['no_data_value'])

t = t[Q != nodata_value]
Q = Q[Q != nodata_value]

plt.ion()
plt.figure(figsize=(18,8))
plt.plot(t, Q, 'k-', linewidth=2)
plt.title(usgs_gauge['name'], fontsize=30)
plt.xlabel('Date', fontsize=20)
#plt.ylabel('Daily mean discharge [cfs]', fontsize=20)
plt.ylabel(daily_request.values()[0]['variable']['name'], fontsize=20)
plt.tight_layout()

