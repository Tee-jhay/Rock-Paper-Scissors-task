import random

moves = ['R', 'P', 'S']
randomNumber = random.randint(0, 2)
cpuMove = moves[randomNumber]

while True:
    player = input('What is your choice? R for Rock, P for Paper, S for Scissors, Q to Quit game: \n').upper()
    if player == 'Q':
        break
    elif player not in moves:
        print('Invalid option, Try again\n')
        continue

    if player == cpuMove:
        if player == cpuMove == 'R':
            print('Player (Rock) : CPU (Rock)\n')
            print('Tie')

        elif player == cpuMove == 'P':
            print('Player (Paper) : CPU (Paper)\n')
            print('Tie')

        elif player == cpuMove == 's':
            print('player (Scissors) : CPU (Scissors)\n')
            print('Tie')

    elif player == 'R':
        if cpuMove == 'P':
            print('Player (Rock) : CPU (Paper)\n')
            print('YOU LOSE!!')

        elif player == 'S':
            print('Player (Rock) : CPU (Scissors)\n')
            print('YOU WIN!!!!')

    elif player == 'P':
        if cpuMove == 'S':
            print('Player (Paper) : CPU (Scissors)\n')
            print('YOU LOSE!!')
        elif cpuMove == 'R':
            print('Player (Paper) : CPU (Rock)\n')
            print('YOU WIN!!!!')
    elif player == 'S':
        if cpuMove == 'R':
            print('Player (Scissors) : CPU (Rock)\n')
            print('YOU LOSE!!')
        elif cpuMove == 'P':
            print('Player (Scissors) : CPU (Paper)\n')
            print('YOU WIN!!!!')
