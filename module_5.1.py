class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

my_house = House('ЖК Эльбрус', 30)

my_house.go_to(30)  # Ожидаемый вывод: 1 2 3 4 5
my_house.go_to(35)  # Ожидаемый вывод: Такого этажа не существует

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
