from math import pi
from numpy import Infinity
import calculationConstants
import Electrostatics.electricField as Ef
import scipy.integrate as integrate

k = pow((4*pi*calculationConstants.vaccumPermittivity), -1)


def dueToPointCharge(charge, distance):
    if distance == 0:
        return Infinity
    else:
        return (k * charge)/distance

# dV = -E.dr (when E vector exist only in direction of dr vector)


def dueToNonConductingSphere(chargeDensityFunction, radiusOfSphere, distanceFromCenter):
    def integrand(x):
        return chargeDensityFunction(x)*4*pi*(x**2)
    totalEnclosedCharge = integrate.quad(
        integrand, 0, radiusOfSphere)[0]
    if distanceFromCenter >= radiusOfSphere:
        # for point outside or on the sphere
        return k * totalEnclosedCharge / distanceFromCenter
    else:
        potentialAtSurface = k * totalEnclosedCharge / radiusOfSphere

        def integrand(x):
            return Ef.dueToNonConductingSphere(
                chargeDensityFunction, radiusOfSphere, x)
        excessPotential = integrate.quad(
            integrand, distanceFromCenter, radiusOfSphere)[0]
        # Potential at point inside sphere - Potential at surface = - integral(E.dx) from x to R
        potentialAtPointInside = potentialAtSurface + excessPotential
        return potentialAtPointInside


def dueToUniformNonConductingSphere(linearChargeDensity, radiusOfSphere, distanceFromCenter):
    def chargeDensityFunction(x):
        return linearChargeDensity
    return dueToNonConductingSphere(chargeDensityFunction, radiusOfSphere, distanceFromCenter)


def dueToSymmetericLineCharge(linearChargeDensity, angleSubtended, perpendicularDistanceFromBody):
    # IT IS NOT AT ALL AN ABSOLUTE QUANTITY
    # when angleSubtendedA = angleSubtendedB
    # limitation as Electric field won't be in direction
    # perpendicular to the charged body in other case
    # or E vector doesn't align with dr vector
    def integrand(x):
        return Ef.dueToUniformLineCharge(
            linearChargeDensity, angleSubtended, angleSubtended, x)
    referencePotential = 0
    # assuming potential at x=Infinity to be zero (which maybe treated as wrong)
    excessPotential = integrate.quad(
        integrand, perpendicularDistanceFromBody, Infinity)[0]
    return referencePotential + excessPotential


def dueToConductingSphere(surfaceChargeDensity, radiusOfSphere, distanceFromCenter):
    totalChargeEnclosed = surfaceChargeDensity * 4 * pi * (radiusOfSphere**2)
    if distanceFromCenter > radiusOfSphere:
        potential = k * totalChargeEnclosed / distanceFromCenter
    else:
        # E = 0 so V=constant=V surface
        potential = k * totalChargeEnclosed / radiusOfSphere
    return potential
