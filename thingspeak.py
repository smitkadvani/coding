import httplib
import urllib2
#hq = httplib.HTTPConnection('https://api.thingspeak.com/update?api_key=FY52UTY60ED4I2AS&field1=0')
#URL = "http://api.thingspeak.com/update?key=FY52UTY60ED4I2AS&field1=333"
i=0
for i to 100:
    f = urllib2.urlopen('https://api.thingspeak.com/update?api_key=FY52UTY60ED4I2AS&field1=0')
print "smot"
