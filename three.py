
import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, sqrt

np.random.seed(13531)
coordinates = (np.random.rand(3_000_000, 4) - .5) * 360
df = pd.DataFrame(coordinates, columns=["lat_1", "lon_1", "lat_2", "lon_2"])



def formula(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # print(lat1, ", ", lon1, ", ", lat2, ", ", lon2)

    r = 6371  # km
    pt1 = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
    pt2 = 2 * asin(sqrt(pt1))
    final = pt2 * r

    # print(final)
    return final


def haversine():
    count = df['lat_1'].count()
    # count = 1

    distance = []
    for i in range(count):
        row = formula(df['lat_1'][i], df['lon_1'][i], df['lat_2'][i], df['lon_2'][i])
        distance.append(row)

    return distance


distances = haversine()

print(hash(tuple(distances)))
