import geopandas as gpd
import matplotlib.pyplot as plt
import pathlib

f = pathlib.Path('./all.geojson')

gdf = gpd.read_file(f)
print(gdf.Address[0])

for i in gdf:
    arr = [gdf["Route"], gdf["Address"], gdf["Account Number"], gdf["Meter Number"]]

print(arr)
gdf.to_csv("/Users/jtylerstahl/Documents/Code/PythonGeoJSON/addresses.csv")


