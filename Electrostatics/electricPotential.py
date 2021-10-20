from math import pi
from numpy import Infinity, sign
import calculationConstants
import Electrostatics.electricField as Ef
import scipy.integrate as integrate

k = 1/(4*pi*calculationConstants.vaccumPermittivity)


def dueToPointCharge(charge, distance):
    if distance == 0:
        print('WARNING : Electric field/potential on the charge itself will be undefined')
        return sign(charge)*Infinity
    else:
        return (k * charge)/distance

# dV = -E.dr (when E vector exist only in direction of dr vector)


class Sphere:
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
                return Ef.Sphere.dueToNonConductingSphere(
                    chargeDensityFunction, radiusOfSphere, x)
            excessPotential = integrate.quad(
                integrand, distanceFromCenter, radiusOfSphere)[0]
            # Potential at point inside sphere - Potential at surface = - integral(E.dx) from x to R
            potentialAtPointInside = potentialAtSurface + excessPotential
            return potentialAtPointInside

    def dueToConductingSphere(surfaceChargeDensity, radiusOfSphere, distanceFromCenter):
        totalChargeEnclosed = surfaceChargeDensity * \
            4 * pi * (radiusOfSphere**2)
        if distanceFromCenter > radiusOfSphere:
            potential = k * totalChargeEnclosed / distanceFromCenter
        else:
            # E = 0 so V=constant=V surface
            potential = k * totalChargeEnclosed / radiusOfSphere
        return potential

    def dueToUniformNonConductingSphere(linearChargeDensity, radiusOfSphere, distanceFromCenter):
        def chargeDensityFunction(x):
            return linearChargeDensity
        return Sphere.dueToNonConductingSphere(chargeDensityFunction, radiusOfSphere, distanceFromCenter)


class LineCharge:
    def dueToSymmetericLineCharge(linearChargeDensity, angleSubtended, perpendicularDistanceFromBody):
        # IT IS NOT AT ALL AN ABSOLUTE QUANTITY
        # when angleSubtendedA = angleSubtendedB
        # limitation as Electric field won't be in direction
        # perpendicular to the charged body in other case
        # or E vector doesn't align with dr vector
        def integrand(x):
            return Ef.LineCharge.dueToUniformLineCharge(
                linearChargeDensity, angleSubtended, angleSubtended, x)
        referencePotential = 0
        # assuming potential at x=Infinity to be zero (which maybe treated as wrong)
        excessPotential = integrate.quad(
            integrand, perpendicularDistanceFromBody, Infinity)[0]
        return referencePotential + excessPotential

    def dueToInfiniteLineCharge(linearChargeDensity, perpendicularDistanceFromBody):
        return LineCharge.dueToSymmetericLineCharge(linearChargeDensity, pi/2, perpendicularDistanceFromBody)


class Ring:
    def dueToChargedRingOnAxis(chargeOnRing, radiusOfRing, distanceFromCenter):
        # All points are at a same distance from the ring's axis

        potential = k * chargeOnRing / \
            ((distanceFromCenter**2 + radiusOfRing**2)**(1/2))
        return potential

    def dueToUniformlyChargedRingOnAxis(linearChargeDensity, radiusOfRing, distanceFromCenter):
        # Equivalent to Electric field due to Charged Ring on it's Axis
        totalCharge = linearChargeDensity * (2*pi*radiusOfRing)
        return Ring.dueToChargedRingOnAxis(totalCharge, radiusOfRing, distanceFromCenter)


class Disk:
    def dueToChargedDiskOnAxis(chargeDensityFuntion, radiusOfDisk, distanceFromCenter):
        def integrand(x):
            return k * chargeDensityFuntion(x) * 2 * pi * x / (distanceFromCenter**2+x**2)**(1/2)
        potential = integrate.quad(integrand, 0, radiusOfDisk)[0]
        return potential

    def dueToUniformlyChargedDiskOnAxis(chargeDensity, radiusOfDisk, distanceFromCenter):
        def chargeDensityFuntion(chargeDensity):
            return chargeDensity
        return Disk.dueToChargedDiskOnAxis(chargeDensityFuntion, radiusOfDisk, distanceFromCenter)


class Work:
    def workDoneByUs(finalPotential, initialPotential, chargeTransferred):
        return chargeTransferred * (finalPotential-initialPotential)

    def changeInPotentialEnergy(finalPotential, initialPotential, chargeTransferred):
        return chargeTransferred * (finalPotential-initialPotential)

    def workDoneByElectricForce(finalPotential, initialPotential, chargeTransferred):
        return -chargeTransferred * (finalPotential-initialPotential)
