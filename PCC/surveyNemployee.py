class AnonSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_ques(self):
        print(f"Survey Question: {self.question}")

    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        print(f"Survey question: {self.question}")
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")


# 11-3
class Employee:
    def __init__(self, first_name, last_name, an_salary=0):
        self.f_n = first_name
        self.l_n = last_name
        self.a_s = an_salary

    def give_raise(self, amount=5000):
        self.a_s += amount
