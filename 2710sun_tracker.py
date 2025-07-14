from astral import LocationInfo
from astral.sun import elevation, azimuth
from datetime import datetime, timezone, timedelta

city = LocationInfo("Seoul", "South Korea", "Asia/Seoul", 37.5665, 126.9780)

now = datetime.now(timezone(timedelta(hours=9)))

alt = elevation(city.observer, now)
az = azimuth(city.observer, now)

print(f"현재 시간: {now.strftime('%Y-%m-%d %H:%M')}")
print(f"태양 고도: {alt:.2f}°")
print(f"태양 방위각: {az:.2f}°")
import matplotlib.pyplot as plt
import numpy as np

r = 90 - alt
theta = np.radians(az)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_rlim(90, 0)
ax.plot(theta, r, 'o', color='orange', markersize=15)
ax.set_title("태양 위치 (고도/방위각)")
plt.show()
