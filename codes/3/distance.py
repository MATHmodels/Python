from math import *
def distance(phii,thetai, phij,thetaj, R=6371):
    phii = phii/180*pi
    thetai = thetai/180*pi
    phij = phij/180*pi
    thetaj = thetaj/180*pi

    d = R*acos(sin(phii)*sin(phij) + cos(phii)*cos(phij)*cos(thetai-thetaj))
    return d

d = distance(39.9, 116.41, 40.71,-74.01)
print('d = %d km' % d)
