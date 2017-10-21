from point import *

def main(args=[]):

    P1 = Point()
    P2 = Point()

    print("Ponto 1:")
    P1.SolicitarPontos()

    print("Ponto 2:")
    P2.SolicitarPontos()

    PN = Point()

    PN = P1 + P2

    print PN

if __name__ == "__main__":
        main()
