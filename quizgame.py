import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the General Knowledge Quiz!")
        print("Answer multiple-choice and fill-in-the-blank questions to test your knowledge.")

    def ask_question(self, question):
        print("\nQuestion:", question['question'])
        if question['type'] == 'multiple-choice':
            for i, choice in enumerate(question['choices'], start=1):
                print(f"{i}. {choice}")
            user_answer = input("Your answer (enter the option number): ")
        else:
            user_answer = input("Your answer: ")

        return user_answer

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
            print("Correct answer:", correct_answer)

    def run(self):
        self.display_welcome_message()

        while self.questions:
            question = random.choice(self.questions)
            self.questions.remove(question)

            user_answer = self.ask_question(question)
            self.evaluate_answer(user_answer, question['correct_answer'])

        print("\nQuiz completed!")
        print("Your final score:", self.score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            self.score = 0
            self.run()

# Define quiz questions
quiz_questions = [
    {
        'question': "What is the capital of France?",
        'type': 'multiple-choice',
        'choices': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct_answer': 'Paris'
    },
    {
        'question': "The largest planet in our solar system is...",
        'type': 'fill-in-the-blank',
        'correct_answer': 'Jupiter'
    },
    {
        'question':"What is the capital city of Pakistan ?",
        'type': 'multiple-choice',
        'choices':['Lahore','Karachi','Islamabad','Rawalpindi'],
        'correct_answer': 'Islamabad'},
    {
        'question': "What is the capital of France?",
        'type': 'multiple-choice',
        'choices': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct_answer': 'Paris'
    },
    {
      'question':"Which mountain range is located in northern Pakistan and is home to some of the world's highest peaks, including K2?",
      'type':'multiple-choice',
      'choices':['Himalayas','Alps','Andes','Karakoram Range'],
      'correct_answer':'Karakoram Range'

    },
    {'question':"Pakistan gained independence from British rule on which date?",'type':'multiple-choice',
    'choices':['August 14, 1947','September 1, 1947','July 4, 1947',' June 30, 1947'],
    'correct_answer':'August 14, 1947' 
    }
    # Add more questions here
]

# Create and run the quiz game
game = QuizGame(quiz_questions)
game.run()
