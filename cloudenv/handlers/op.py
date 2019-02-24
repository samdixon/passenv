class OnePassword:
    def __init__(self, CreateObject):
        self.CreateObject = CreateObject
        self.name = CreateObject.name

        self.PrintMe()

    def PrintMe(self):
        print(self.name)


class OnePasswordCreate(OnePassword):
    def __init__(self, CreateObject):
        super().__init__(CreateObject)
