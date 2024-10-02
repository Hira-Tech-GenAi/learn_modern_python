

motorcycles: list[str] = ['honda', 'yamaha', 'suzuki']

first_owned: str = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {first_owned.capitalize()}")