with open('input.txt', 'r') as file:
    elf_meals = file.read().split("\n\n")

elf_calories = []
for elf in elf_meals:
    calories = sum(map(int, elf.splitlines()))
    elf_calories.append(calories)
print(max(elf_calories))

elf_calories = sorted(elf_calories)
print(elf_calories[-1]+elf_calories[-2]+elf_calories[-3])
