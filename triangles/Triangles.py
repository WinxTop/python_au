import sys


def getLinesFromFile(fileName):
    file = open(fileName)
    lines = file.readlines()
    file.close()

    return lines


def writeToFile(coordinates, fileName):
    file = open(fileName, "w")
    file.write(coordinates)
    file.close()


def getCoordinates(line):
    listCrd = list(map(int, line.strip('\n').split()))

    if len(listCrd) == 6:
        crd1 = Coordinate(listCrd[:2])
        crd2 = Coordinate(listCrd[2:4])
        crd3 = Coordinate(listCrd[4:])
    else:
        crd1 = Coordinate([0, 0])
        crd2 = Coordinate([0, 0])
        crd3 = Coordinate([0, 0])

    return crd1, crd2, crd3


class Coordinate:
    def __init__(self, listCrd):
        self.X = int(listCrd[0])
        self.Y = int(listCrd[1])


class Length:
    def __init__(self, crd1, crd2):
        dX = crd1.X - crd2.X
        dY = crd1.Y - crd2.Y
        self.length = (dX * dX + dY * dY) ** 0.5


class Triangle:
    def __init__(self, coordinates):
        self.side1 = Length(coordinates[0], coordinates[1]).length
        self.side2 = Length(coordinates[0], coordinates[2]).length
        self.side3 = Length(coordinates[1], coordinates[2]).length

    def isTriangle(self):
        c1 = self.side1 + self.side2 > self.side3
        c2 = self.side2 + self.side3 > self.side1
        c3 = self.side3 + self.side1 > self.side2

        return c1 and c2 and c3

    def isIsosceles(self):
        c1 = self.side1 == self.side2
        c2 = self.side2 == self.side3
        c3 = self.side3 == self.side1

        return c1 or c2 or c3

    def isoscelesSquare(self):
        if self.isTriangle() and self.isIsosceles():
            p = (self.side1 + self.side2 + self.side3) / 2

            return (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5

        return 0


def main(data, result):
    lines = getLinesFromFile(data)
    maxArea = 0
    coordinates = ''

    for i in range(len(lines)):
        triangle = Triangle(getCoordinates(lines[i]))
        area = triangle.isoscelesSquare()

        if area > maxArea:
            maxArea = area
            coordinates = lines[i]

    writeToFile(coordinates, result)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
