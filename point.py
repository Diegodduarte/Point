class Point():

    def __init__(self, Pontox=0,Pontoy=0):
        self.x = Pontox
        self.y = Pontoy


    def SolicitarPontos(self):
        self.x = float(input('Informe o Ponto x: '))
        self.y = float(input('Informe o Ponto y: '))

    def __str__(self):
        result = '\nPonto x: '  + str(self.x)
        result += '\nPonto y: '  + str(self.y)
        return result

    def __eq__(self, other):
        P1x = self.x
        P1y = self.y
        P2x = other.x
        P2y = other.y


        return (P1x == P2x and P1y == P2y)



    def __add__(self,other):
        P1x = self.x
        P1y = self.y
        P2x = other.x
        P2y = other.y

        NovoPonto = Point()

        NovoPonto.x = P1x + P2x
        NovoPonto.y = P1y + P2y


        return (NovoPonto)




