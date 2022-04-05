import numpy as np

def Image_distance(z1,f):
    return z1 * f / (z1 -f)

def distance2alpha(z1,z2,f):
    '''
    Gives order parameter for given z1,z2,f
    z1 - distance from object to CRL (object distance)
    z2 - distance from CRL to detector
    f - focal length of the lens
    '''
    numerator = z1 + z2*(1-z1/f)
    denominator = z1*(1-z2/f)
    z2_cal = Image_distance(z1,f)
    if z2 > z2_cal:
        print('z2 must be less than %.3f'%z2_cal)
    alpha_piby2 = np.arctan2(numerator,denominator)
    alpha = (2/np.pi) * alpha_piby2
    return alpha

def alpha2distance(z1,f,alpha):
    '''
    returns z2 - distance from CRL to detector
    z1 - distance from object to CRL (object distance)
    alpha: FrFT paramater
    f - focal length of the lens
    '''
    k = np.tan(alpha * np.pi/2.)
    numerator = z1*f*(k-1)
    denominator = f + z1*(k-1)
    z2 = float(numerator)/denominator
    return z2
    

z1 = 145.97 # in mm
f = 136.0 ## in mm
print('Imagedistance:',Image_distance(z1,f))
z2 = 1570.0 # in mm 

alpha = distance2alpha(z1,z2,f)
print('Alpha:%.3f'%alpha)
z2 = alpha2distance(z1,f,alpha)
print('z2:%.3f'%z2)
