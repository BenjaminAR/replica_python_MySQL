class Miclase:
    def metodouno(self):
        print('desde uno')
    def metododos(self):
        print('desde dos')
        self.metodouno()

demiclase = Miclase()

demiclase.metododos()