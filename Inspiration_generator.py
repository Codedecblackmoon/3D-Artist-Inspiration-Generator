# import random

# def whatufeeling():
#     print("-------------------------------")
#     print('What do you feel like craeting?...')
#     output = input("Pick a difficalty....\nEasy, Middium or Hard.\n....").lower()
#     while True:
#         if output == '' and output != 'simple' and output != 'middium' and output != 'hard':
#             output = input("......Pick a difficalty level......\n......Easy, Middium or Hard.\n.... ").lower()
#         else:
#             return output

# def simple():
#     with open('data/simple.txt', 'r')as fill:
#         word = fill.readline()
#     return word

# def hard():
#     with open('data/hard.txt', 'r')as fill:
#         word = fill.readline()
#     return word

# def middium():
#     with open('data/middum.txt', 'r')as fill:
#         word = fill.readline()
#     return word

# def Theme():
#     with open('data/theme.txt', 'r')as fill:
#         word = fill.readline()
#     return word

# def colors():
#     with open('data/color.txt', 'r')as fill:
#         word = fill.readline()
#     return word

# def chosing(theme, output, color):
    
#     if output == "hard":
#         iterm = random.choice(hard().split('='))
#         colorse = random.sample(color, k=5)
#         return f"Create a {iterm} in a {theme} setting using the following colors {colorse[0]}, {colorse[1]}, {colorse[2]}, {colorse[3]}, {colorse[4]}."
#     elif output == "easy":
#         iterm = random.choice(simple().split('='))
#         colorse = random.sample(color, k=2)
#         return f"Create a {iterm} using the following colors {colorse[0]}, {colorse[1]}.\n"
#     elif output == "middium":
#         iterm = random.choice(middium().split('='))
#         colorse = random.sample(color, k=3)
#         return f"Create a {iterm} in a {theme} setting using the following colors {colorse[0]}, {colorse[1]}, {colorse[2]}."
    
# def deffination(theme):
#     print(f"\nTHEME DEFFINATION..... {theme.upper()} ....")
#     print("-------------------------------")
#     with open('data/theme_def.txt', 'r')as fill:
#         word = fill.readlines()
#     for line in word:
#         deff = line.split(':')
#         if deff[0] == theme:
#             print(deff[1])
     
# def main():
#     theme = random.choice(Theme().split('+'))
#     output = whatufeeling()
#     color = list(colors().split('='))
    
#     print("\n3D Artist Inspiration Generator")
#     print("-------------------------------")
#     print(chosing(theme, output, color))
#     if output == 'hard' or output == 'middium':
#         deffination(theme)
    
# if __name__ == "__main__":
#     main()
    
    
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Functions from your script (copy here)
def simple():
    with open('data/simple.txt', 'r')as fill:
        return fill.readline()

def hard():
    with open('data/hard.txt', 'r')as fill:
        return fill.readline()

def middium():
    with open('data/middium.txt', 'r')as fill:
        return fill.readline()

def Theme():
    with open('data/theme.txt', 'r')as fill:
        return fill.readline()

def colors():
    with open('data/color.txt', 'r')as fill:
        return fill.readline()

def chosing(theme, output, color):
    if output == "hard":
        iterm = random.choice(hard().split('='))
        colorse = random.sample(color, k=5)
        return f"Create a {iterm} in a {theme} setting using the following colors {', '.join(colorse)}."
    elif output == "easy":
        iterm = random.choice(simple().split('='))
        colorse = random.sample(color, k=2)
        return f"Create a {iterm} using the following colors {', '.join(colorse)}."
    elif output == "middium":
        iterm = random.choice(middium().split('='))
        colorse = random.sample(color, k=3)
        return f"Create a {iterm} in a {theme} setting using the following colors {', '.join(colorse)}."

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        difficulty = request.form.get("difficulty").lower()
        theme = random.choice(Theme().split('+'))
        color = list(colors().split('='))
        output = chosing(theme, difficulty, color)
        return render_template("index.html", output=output, theme=theme)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
