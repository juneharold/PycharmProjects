import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


birddata = pd.read_csv("/Users/harold/PycharmProjects/UPFR/bird_migration/bird_tracking.csv")


ix = birddata.bird_name == "Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize=(7, 7))
plt.plot(x, y, ".")


bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.legend(loc="lower right")
"""plt.savefig("3traj.pdf")"""


ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind])
"""plt.savefig("hist.pdf")"""

plt.figure(figsize=(8, 4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20))
plt.xlabel("2D speed(m/s)")
plt.ylabel("Frequency")

birddata.speed_2d.plot(kind="hist", range=[0, 30])
plt.xlabel("2D speed")
"""plt.savefig("pd_hist.pdf")"""


date_str = birddata.date_time[0]
type(date_str)
datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []
for k in range(0, len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))


birddata["timestamp"] = pd.Series(timestamps, index=birddata.index)

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]

plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observations")
plt.ylabel("Elapsed time (days)")
"""plt.savefig("timeplot.pdf")"""


elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for i, t in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(birddata.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/sl)")
plt.show()
"""plt.savefig("dms.pdf")"""




