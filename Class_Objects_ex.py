class krishnan():
    def skills(self) -> None:
        print ("Krishnan is a good boy")

class ge():
    def skills(self) -> None:
        print("Yes I am working with GE")

class profile(krishnan,ge):
    def skills(self) -> None:
        krishnan.skills(self)
        ge.skills(self)
        print("CV")

c = profile()

c.skills()




