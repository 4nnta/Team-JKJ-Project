from Employee import Employee
from Task import Task
from PriorityQueue import PriorityQueue

class JobAssignment(object):
	# return # of matching entries between 2 lists
	def compareList(self, list1: [], list2: []):
		appeared = {}
		for entry in list1:
			appeared[entry] = 1

		numMatched = 0

		for entry in list2:
			if entry in appeared:
				numMatched = numMatched + 1

		return numMatched

	def evaluation(self, matchDept: int, matchSkill: int, capacity: int)->float:
		return 1 * matchDept + 1 * matchSkill + 1 * capacity
		# weight1 * matchDept + weight2 * matchSkill + weight3 * capacity

	# assignment list for a single task
	def singleTaskAssignment(self, task: Task, employeeList: [], maxCapacity = 1000):
		availableEmployee = employeeList
		PQ = PriorityQueue([])

		it = 0

		for employee in availableEmployee:
			matchDept = self.compareList(employee.department, task.department)
			matchSkill = self.compareList(employee.skillSet, task.skillSet)

			if employee.capacity >= maxCapacity or matchDept == 0 or matchSkill == 0:
				continue

			evaluation = self.evaluation(matchDept, matchSkill, maxCapacity - employee.capacity)

			PQ.add((-evaluation, it, employee))
			it = it + 1

		assignedEmployee = []

		for i in range(min(len(availableEmployee), task.assignedNeeded)):
			employee = PQ.pop()
			assignedEmployee.append(employee)

		return assignedEmployee

	def getAssignment(self, taskList: [], employeeList: []):
		queue = PriorityQueue([])

		for task in taskList:
			queue.add((-task.priority, task))

		assignmentList = []

		while (queue.size() > 0):
			task = queue.pop()
			assignment = self.singleTaskAssignment(task[1], employeeList)

			for employee in assignment:
				assignmentList.append((task, employee))

		return assignmentList

		