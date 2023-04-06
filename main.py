from turtle import Turtle, Screen
import pandas
import time

# Screen Setup
screen = Screen()
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")
screen.addshape("checkmarkA.gif")
screen.title("Can YOU name the States of America!!")

states_list = pandas.read_csv("50_states.csv")
print(states_list.state)

# Lists of State Values
state_names = states_list.state.to_list()
states2 = []
x_values = states_list.x.to_list()
y_values = states_list.y.to_list()
# to accept lower case guesses
state_names_2 = state_names
state_names_2 = list(map(str.lower, state_names_2))

# Game Functionality
score = 0
strikes = 3
states_learned = []
game = True
while game:
    guessed_index = -1
    guess = screen.textinput(f"States guessed: {score}/50 -- Strikes left: {strikes}", "Name a state? (spell it fully) ")
    for i in range(0, len(state_names)):
        if guess == state_names[i] or guess == state_names_2[i]:
            # Checkmark turtle placement / record correct guesses / increase score
            guessed_index = i
            check = Turtle()
            check.pu()
            check.shape("checkmarkA.gif")
            check.setpos(x_values[i], y_values[i])
            states_learned.append(i)
            score += 1
            break
        else:
            pass
    # if guess is wrong, the value will remain at -1
    if guessed_index == -1:
        strikes -= 1
        # End of Game
        if strikes == 0:
            if 50 >= score >= 45:
                conclusion = "YOU ARE A SAVANT OF AMERICAN Culture"
            elif 44 >= score >= 38:
                conclusion = "Obama would be Proud!"
            elif 37 >= score >= 31:
                conclusion = "Trump would be proud!"
            elif 30 >= score >= 23:
                conclusion = "Your Knowledge is Mid; DO BETTER"
            elif 22 >= score >= 14:
                conclusion = "Maybe try picking up a book sometime soon?"
            else:
                conclusion = "You are a certified COMMUNIST!"
            game = False
            game_over = Turtle()
            game_over.hideturtle()
            game_over.color("red")
            game_over.write(f"GAME OVER\n  \n You got {score}/50 right,\n  \n {conclusion}",
                            align='center', font=("Arial", 20, 'normal'))
            time.sleep(3)
# States to Learn CSV Creation
states_to_learn = state_names
for item in states_learned:
    states_to_learn.remove(state_names[item])

states_to_study_dict = {
    "States": states_to_learn
}
states_to_study = pandas.DataFrame(states_to_study_dict)
states_to_study.to_csv("states_to_study.csv")

screen.exitonclick()
