from MuseumSculpture import MuseumSculpture


def main():
    zeus_sculpture = MuseumSculpture(1234, "Zeus_Sculpture", "Wax", 150, 100000)
    ahilles_sculpture = MuseumSculpture(1310, "Ahilles_Sculpture", "Wax", 110, 120000)
    lenin_sculpture = MuseumSculpture(1946, "Lenin_Sculpture", "Clay", 200)

    print(zeus_sculpture)
    print(ahilles_sculpture)
    print(lenin_sculpture)
    print(MuseumSculpture.amount_of_sculptures)


if __name__ == '__main__':
    main()
