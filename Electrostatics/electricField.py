from math import pi , sin
from numpy import Infinity
import calculationConstants
import scipy.integrate as integrate

k = pow((4*pi*calculationConstants.vaccumPermittivity), -1)


def dueToPointCharge(charge, distance):
    if distance == 0:
        return Infinity
    else:
        return (k * charge)/(pow(distance, 2))


def dueToNonConductingSphere(chargeDensityFunction, radiusOfSphere, distanceFromCenter):
    if min(radiusOfSphere, distanceFromCenter) == 0:
        electricField = 0
    else:
        if distanceFromCenter > radiusOfSphere:
            def integrand(x):
                return chargeDensityFunction(x)*4*pi*(x**2)
            totalEnclosedCharge = integrate.quad(
                integrand, 0, radiusOfSphere)[0]
            electricField = k*totalEnclosedCharge/(distanceFromCenter**2)
        else:
            def integrand(x):
                return k * chargeDensityFunction(x)*4*pi*(x**2)/(distanceFromCenter**2)
            electricField = integrate.quad(integrand, 0, distanceFromCenter)[0]
    return electricField


def dueToUniformNonConductingSphere(linearChargeDensity, radiusOfSphere, distanceFromCenter):
    def chargeDensityFunction(x):
        return linearChargeDensity
    return dueToNonConductingSphere(chargeDensityFunction, radiusOfSphere, distanceFromCenter)


def dueToUniformLineCharge(linearChargeDensity, angleSubtendedA, angleSubtentedB, perpendicularDistanceFromBody):
    if perpendicularDistanceFromBody == 0:
        raise Exception(
            'Electric field is not defined for a point on the line charge itself')
    return k * linearChargeDensity * (sin(angleSubtendedA)+sin(angleSubtentedB))/perpendicularDistanceFromBody


def dueToUniformInfiniteLineCharge(chargeDensity, perpendicularDistanceFromBody):
    return dueToUniformLineCharge(chargeDensity, pi/2, pi/2, perpendicularDistanceFromBody)


def dueToConductingSphere(surfaceChargeDensity, radiusOfSphere, distanceFromCenter):
    if distanceFromCenter < radiusOfSphere:
        electricField = 0
    else:
        chargeEnclosed = surfaceChargeDensity * \
            (4 * pi * (radiusOfSphere**2))
        electricField = k * chargeEnclosed / (distanceFromCenter**2)
    return electricField
