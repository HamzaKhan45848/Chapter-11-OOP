class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def dog_attrributes(self):
        print(f"The name of the dog is:{self.name} and it's breed is '{self.breed}'.")
dog1 = Dog('buddy','golden retriever')
dog2 = Dog('charlie','husky')
dog1.dog_attrributes()
dog2.dog_attrributes()