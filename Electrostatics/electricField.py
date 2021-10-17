from math import pi, sin
from numpy import Infinity
import calculationConstants
import scipy.integrate as integrate
import scipy.misc as diff
import Electrostatics.electricPotential as potential

k = 1/(4*pi*calculationConstants.vaccumPermittivity)


def dueToPointCharge(charge, distance):
    if distance == 0:
        return Infinity
    else:
        return (k * charge)/(pow(distance, 2))


class Sphere:
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
                electricField = integrate.quad(
                    integrand, 0, distanceFromCenter)[0]
        return electricField

    def dueToUniformNonConductingSphere(linearChargeDensity, radiusOfSphere, distanceFromCenter):
        def chargeDensityFunction(x):
            return linearChargeDensity
        return Sphere.dueToNonConductingSphere(chargeDensityFunction, radiusOfSphere, distanceFromCenter)

    def dueToConductingSphere(surfaceChargeDensity, radiusOfSphere, distanceFromCenter):
        if distanceFromCenter < radiusOfSphere:
            electricField = 0
        else:
            chargeEnclosed = surfaceChargeDensity * \
                (4 * pi * (radiusOfSphere**2))
            electricField = k * chargeEnclosed / (distanceFromCenter**2)
        return electricField


class LineCharge:
    def dueToUniformLineCharge(linearChargeDensity, angleSubtendedA, angleSubtentedB, perpendicularDistanceFromBody):
        if perpendicularDistanceFromBody == 0:
            raise Exception(
                'Electric field is not defined for a point on the line charge itself')
        return k * linearChargeDensity * (sin(angleSubtendedA)+sin(angleSubtentedB))/perpendicularDistanceFromBody

    def dueToUniformInfiniteLineCharge(chargeDensity, perpendicularDistanceFromBody):
        return LineCharge.dueToUniformLineCharge(chargeDensity, pi/2, pi/2, perpendicularDistanceFromBody)


class Ring:
    def dueToUniformlyChargedRingOnAxis(linearChargeDensity, radiusOfRing, distanceFromCenter):
        # Using E(x) = -dV/dx (or one can directly use formula from books)

        def f(x):
            return -potential.Ring.dueToUniformlyChargedRingOnAxis(linearChargeDensity, radiusOfRing, x)
        return diff.derivative(f, distanceFromCenter, dx=10**-5)


class Disk:
    def dueToUniformlyChargedDiskOnAxis(chargeDensity, radiusOfDisk, distanceFromCenter):
        def f(x):
            return -potential.Disk.dueToUniformlyChargedDiskOnAxis(chargeDensity, radiusOfDisk, x)
        return diff.derivative(f, distanceFromCenter, dx=10**-5)
