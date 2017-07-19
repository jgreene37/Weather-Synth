####################################################################################################################
####################################################################################################################
#     Weather Synth  0.1
#
#     API SCRAPE
#import the requests library
import requests

#import the json library

import json

#import the math plot lib
import matplotlib.pyplot as plt
#5 day, 3 hour increment data request
#Request weather info for Atlanta (city code4180439) in JSON format, imperial units and add API KEY

#response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=4180439&mode=JSON&units=imperial&APPID=399358a30ccc7fc4bd37c778a5967cc5")

#Current Data request
response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=4180439&mode=JSON&units=imperial&APPID=399358a30ccc7fc4bd37c778a5967cc5")

#print request status

status_code = response.status_code
print(status_code)

#extract list of weather data, starting with temperature
json_data = response.json()

#5 hour data set manipulation#######################################################

#weather_data = json_data["list"]
#ll = len(weather_data)


#temp_dat = [0] * ll
#for i in xrange(0, ll):
 #   temp_dat[i] = weather_data[i]["main"]['temp']

#print(temp_dat)

#plot temperature values
#plt.plot(temp_dat)
#plt.show()
##############################################################################

#Current Data Manipulation##########################################################
#
#current temp in Fahrenheit
tc = json_data["main"]['temp']
print(tc)
#current humidity
hu = json_data["main"]['humidity']
print(hu)
#current pressure
pres = json_data["main"]['pressure']
print(pres)
#current wind speed
wind = json_data["wind"]['speed']
print(wind)
#current clouds
cloud = json_data["clouds"]['all']
print(cloud)

############################################################################


#extract weather details from data
#weather_desc = weather_data["weather"][0]["description"]
#print(weather_desc)



#w_string = json.dumps(json_data["list"][0]["wind"])
#print(w_string)




#######################################################################################################################
#     PYO MUSIC SYNTHESIS



from pyo import *
s = Server(duplex=0).boot()
s.amp = 0.1
wf = wind *.1
tf = tc *.01
hf = hu *.01
cf = cloud * .001
# Creates a noise source
#n = Noise()
#create a major chord
n = Sine(freq=440)+Sine(freq=554.37)+Sine(freq=659.25)

# Creates an LFO oscillating +/- 500 around Pressure (filter's frequency)
lfo1 = Sine(freq=wf, mul=500, add=pres)
# Creates an LFO oscillating between 2 and 8 (filter's Q)
lfo2 = Sine(freq=tf).range(2, 8)
# Creates a dynamic bandpass filter applied to the noise source
bp1 = ButBP(n, freq=lfo1, q=lfo2).out()

# The LFO object provides more waveforms than just a sine wave

# Creates a ramp oscillating +/- 1000 around 12000 (filter's frequency)
lfo3 = LFO(freq=hf, type=1, mul=pres, add=1200)
# Creates a square oscillating between 4 and 12 (filter's Q)
lfo4 = LFO(freq=4, type=2).range(4, 12)
# Creates a second dynamic bandpass filter applied to the noise source
bp2 = ButBP(n, freq=lfo3, q=lfo4).out(1)

#create cloud noise
cnL = Noise(mul=cf).out(0)
cnR = Noise(mul=cf).out(1)
s.gui(locals())
