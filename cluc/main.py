from PyInquirer import prompt, print_json


questions = [
    {
        'type': 'input',
        'name': 'username',
        'message': 'Enter your username',
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'Enter your password',
    },
]

answers = prompt(questions)
import pdb; pdb.set_trace()
print_json(answers)
