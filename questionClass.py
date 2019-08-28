class SurveyClass:
    def __init__(self, sectionList):
        self.sectionList = sectionList

    def startSurvey(self):
        for i in self.sectionList:
            i.startSection()

class Section:
    def __init__(self, qualifyingQuestion, questionList, description):
        self.qualifyingQuestion = qualifyingQuestion
        self.questionList = questionList
        self.description = description

    def startSection(self):
        print(self.qualifyingQuestion.questionText)
        print('Your Answer: ')
        response= input()
        if response == 'yes':
            print(self.description)
            for i in self.questionList:
                i.ask()


class Question:
    def __init__(self, questionNumber, responses, questionText, answerOptions):
        self.questionNumber = questionNumber 
        self.responses = responses
        self.questionText = questionText
        self.answerOptions = answerOptions

    def ask(self):
        print(self.questionText, self.answerOptions)
        print('Your Answer: ')
        responseSingular= input()
        self.responses.append(responseSingular) 
        print(self.responses)
        # self.nextQuestion


####
#This is my running code
####


qualQuestion1 = Question(1, [], 'qualifying question 1', ['yes', 'no'])
qualQuestion2 = Question(2, [], 'qualifying question 2', ['yes', 'no'])
qualQuestion3 = Question(3, [], 'qualifying question 3', ['yes', 'no'])

question1 = Question(1, [], 'section 1 question 1', ['1', '2'])

question2 = Question(2, [], 'section 1 quesion 2', ['1','2'])

question3 = Question(3, [], 'section 2 question 1', ['1', '2'])

question4 = Question(4, [], 'section 2 quesion 2', ['1','2'])

question5 = Question(5, [], 'section 3 question 1', ['1', '2'])

question6 = Question(6, [], 'section 3 quesion 2', ['1','2'])


section1 = Section(qualQuestion1,[question1, question2],'This is the description for section 1')

section2 = Section(qualQuestion2,[question3, question4],'This is the description for section 2')

section3 = Section(qualQuestion3,[question5, question6],'This is the description for section 3')

sheCodesSurvey = SurveyClass([section1 ,section2 ,section3])
sheCodesSurvey.startSurvey()

# print(answers)