import turtle
import random

turtle.penup()

while True:
    try:
        render_speed = int(input("Speed of the render(10 being the highest and 1 being the slowest while 0 is having no animation in between the vertices and only intergers.): "))
        iterations = int(input("Iterations(only intergers): "))
        spacing = float(input("Spacing per iteration(very sensitave): "))
        render_data = ("")
        render_data_random = ("")
        x_coords = float(input("X spawn position: "))
        y_coords = float(input("Y spawn position: "))
        for i in range(10):
            rand = input("Random numerical settings? (type 'confirm' to confirm it and type 'deny' to deny it): ").lower(
            if rand != "confirm" and rand != "deny":
                print("Invalid input please try again")
            elif i == 9:
                print("Defaulted to confirm")
            else:
                break
        rand_dat = (0)
        rand_int_dat1 = (0)
        rand_int_dat2 = (0)
        for_var = (0)
    except ValueError:
        print("Invalid input, please try again")

    break


print("Colours are:")

print("white, white smoke, gainsboro, light gray, silver, dark gray, gray, dim gray, black, light slate gray, slate gray, alice blue, light steel blue, cornflower blue, royal blue, blue, medium blue, navy, dark blue, midnight blue, light blue, deep sky blue, dodger blue, powder blue, sky blue, light sky blue, steel blue, azure, light cyan, cyan, pale turquoise, dark turqoise, turquoise, medium turquoise, light sea green, cadet blue, dark cyan, teal, dark slate gray, mint green, aquamarine, medium aquamarine, dark sea green, medium sea green, sea green, honeydew, pale green, light green, medium spring green, spring green, lime green, green, forest green, dark green, green yellow, chartruse, lawn green, lime, yellow green, olive drab, beige, dark kahki, olive, dark olive green, pale goldenrod, kahki, ivory, light yellow, light goldenrod yellow, cornsilk, lemon chiffon, yellow, gold, goldenrod, dark goldenrod, wheat, tan, burlywood, peru, sienna, saddle brown, floral white, old lace, novajo white, moccasin, sandy brown, orange, dark orange, chocolate, firebrick, brown, dark red, maroon, antique white, papaya whip, blanched almond, bisque, peach puff, light salmon, coral, tomato, orange red, red, crimson, dark salmon, salmon, light coral, indian red, rosy brown, linen, seashell, misty rose, pink, light pink, hot pink, deep pink, snow, lavender bush, pale violet red, violet red, medium violet red, purple, dark magenta, violet, magenta, thistle, plum, orchid, medium orchid, dark violet, blue violet, medium purple, rebecca purple, indigo, ghost white, lavender, light slate blue, medium slate blue, slate blue, and finnaly, dark slate blue.")

background = input("Plz choose the background colour from the above (case sensitave): \n")

turtle.speed(render_speed)
b_col = turtle.Screen()
b_col.bgcolor(background)

if rand == ("comfirm"):
    print("Colours are:")
    print("white, white smoke, gainsboro, light gray, silver, dark gray, gray, dim gray, black, light slate gray, slate gray, alice blue, light steel blue, cornflower blue, royal blue, blue, medium blue, navy, dark blue, midnight blue, light blue, deep sky blue, dodger blue, powder blue, sky blue, light sky blue, steel blue, azure, light cyan, cyan, pale turquoise, dark turqoise, turquoise, medium turquoise, light sea green, cadet blue, dark cyan, teal, dark slate gray, mint green, aquamarine, medium aquamarine, dark sea green, medium sea green, sea green, honeydew, pale green, light green, medium spring green, spring green, lime green, green, forest green, dark green, green yellow, chartruse, lawn green, lime, yellow green, olive drab, beige, dark kahki, olive, dark olive green, pale goldenrod, kahki, ivory, light yellow, light goldenrod yellow, cornsilk, lemon chiffon, yellow, gold, goldenrod, dark goldenrod, wheat, tan, burlywood, peru, sienna, saddle brown, floral white, old lace, novajo white, moccasin, sandy brown, orange, dark orange, chocolate, firebrick, brown, dark red, maroon, antique white, papaya whip, blanched almond, bisque, peach puff, light salmon, coral, tomato, orange red, red, crimson, dark salmon, salmon, light coral, indian red, rosy brown, linen, seashell, misty rose, pink, light pink, hot pink, deep pink, snow, lavender bush, pale violet red, violet red, medium violet red, purple, dark magenta, violet, magenta, thistle, plum, orchid, medium orchid, dark violet, blue violet, medium purple, rebecca purple, indigo, ghost white, lavender, light slate blue, medium slate blue, slate blue, and finnaly, dark slate blue.\n")

    col = input("Plz choose the print colour from above (case sensitave): \n")

    
    rand_int_dat1 = int(input("1st number for randimization: "))
    rand_int_dat2 = int(input("2nd number for randimization: "))
    render_data_random = input("Are you sure you want to render? (type 'go' to render) ")

    turtle.setpos(x_coords, y_coords)
    turtle.pendown()

    if render_data_random == ("go"):
        for forward in range(iterations):
            turtle.forward(forward *rand_dat)
            turtle.left(rand_dat)
            turtle.color(col)
            rand_dat = random.randint(rand_int_dat1, rand_int_dat2)

elif rand == ("deny"):
    print("Colours are:")
    print("white, white smoke, gainsboro, light gray, silver, dark gray, gray, dim gray, black, light slate gray, slate gray, alice blue, light steel blue, cornflower blue, royal blue, blue, medium blue, navy, dark blue, midnight blue, light blue, deep sky blue, dodger blue, powder blue, sky blue, light sky blue, steel blue, azure, light cyan, cyan, pale turquoise, dark turqoise, turquoise, medium turquoise, light sea green, cadet blue, dark cyan, teal, dark slate gray, mint green, aquamarine, medium aquamarine, dark sea green, medium sea green, sea green, honeydew, pale green, light green, medium spring green, spring green, lime green, green, forest green, dark green, green yellow, chartruse, lawn green, lime, yellow green, olive drab, beige, dark kahki, olive, dark olive green, pale goldenrod, kahki, ivory, light yellow, light goldenrod yellow, cornsilk, lemon chiffon, yellow, gold, goldenrod, dark goldenrod, wheat, tan, burlywood, peru, sienna, saddle brown, floral white, old lace, novajo white, moccasin, sandy brown, orange, dark orange, chocolate, firebrick, brown, dark red, maroon, antique white, papaya whip, blanched almond, bisque, peach puff, light salmon, coral, tomato, orange red, red, crimson, dark salmon, salmon, light coral, indian red, rosy brown, linen, seashell, misty rose, pink, light pink, hot pink, deep pink, snow, lavender bush, pale violet red, violet red, medium violet red, purple, dark magenta, violet, magenta, thistle, plum, orchid, medium orchid, dark violet, blue violet, medium purple, rebecca purple, indigo, ghost white, lavender, light slate blue, medium slate blue, slate blue, and finnaly, dark slate blue.")
    print("")

    col = input("Plz choose the print colour from the above (case sensitave): ")

    print("")
    print("To angle right, use a negative number")
    print("")

    angle = float(input("Angle: "))
    
    render_data = input("Are you sure you want to render? (type 'go' to render) ")

    turtle.setpos(x_coords, y_coords)
    turtle.pendown()

    if render_data == ("go"):
        for fw in range(iterations):
            turtle.forward(fw *spacing)
            turtle.left(angle)
            turtle.color(col)
            print("Current iteration is: " + str(fw + 1))

    print("Render succesfully completed. Plz left-click on render window to terminate.")

    turtle.exitonclick
