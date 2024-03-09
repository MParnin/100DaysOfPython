# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
    
#     def breathe(self):
#         print("Inhale, exhale")
    
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater")

#     def swim(self):
#         print("moving in water")

# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)
    

piano_keys = ["a", "b", "c", "d", "e", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[::-1])
print(piano_tuple[2:5])