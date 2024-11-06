class User:
    def __unit__(self, name, work, age):
        self.name = name
        self.work = work
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

    def change_work(self, new_work):
        self.work = new_work

    def change_age(self, new_age):
        self.age = new_age
