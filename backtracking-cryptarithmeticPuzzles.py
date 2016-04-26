
'''
Solving cryptarithmetic puzzles
Newspapers and magazines often have cryptarithmetic puzzles of the form:
  SEND
+ MORE
 MONEY

The goal here is to assign each letter a digit from 0 to 9 so that the arithmetic works out
correctly. The rules are that all occurrences of a letter must be assigned the same digit, and no
digit can be assigned to more than one letter. First, I will show you a workable, but not very
efficient strategy and then improve on it.

In pseudocode, our first strategy will be:
First, create a list of all the characters that need assigning to pass to Solve
If all characters are assigned, return true if puzzle is solved, false otherwise
Otherwise, consider the first unassigned character
for (every possible choice among the digits not in use)
make that choice and then recursively try to assign the rest of the characters
if recursion sucessful, return true
if !successful, unmake assignment and try another digit
if all digits have been tried and nothing worked, return false to trigger backtracking

The algorithm above actually has a lot in common with the permutations algorithm, it pretty
much just creates all arrangements of the mapping from characters to digits and tries each until
one works or all have been unsuccessfully tried. For a large puzzle, this could take a while.

A smarter algorithm could take into account the structure of the puzzle and avoid going down
dead-end paths. For example, if we assign the characters starting from the ones place and moving
to the left, at each stage, we can verify the correctness of what we have so far before we continue
onwards. This definitely complicates the code but leads to a tremendous improvement in
efficiency, making it much more feasible to solve large puzzles.

'''

import re


class puzzle(object):
    @staticmethod
    def _parseFormula(formula):
        formula = formula.replace(' ', '')
        ops = re.split(r'([\+\-\*\/\=])', formula)
        if len(ops) != 5:
            raise ValueError('formula incorrect')
        else:
            return ops

    def transOp(self, operand):
        '''convert a oprand into a number of string based on assignment'''
        value = int(''.join(str(self.solution[c]) for c in operand))
        return str(value)

    def initalSolution(self):
        sol = {}
        for c in self.ops[0]+self.ops[2]+self.ops[4]:
            if c not in sol:
                sol[c] = -1
        return sol

    def __init__(self, formula='CS+YOU=FUN'):
        #self.solution = {'C':4, 'S':1, 'Y':5, 'O':8, 'U':2, 'F':6,'N':3}
        self.ops = puzzle._parseFormula(formula)
        self.solution = self.initalSolution()

    def printSolution(self):
        print (self.ops[0], self.transOp(self.ops[0])), (self.ops[2], self.transOp(self.ops[2])), (self.ops[4], self.transOp(self.ops[4]))

    def isSolved(self):
        value1 = self.transOp(self.ops[0])
        value2 = self.transOp(self.ops[2])
        value3 = self.transOp(self.ops[4])
        return eval(value1 + self.ops[1] + value2 + "==" + value3)


    def isValid(self, num):
        if num in self.solution.values():
            return False
        else:
            return True

    def nextAssignment(self):
        for key in self.solution:
            if self.solution[key] == -1:
                return key
        return -1

    def solvePuzzle(self):
        assign = self.nextAssignment()
        if assign == -1:
            if self.isSolved():
                self.printSolution()
                return True
            # else:
            #     return False
        else:
            for num in [1,2,3,4,5,6,7,8,9,0]:
                if self.isValid(num):
                    self.solution[assign] = num
                    if self.solvePuzzle():
                        return True
                    self.solution[assign] = -1
            return False


if __name__ == '__main__':
    p = puzzle('eel + ebb = blab') #550+511=1061
    p = puzzle('go+to=out')
    p = puzzle('japan+major=ichiro')
    p.solvePuzzle()
    p = puzzle('A+B=AC') # A=1, B=9, C=0
    p.solvePuzzle()
    p = puzzle('aa+bb=cbc') # a=9, b = 2, c =1
    p.solvePuzzle()
    p = puzzle('send+more=money')
    p.solvePuzzle()


