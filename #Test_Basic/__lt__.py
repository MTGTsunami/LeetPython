class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ":" + str(self.age)

    def __lt__(self, other):
        return self.name < other.name if self.name != other.name else self.age < other.age

print("\t".join([str(item) for item in sorted([People("abc", 18), People("abe", 19), People("abe", 12), People("abd", 20)])]))
