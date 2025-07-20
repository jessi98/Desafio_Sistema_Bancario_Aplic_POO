class Passaro:
    def voar(self):
        print("Voamdo...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
