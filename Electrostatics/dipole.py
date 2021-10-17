from numpy import Infinity
from Electrostatics.electricPotential import dueToPointCharge as EpPoint
import scipy.misc as diff


class GeneralPoint:
    def electricPotential(charge: float, dipoleLength: float, coordinates: list):
        # Direction of dipole moement vector
        # is from negative to positive charge
        # Taking dipole center to be at (0,0,0)
        # & dipole moment parrelel to +ve x-axis
        sumOfSquares = 0
        for x in range(len(coordinates)):
            if x == 0:
                sumOfSquares += (coordinates[x]-dipoleLength/2)**2
            else:
                sumOfSquares += (coordinates[x])**2
        distanceFromPositiveCharge = (sumOfSquares)**(1/2)
        sumOfSquares = 0
        for x in range(len(coordinates)):
            if x == 0:
                sumOfSquares += (coordinates[x]+dipoleLength/2)**2
            else:
                sumOfSquares += (coordinates[x])**2
        distanceFromNegativeCharge = (sumOfSquares)**(1/2)

        potential = EpPoint(charge, distanceFromPositiveCharge) + \
            EpPoint(-charge, distanceFromNegativeCharge)
        if abs(potential) == Infinity:
            print(
                'WARNING : Electric field/potential on the charge of dipole itself will be undefined')
        return potential

    def electricField(charge: float, dipoleLength: float, coordinates: list):
        # here we are using a simple calculus with a
        # complex code, the formula used here are :
        # Ex = -dV/dx ; Ey = -dV/dy; Ez = -dV/dz
        electricFieldArray = []
        for alpha in range(len(coordinates)):
            mu = coordinates

            def f(x):
                mu[alpha] = x
                return GeneralPoint.electricPotential(charge, dipoleLength, mu)
            electricFieldArray.append(diff.derivative(
                f, coordinates[alpha], dx=10**-5))

        return electricFieldArray


class AxialPoint:
    def electricField(charge: float, dipoleLength: float, distanceFromCenter: float):
        return GeneralPoint.electricField(charge, dipoleLength, [
            distanceFromCenter, 0, 0])

    def electricPotential(charge: float, dipoleLength: float, distanceFromCenter: float):
        return GeneralPoint.electricPotential(charge, dipoleLength, [distanceFromCenter, 0, 0])

    class DipoleMoment:
        def electricField(charge: float, dipoleLength: float, distanceFromCenter: float):
            return GeneralPoint.electricField(charge, dipoleLength, [
                distanceFromCenter, 0, 0])


class EquitorialPoint:
    def electricField(charge: float, dipoleLength: float, distanceFromCenter: float):
        return GeneralPoint.electricField(charge, dipoleLength, [
            0, distanceFromCenter, 0])

    def electricPotential(charge: float, dipoleLength: float, distanceFromCenter: float):
        return GeneralPoint.electricPotential(charge, dipoleLength, [0, distanceFromCenter, 0])
