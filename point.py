class Point():

    def __init__(self,x,y,x2,y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2


    def __add__(self, other):
        P1x = self.x
        P1y = self.y
        P2x = self.x2
        P2y = self.Y2

        SomaPontoX = P1x + P2x
        SomaPontoY = P1y + P2y

    def SolicitarPontos(self):
        self.x = float(input('Informe o primeiro Ponto x'))
        self.y = float(input('Informe o primeiro Ponto y'))
        self.x2 = float(input('Informe o segundo Ponto x'))
        self.y2 = float(input('Informe o segundo Ponto y'))




