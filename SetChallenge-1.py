number_of_plants = int(input())
plant_heights = {int(x) for x in input().split()}
Average = sum(plant_heights) / len(plant_heights)
print(Average)
