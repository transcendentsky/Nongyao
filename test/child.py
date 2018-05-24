from Parent import Parent


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        self.mp = 0

    def func(self):
        print(self.hp)


child = Child()
child.func()
print(child.hp)