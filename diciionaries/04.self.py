# Podemos utilizar el método especial _init__(conocido como constructor)
# y el objetivo actual self para un creador de objetos del tipo definido con la 
# palabra reservada class


first_dict= {
    "name": "Student",
    "position": "Fulltrack Developer",
    "Skills": ["Python", "Git", "html", "CSS", "Javascript"]
}

class Student:
    def __init__(self,name, skills, position):
        self.name = name
        self.position = position
        self.skills = skills
    def say_name(self):
        print("mi nombre es", self.name,"mi cargo es",self.position,"mis habilidades son"
        ,self. show_kills)()

    def show_kills(self):
        skills =""
        for skill in self.skills:
            skills += skill + " "
        return skills
        
Alice = Student("Alice","full strack developed",["python","git","html","css","javascript"])
bob_el_chef = Student("bob el chef","kitchen helpr",["pastry chef internacional and cake shop"])

Alice.say_name()

bob_el_chef.say_name()