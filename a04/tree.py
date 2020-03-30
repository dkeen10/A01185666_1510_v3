class Tree:
    def __init__(self, species, age, circumference):
        if len(species.strip()):
            self.__species = species
        else:
            raise ValueError("species can't be blank!")

        if age >= 0:
            self.__age = age
        else:
            raise ValueError("age must be a positive integer!")

        if circumference >= 0:
            self.__circumference = circumference
        else:
            raise ValueError("circumference must be a positive integer!")

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_circumference(self):
        return self.__circumference

    def __str__(self):
        return f"Species: {self.__species} \nAge: {self.__age} \nCircumference: {self.__circumference}"

    def __repr__(self):
        return f"Species: {self.__species} \nAge: {self.__age} \nCircumference: {self.__circumference}"


def main():
    print(Tree("redwood", 50, 200))


if __name__ == "__main__":
    main()
