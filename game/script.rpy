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
    
    "And on to the placeholder/test story"
    jump placeHolderStoryStart

label placeHolderStoryStart:
    ## bendzz added this for testing the branch display system, which will need python
    "Place Holder Story Start \n Megan, early 20’s ish (doesn’t matter much), very introverted and intelligent. Friendly, but shy, she is well suited to the quiet, comfortable environment of the local library."
    
menu: 
    "Ears feel itchy":
        jump EarlyEarItching
        
    "Breasts are tingling":
        jump EarlyBreastExpansion
            
label EarlyEarItching:
    "Girl starts itching behind her ear, which has begun to lengthen slightly. By the end of the scene she’s scratching a lot like a dog."
    jump Walkies
    
label EarlyBreastExpansion:
    " Not much, but enough where she has to fidget constantly with how tight her bra has become, and finds people actually peeking at her cleavage - cleavage she’s never had before."
    jump DirtyDaydreams 
    
label DirtyDaydreams:
    "Girl is bored, and because of the player’s power, she’s finding it harder and harder to concentrate on her work. Instead, she finds her mind wandering to places she’d normally never even come close to imagining."
    "Quick and compelling images flicker through, showing her how hot she’d look if her tits were much, much bigger, or how good exciting it would be to wear a shorter skirt and show off more for the library patrons. Ends when she has one more fantasy, of her on her down on her hands and knees, with a leash dangling down between her tits. Could be recurring."
    jump DvDTrainedDogsGetBred
    
label Walkies:
    "Girl finds a leash and collar inexplicably left unattended somewhere in the library. Looks around for the owner but finds none. Ends up taking them back to the front desk where it becomes more than a little distracting. While she works, she runs her fingers over it constantly, and actually begins to feel more than a little excited, though she has no idea why."
    "Eventually, one of the library patrons comes by and claims the leash, and even offers to take the girl along on a walk as thanks. She agrees immediately, though she’s more than a little shocked when the person slips the collar onto her and tugs her away on the leash."
    
menu:
    "She can't keep up on two feet":
        jump cantKeepOnFeet
    
    "She's feeling ashamed":
        jump feelingAshamed

label cantKeepOnFeet:
    "She feels off balance with how fast he's walking, and gets down on all fours. Every time she tries to ask to go back, or even pull away, the person holding her leash gives it a tug and urges her onward. All throughout she becomes more and more excited about the walk, until she’s practically bouncing around the other person whether she really likes it or not."
    jump DvDTrainedDogsGetBred
    
label feelingAshamed:
    "She simply trails along behind with her head down submissively. By the end she’s a disheveled, embarrassed mess, and she’s more than a little shocked at how she had acted all through out. On top of that though, is the incredibly troubling knowledge that she wouldn’t be able to say no to a repeat of the experience."
    jump DvDTrainedDogsGetBred
    
label DvDTrainedDogsGetBred:
    "A possible ending branch from the second DVD scene. Main character preps her friend for breeding at the prompting of another dvd, completely unaware of her friend changing all the while. At the end, she drops off her new dog at a friend of theirs’ who has a very eager male dog."
    "At this point there’s a branch - She either drops her friend off and goes back to her own steady downfall, while her friend gets to move on to her new life of being constantly bred. OR she watches her friend-turned-bitch get mounted for the first time, and ends up really getting into the scene… slowly becoming overwhelmed with the urge to join the other dog. When she succumbs, that’s the end for her. "
    return

label TODO:
    "Oops, you found a placeholder screen. There's nothing here. Return to main menu."
    ## Two things I didn't test: One is, if you're two branches deep, and the parent branch collapses before the little child branch. The other, is IF statements based on variables that allow for optional later paths. Both will need to be addressed with the node scanning code
    return