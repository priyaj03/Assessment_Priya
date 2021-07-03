'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock'''


def rock_paper_scissors():
    player1 = input('PLAYER 1 : rock / paper / scissor:')
    player2 = input('PLAYER 2 : rock / paper / scissor:')
    if player1 == 'rock' and player2 == 'scissor' or player1 == 'scissor' and player2 == 'paper' or \
            player1 == 'paper' and player2 == 'rock':
        print('Congratulations Player 1')
    elif player2 == 'rock' and player1 == 'scissor' or player2 == 'scissor' and player1 == 'paper' or \
            player2 == 'paper' and player1 == 'rock':
        print('Congratulations Player 2')
    elif player1 == player2:
        print('Draw the match')


def start_again():
    n = input('Wanna play again? [y/n] :')
    if n == 'y':
        rock_paper_scissors()
        start_again()
    else:
        pass


rock_paper_scissors()
start_again()
