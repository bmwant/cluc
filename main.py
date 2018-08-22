from PyInquirer import prompt, print_json

questions = [
        {
            'type': 'input',
            'name': 'first_name',
            'message': 'Enter your username',
            }
        ]

answers = prompt(questions)
print_json(answers)
