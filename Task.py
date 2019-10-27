class Task:
    'Common base class for all task'
    def __init__(self, name, department, skillSet, difficulty, length, description, priority, assignedNeeded):
        self.name = name
        self.department = department
        self.skillSet = skillSet
        self.difficulty = difficulty
        self.length = length
        self.description = description
        self.priority = priority
        self.assignedNeeded = assignedNeeded

    def __str__ (self):
        print ("Task: \n   Name:            ", self.name,
                     "\n   Description:     ", self.description,
                     "\n   Department:      ", self.department,
                     "\n   Skill Set:       ", self.skillSet,
                     "\n   Difficulty:      ", self.difficulty,
                     "\n   Length:          ", self.length,
                     "\n   Priority:        ", self.priority,
                     "\n   Assigned:        ", self.assigned,
               )