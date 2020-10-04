import requests
from datetime import datetime
front="https://www.n2yo.com/rest/v1/satellite/positions/"
end="/2/&apiKey=3J8GBR-WYHM3S-JHNLDD-4KER"
ID="25544/"  # satellite ID
# observer position information
obslatitude="41.702/"
obslongitude="-76.014/"
obsaltitude="0"
url=front+ID+obslatitude+obslongitude+obsaltitude+end
# url="https://www.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2/&apiKey=3J8GBR-WYHM3S-JHNLDD-4KER"
r=requests.get(url)

raw_json=r.json()
timestamp = raw_json["positions"][0]["timestamp"]
ts = int(timestamp)
time=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

satname=raw_json["info"]["satname"]
satlatitude=raw_json["positions"][0]["satlatitude"]
satlongitude=raw_json["positions"][0]["satlongitude"]
sataltitude=raw_json["positions"][0]["sataltitude"]

print("time: "+time)
print("satname: "+satname)
print("latitude: "+str(satlatitude))
print("longitude: "+str(satlongitude))
print("altitude: "+str(sataltitude))
