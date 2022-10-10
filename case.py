
class Final_Step:
    def __init__(self):
        self.case_id = ''
        self.step_id= ''
        self.suggestions = []

    def add_suggestion(self, Step):
        self.suggestions.append(Step)

    def finalise_step(self):
        val =0
        final_step = Step()
        for i in self.suggestions:
            if i.pheromone_level>val:
                val = i.pheromone_level
                final_step = i
        return final_step



class Step:
    def __init__(self):
        self.case_id = ''
        self.step_id = ''
        self.suggestion_id = ''
        self.pheromone_level = 0
        self.data = ''

    def set_step(self, case_id, step_id):
        self.step_id = step_id
        self.case_id = case_id

    def increase_pheromone_level(self):
        self.pheromone_level+=10

    def display(self):
        print("Step id : ", self.step_id)
        print("Suggestion id : ", self.suggestion_id)
        print("Pheromone strength : ", self.pheromone_level)

    def evaporation(self):
        self.pheromone_level-=2




class Case:
    def __init__(self):
        self.case_id = ''
        self.solution = []
        self.final_step = Final_Step()

    def finalise_solution_step(self):
        decided_step = self.final_step.finalise_step()
        self.solution.append(Final_Step)
        self.final_step = Final_Step()

    def display_solution(self):
        for i in range(len(self.solution)):
            print("Step ", i, " : ", self.solution[i])
