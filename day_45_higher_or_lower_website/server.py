from flask import Flask
import random

app = Flask(__name__)

# Constants
low_url_gif = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc29hbW1odWl6ZGJvbGIxZjVsang3NW5mYzEwOTZmdjZ6N3J3ODZ0dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xNiL0f6NCplbuE/giphy.gif'
too_high_gif = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGUzY3Bud3p1amg5N2xhdnc5bGVqcXhud2M0NnIwMThzdHNoY2NjeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gS0rng73xPCU/giphy.gif'
correct_answer_gif = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2x4dDhoemZrb3Q5MXZic3pkM3N6NnFqZWNmaXM2bDRjaHVheXE4OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qo8ItWaISHkCwrwU93/giphy.gif'
home_page_gif = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3YyZGFqbG9udWRuamluM2k2ajBxZzVpdWM3Y3dpaDdtaXNzcmEyMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26gskf95cHOTlQOL6/giphy-downsized-large.gif'

# Generate random number.
random_number = random.randint(1, 9)


# Home page
@app.route("/")
def index():
    return ("<h1>Guess a number between 1-9? (enter after the \ in the url)</h1>"
            f"<img src={home_page_gif} />")


# Guessing the numbers and sorting them into their own page.
@app.route("/<int:guess>")
def too_high(guess):
    global random_number
    if guess > random_number:
        return (f"<h1 style='color:red;'>Too High!</h1>"
                f"{random_number}"
                f"<img src={too_high_gif} />")
    elif guess < random_number:
        return (f"<h1 style='color:blue;'>Too Low!</h1>"
                f"{random_number}"
                f"<img src={low_url_gif} />")
    elif guess == random_number:
        return (f"<h1 style='color:blue;'>You got it!</h1>"
                f"{random_number}"
                f"<img src={correct_answer_gif} />")


if __name__ == "__main__":
    app.run(debug=True)
