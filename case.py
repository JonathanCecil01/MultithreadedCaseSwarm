EVAPORATION_FACTOR = 0.02


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
        self.pheromone_level = 10
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
        if self.pheromone_level ==0:
            return 
        self.pheromone_level-=self.pheromone_level*EVAPORATION_FACTOR




class Case:
    def __init__(self):
        self.case_id = ''
        self.solution = []
        self.final_step = Final_Step()
        self.final_step.case_id = self.case_id
        self.final_step.step_id = 0
        self.finalise_count =0

    def finalise_solution_step(self):
        decided_step = self.final_step.finalise_step()
        self.solution.append(decided_step)
        self.final_step.step_id +=1
        self.final_step.suggestions = []

    def add_suggestion(self, Step):
        self.final_step.add_suggestion(Step)
        return

    def display_step_in_choice(self):
        count =0
        reply = "Case ID : "+str(self.case_id)+" Step ID : "+str(self.final_step.step_id)+" Suggestions\n"
        for i in self.final_step.suggestions:
            reply+="Suggestion "+str(count)+" : "+str(i.data)#+"\n"
            reply+="Pheromone Strength : "+str(i.pheromone_level)+" "
            count+=1
        return reply
    
    def evaporate(self):
        for i in self.final_step.suggestions:
            i.evaporation()

    def display_solution(self):
        reply = "\n----CASE "+str(self.case_id)+"--------\n"
        for i in self.solution:
            reply+="Step "+str(i)+" : "+str(i.data)+"\n"
            reply+="Pheromone Strength : "+str(i.pheromone_level)+"\n"
        return reply

    def display_case(self):
        reply = "\n----------------------\n"
        reply+= "-------Case ID : "+str(self.case_id)+"-------\n"
        return reply
