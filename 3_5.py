"""
Objectives
improve the student's skills in defining, using and testing functions.
Scenario
A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers. In the USA it is shown as the number of miles travelled by car using one gallon of fuel.

Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

The functions:

are named l100kmtompg and mpgtol100km respectively;
take one argument (the value corresponding to their names)
Complete the code presented below.

Run your code and check whether your output is the same as ours.

Well, you will surely need this:

1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757
"""

"""
1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
"""

def l100kmtompg(litres): 
    convertToMPG = 1/(litres / 3.785411784 * .01609344) 
    return convertToMPG


def mpgtol100km(miles):
    convertToL100Km = 1 / (miles /3.785411794 * .01609344) 
    return convertToL100Km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))