class Developer:
    def __init__(self, name):
        self.name = name
        self.skills = [
            "Python",
            "Data Science",
            "Machine Learning",
            "Neural Networks",
            "Problem Solving",
            "Creative Thinking",
        ]
        self.mindset = "Learning by building"
        self.mission = "Master AI concepts and create real-world intelligent solutions."
        self.fun_fact = (
            "Started learning C# in 2015 and quit. "
            "Rediscovered programming with Python in 2023 and unlocked a passion for AI!"
        )

    def current_focus(self):
        return "Deepening knowledge in ML models, neural networks, and data analysis."

    def introduction(self):
        print(f"Hello! I'm {self.name}")
        print("AI-driven developer passionate about data and intelligent systems.")
        print(f"Skills: {', '.join(self.skills)}")
        print(f"Mindset: {self.mindset}")
        print(f"Mission: {self.mission}")
        print(f"Currently: {self.current_focus()}")
        print(f"Fun fact: {self.fun_fact}")


if __name__ == "__main__":
    me = Developer("Plamen Svetoslavov")
    me.introduction()