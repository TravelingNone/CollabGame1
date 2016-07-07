# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image loading1 = "Loading1.jpg"
image loading2 = "Loading2.jpg"
image loading3 = "Loading3.jpg"
image menuIdle = "menuIdle.jpg"
image menuHovering:
    "menuHover00.jpg"
    .10
    "menuHover01.jpg"
    .10
    "menuHover02.jpg"
    .10
    "menuHover03.jpg"
    .10
    "menuHover04.jpg"
    .10
    "menuHover05.jpg"
    .10
    "menuHover06.jpg"
    .10
    "menuHover07.jpg"
    .10
    "menuHover08.jpg"
    .10
    "menuHover09.jpg"
    .10
    "menuHover10.jpg"
    .10
    "menuHover11.jpg"
    .10
    "menuHover12.jpg"
    .10
    "menuHover13.jpg"
    .10
    "menuHover14.jpg"
    .10
    "menuHover15.jpg"
    .10
    "menuHover16.jpg"
    .10
    "menuHover17.jpg"
    .10
    "menuHover18.jpg"
    .10
    "menuHover19.jpg"
    .10
    "menuHover20.jpg"
    .10
    "menuHover21.jpg"
    .10
    "menuHover22.jpg"
    .10
    "menuHover23.jpg"
    .10
    "menuHover24.jpg"
    .10
    "menuHover25.jpg"
    .10
    "menuHover26.jpg"
    repeat
    
default hope1 = False
default hope2 = False
default hope3 = False
default hope4 = False
default hope5 = False 

# Set the default value.
init python:
    if persistent.Bestiality is None:
        persistent.Bestiality = True

$ dogTail = False
$ dogEars = False


# Declare characters used by this game.
define m = Character('Megan', color="#c8ffc8")
init:
    image dog1 = "baddog.jpg"
    image dog2 = "gooddog.png"

# The game starts here.
label splashscreen:
    $ renpy.start_predict("menuHovering")
    scene black 
    $ renpy.pause(.5)

   # show loading1 with dissolve
   # $ renpy.pause(0.5)
    
   # show loading2 with dissolve
   # $ renpy.pause(0.5)
    
   # show loading3 with dissolve
   # $ renpy.pause(0.5)
    
   # scene black with dissolve
   # $ renpy.pause(1.0)
    
    return
    
label mainMenu:

    with fade

label start:
    image cg1 = "cg1.jpg"
    image cg2 = "cg2.jpg"
    image cg3 = "cg03.jpg"
    "Behold all the beautiful exposition."
    "Just kidding. Go make some bitches!"
    
    return