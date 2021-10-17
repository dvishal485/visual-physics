from Electrostatics import electricField as Ef
from Electrostatics import electricPotential as Ep
import matplotlib.pyplot as plt
from numpy import arange as np
from Electrostatics import dipole
from tools import vectorMagnitude


def Electrostatics():
    print('''
=> Electrostatics
''')
    module = input('''Enter the topic code :

    [1] Electric Field due to Point Charge
    [2] Electric Potential due to Point Charge
    [3] Electric Field due to a Finite Line Charge
    [4] Electric Potential difference between
        two points due to a Finite Line Charge (#)
    [5] Electric Field due to Infinite Line Charge
    [6] Electric Potential difference between
        two points due to Infinite Line Charge (#)
    [7] Electric Field due to Uniformly charged Non-conducting sphere
    [8] Electric Potential due to Uniformly charged Non-conducting sphere
    [9] Electric Field due to Conducting sphere
    [10] Electric Potential due to Conducting sphere
    [11] Electric Potential due to Electric Dipole at General Point
    [12] Electric Feild due to Electric Dipole at General Point
    [13] Electric Potential due to Electric Dipole at Equitorial Point
    [14] Electric Feild due to Electric Dipole at Equitorial Point
    [15] Electric Potential due to Electric Dipole at Axial Point
    [16] Electric Feild due to Electric Dipole at Axial Point

    # - Not implemeted yet
''')

    if module == "1":
        print('[1] Electric Field due to Point Charge')
        charge = float(input('Charge q present on the body (in Coloumb) : '))
        distance = float(input(
            'Distance of point at which electric field is required from the charge (in Meter) : '))
        print('Result : ')
        print('Electric Field : ' +
              str('{:.2e}'.format(Ef.dueToPointCharge(charge, distance)))+' Newton/Columb')

        def graph(x):
            return Ef.dueToPointCharge(charge, x)
        x = np(0, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from point charge (Meter)')
        plt.ylabel('Electric field strength at the point (Newton/Coloumb)')
        plt.title('Electric Field due to point charge')
        plt.show()

    if module == "2":
        print('[2] Electric Potential due to Point Charge')
        charge = float(input('Charge q present on the body (in Coloumb) : '))
        distance = float(input(
            'Distance of point at which electric potential is required from the charge (in Meter) : '))
        print('Result : ')
        print('Electric Potential : ' +
              str('{:.2e}'.format(Ep.dueToPointCharge(charge, distance)))+' Joule/Columb')

        def graph(x):
            return Ep.dueToPointCharge(charge, x)
        x = np(0, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from point charge (Meter)')
        plt.ylabel('Electric Potential at the point (Joule/Coloumb)')
        plt.title('Electric Potential due to point charge')
        plt.show()

    if module == "3":
        print('[3] Electric Field due to a Finite Line Charge')
        chargeDensity = float(
            input('Linear Charge Density present on the body (in Coloumb/Meter) : '))
        distance = float(input(
            'Perpendicular Distance of point at which electric field is required from the charged body (in Meter) : '))
        angle1 = float(input(
            'Angle subtented by body on point lying above perpendicular (in Radians) : '))
        angle2 = float(input(
            'Angle subtented by body on point lying below perpendicular (in Radians) : '))
        print('Result : ')
        print('Electric Field : ' +
              str('{:.2e}'.format(Ef.LineCharge.dueToUniformLineCharge(chargeDensity, angle1, angle2, distance))))

        def graph(x):
            return Ef.LineCharge.dueToUniformLineCharge(chargeDensity, angle1, angle2, x)
        x = np(0 + distance/10000, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Perpendicular distance from line charge (Meter)')
        plt.ylabel('Electric field strength at the point (Newton/Coloumb)')
        plt.title('Electric field due to line charge')
        plt.show()

    if module == "5":
        print('[5] Electric Field due to Infinite Line Charge')
        chargeDensity = float(
            input('Linear Charge Density present on the body (in Coloumb/Meter) : '))
        distance = float(input(
            'Perpendicular Distance of point at which electric field is required from the charged body (in Meter) : '))
        print('Result : ')
        print('Electric Field : ' +
              str('{:.2e}'.format(Ef.LineCharge.dueToUniformInfiniteLineCharge(chargeDensity, distance))))

        def graph(x):
            return Ef.LineCharge.dueToUniformInfiniteLineCharge(chargeDensity, x)
        x = np(0 + distance/10000, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Perpendicular distance from line charge (Meter)')
        plt.ylabel('Electric field strength at the point (Newton/Coloumb)')
        plt.title('Electric field due to line charge')
        plt.show()

    if module == "7":
        print('[7] Electric Field due to Uniformly charged Non-conducting sphere')
        chargeDensity = float(input(
            'Input volume charge density of sphere (in Columb/Meter^3) : '))
        radius = float(input('Radius of charged sphere (in Meter) : '))
        distance = float(input(
            'Distance of point from sphere\'s center (in Meter): '))
        print('Result : ')
        print('Electric Field : ' +
              str('{:.2e}'.format(Ef.Sphere.dueToUniformNonConductingSphere(chargeDensity, radius, distance))))

        def graph(x):
            return Ef.Sphere.dueToUniformNonConductingSphere(chargeDensity, radius, x)
        x = np(0, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from sphere\'s center charge (Meter)')
        plt.ylabel('Electric field strength at the point (Newton/Coloumb)')
        plt.title('Electric Field due to Uniformly charged Non-conducting sphere')
        plt.show()

    if module == "8":
        print('[8] Electric Potential due to Uniformly charged Non-conducting sphere')
        chargeDensity = float(input(
            'Input volume charge density of sphere (in Columb/Meter^3) : '))
        radius = float(input('Radius of charged sphere (in Meter) : '))
        distance = float(input(
            'Distance of point from sphere\'s center (in Meter): '))
        print('Result : ')
        print('Electric Potential : ' +
              str('{:.2e}'.format(Ep.Sphere.dueToUniformNonConductingSphere(chargeDensity, radius, distance))))

        def graph(x):
            return Ep.Sphere.dueToUniformNonConductingSphere(chargeDensity, radius, x)
        x = np(0, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from sphere\'s center charge (Meter)')
        plt.ylabel('Electric potential at the point (Newton/Coloumb)')
        plt.title(
            'Electric potential due to Uniformly charged Non-conducting sphere')
        plt.show()

    if module == "9":
        print('[9] Electric Field due to Conducting sphere')
        chargeDensity = float(input(
            'Input surface charge density of sphere (in Columb/Meter^2) : '))
        radius = float(input('Radius of charged sphere (in Meter) : '))
        distance = float(input(
            'Distance of point from sphere\'s center (in Meter): '))
        print('Result : ')
        print('Electric Field : ' +
              str('{:.2e}'.format(Ef.Sphere.dueToConductingSphere(chargeDensity, radius, distance))))

        def graph(x):
            return Ef.Sphere.dueToConductingSphere(chargeDensity, radius, x)
        x = np(0, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from sphere\'s center charge (Meter) : ')
        plt.ylabel('Electric field strength at the point (Newton/Coloumb) : ')
        plt.title('Electric Field due to Conducting sphere : ')
        plt.show()

    if module == "10":
        print('[10] Electric Potential due to Conducting sphere')
        chargeDensity = float(input(
            'Input volume charge density of sphere (in Columb/Meter^2) : '))
        radius = float(input('Radius of charged sphere (in Meter) : '))
        distance = float(input(
            'Distance of point from sphere\'s center (in Meter): '))
        print('Result : ')
        print('Electric Potential : ' +
              str('{:.2e}'.format(Ep.Sphere.dueToConductingSphere(chargeDensity, radius, distance))))

        def graph(x):
            return Ep.Sphere.dueToConductingSphere(chargeDensity, radius, x)
        x = np(0, 1.5*distance, distance/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from sphere\'s center charge (Meter)')
        plt.ylabel('Electric potential at the point (Newton/Coloumb)')
        plt.title(
            'Electric potential due to Uniformly charged Non-conducting sphere')
        plt.show()

    if module == "11":
        print('[11] Electric Potential due to Electric Dipole at General Point')
        charge = float(input('Magnitude of charge on dipole (Coloumb) : '))
        dipoleLength = float(input('Dipole length (Meter) : '))
        print('Enter the coordinates assuming the dipole is located with it\'s dipole moment parallel to x-axis and it\'s center at origin')
        xCord = float(input('x-coordinate (Meter) : '))
        yCord = float(input('y-coordinate (Meter) : '))
        zCord = float(input('z-coordinate (Meter) : '))
        resultPotential = dipole.GeneralPoint.electricPotential(
            charge, dipoleLength, [xCord, yCord, zCord])
        print('Result : ')
        print('Electric Potential : ' +
              str('{:.2e}'.format(resultPotential)))

    if module == "12":
        print('[12] Electric Field due to Electric Dipole at General Point')
        charge = float(input('Magnitude of charge on dipole (Coloumb) : '))
        dipoleLength = float(input('Dipole length (Meter) : '))
        print('Enter the coordinates assuming the dipole is located with it\'s dipole moment parallel to x-axis and it\'s center at origin')
        xCord = float(input('x-coordinate (Meter) : '))
        yCord = float(input('y-coordinate (Meter) : '))
        zCord = float(input('z-coordinate (Meter) : '))
        resultFeild = dipole.GeneralPoint.electricPotential(
            charge, dipoleLength, [xCord, yCord, zCord])
        print('Result : ')
        print('Electric Feild : ' +
              str('{:.2e}'.format(resultFeild)))

    if module == "13":
        print('[13] Electric Potential due to Electric Dipole at Equitorial Point')
        charge = float(input('Magnitude of charge on dipole (Coloumb) : '))
        dipoleLength = float(input('Dipole length (Meter) : '))
        print('Enter the distance assuming the dipole is located with it\'s dipole moment parallel to x-axis and it\'s center at origin')
        distanceFromCenter = float(
            input('Distance from center of Dipole (Meter) : '))
        resultPotential = dipole.EquitorialPoint.electricPotential(
            charge, dipoleLength, distanceFromCenter)
        print('Result : ')
        print('Electric Potential : ' +
              str('{:.2e}'.format(resultPotential)))

        def graph(x):
            return dipole.EquitorialPoint.electricPotential(charge, dipoleLength, x)
        x = np(0, 1.5*distanceFromCenter, distanceFromCenter/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from dipole\'s center (Meter)')
        plt.ylabel('Electric potential at the point (Newton/Coloumb)')
        plt.title(
            'Electric potential due Dipole at Equitorial point')
        plt.show()

    if module == "14":
        print('[14] Electric Feild due to Electric Dipole at Equitorial Point')
        charge = float(input('Magnitude of charge on dipole (Coloumb) : '))
        dipoleLength = float(input('Dipole length (Meter) : '))
        print('Enter the distance assuming the dipole is located with it\'s dipole moment parallel to x-axis and it\'s center at origin')
        distanceFromCenter = float(
            input('Distance from center of Dipole (Meter) : '))
        resultFeild = dipole.EquitorialPoint.electricField(
            charge, dipoleLength, distanceFromCenter)
        print('Result : ')
        print('Electric Feild : ' + str(resultFeild))

        def graph(x):
            return vectorMagnitude(dipole.EquitorialPoint.electricField(charge, dipoleLength, x))
        x = np(0, 1.5*distanceFromCenter, distanceFromCenter/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from dipole\'s center (Meter)')
        plt.ylabel('Electric field at the point (Newton/Coloumb)')
        plt.title(
            'Electric field due Dipole at Equitorial point')
        plt.show()

    if module == "15":
        print('[15] Electric Potential due to Electric Dipole at Axial Point')
        charge = float(input('Magnitude of charge on dipole (Coloumb) : '))
        dipoleLength = float(input('Dipole length (Meter) : '))
        print('Enter the distance assuming the dipole is located with it\'s dipole moment parallel to x-axis and it\'s center at origin')
        distanceFromCenter = float(
            input('Distance from center of Dipole (Meter) : '))
        resultPotential = dipole.AxialPoint.electricPotential(
            charge, dipoleLength, distanceFromCenter)
        print('Result : ')
        print('Electric Potential : ' +
              str('{:.2e}'.format(resultPotential)))

        def graph(x):
            return dipole.AxialPoint.electricPotential(charge, dipoleLength, x)
        x = np(0, 1.5*distanceFromCenter, distanceFromCenter/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from dipole\'s center (Meter)')
        plt.ylabel('Electric potential at the point (Newton/Coloumb)')
        plt.title(
            'Electric potential due Dipole at Axial point')
        plt.show()

    if module == "16":
        print('[16] Electric Feild due to Electric Dipole at Axial Point')
        charge = float(input('Magnitude of charge on dipole (Coloumb) : '))
        dipoleLength = float(input('Dipole length (Meter) : '))
        print('Enter the distance assuming the dipole is located with it\'s dipole moment parallel to x-axis and it\'s center at origin')
        distanceFromCenter = float(
            input('Distance from center of Dipole (Meter) : '))
        resultFeild = dipole.AxialPoint.electricField(
            charge, dipoleLength, distanceFromCenter)
        print('Result : ')
        print('Electric Feild : ' + str(resultFeild))

        def graph(x):
            return vectorMagnitude(dipole.AxialPoint.electricField(charge, dipoleLength, x))
        x = np(0, 1.5*distanceFromCenter, distanceFromCenter/100)
        y = []
        for point in x:
            y.append(graph(point))
        plt.plot(x, y)
        plt.xlabel('Distance from dipole\'s center (Meter)')
        plt.ylabel('Electric field at the point (Newton/Coloumb)')
        plt.title(
            'Electric field due Dipole at Axial point')
        plt.show()
