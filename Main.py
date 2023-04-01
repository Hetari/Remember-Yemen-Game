import pandas
import turtle
import os


os.system("cls")
city = pandas.read_csv('Cities.csv')

img = "yemen43.gif"
english = [
    "Sana'a", "Aden", "Taiz", "Al hudaydah", "Ibb", "Dhamar", "Hadramaut", "Al mahwit", "Al jawf", "Lahij", "Shabwah", "Marib", "Raymah", "Al bayda", "Hajjah", "Sa'dah", "Amran", "Al dhale'e", "Abyan", "Al mahra", "Socotra"
]
ar_to_en = {
    'صنعاء': "Sana'a", 'عدن': 'Aden', 'تعز': 'Taiz', 'الحديدة': 'Al hudaydah', 'اب': 'Ibb', 'ذمار': 'Dhamar', 'المحويت': 'Al mahwit', 'حضرموت': 'Hadramaut', 'الجوف': 'Al jawf', 'شبوة': 'Shabwah', 'لحج': 'Lahij', 'مأرب': 'Marib', 'ريمة': 'Raymah', 'البيضاء': 'Al bayda', 'حجة': 'Hajjah', 'صعدة': "Sa'dah", 'عمران': 'Amran', 'الضالع': "Al dhale'e", 'المهرة': 'Al mahra', 'ابين': 'Abyan', "سقطرى": "Socotra"
}
guessed = []


screen = turtle.Screen()
screen.setup(1040, 632)
screen.addshape(img)
screen.title("Remember Yemen Game")
turtle.shape(img)

pen = turtle.Turtle()
pen.hideturtle()

while True and len(guessed) < 21:
    pen.penup()
    try:
        input = screen.textinput(
            title=f'{len(guessed)}/21 Guess the city', prompt='Another city?')

        if not input.isascii():
            input = ar_to_en[input]
        else:
            input = input.capitalize()

        if input == 'Exit':
            missed = [city for city in english if city not in guessed]

            write = pandas.DataFrame(missed)
            write.to_csv("Missed Cities.csv")
            break

        x_pos = int(city[city["City"] == input].x)
        y_pos = int(city[city["City"] == input].y)

    except KeyError:
        print("The city isn't correct!")
        continue

    except TypeError:
        print("Please enter a correct value!")
        continue

    except AttributeError:
        print('Exit...')
        break


    if input not in guessed:
        guessed.append(input)
        pen.goto(x_pos, y_pos)
        pen.pendown()
        pen.write(arg=input, font=('Arial', 8, 'bold'))
    else:
        print("The city is already guessed!")


screen.exitonclick()
