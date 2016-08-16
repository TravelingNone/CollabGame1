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
    $ dogTail = 0
    $ dogEar = 0
    $ heat = 0
    $ titSize = 0
    $ titNumber = 2
    "Will insert intro here - brief hook that brings the player straight to the library, explains intent, and shows them Megan for the first time."
    
    "And on to the placeholder/test story"
    jump placeHolderStoryStart

label placeHolderStoryStart:
    ## bendzz added this for testing the branch display system, which will need python
    ## Stray The segment here is separated into two lines for purely visual and ease of reading purposes - looks no different in game. I'll be continuing that trend in other segments as well.
    "Megan is in her usual spot, settled in behind the library counter and slowly browsing the internet for pointless trivia. Every inch of her work area is well-maintained, and there isn’t a trace of a thing out of place, or a book still to shelve. 
     Despite her shyness, with how slow the day has been, the young librarian actually finds herself wishing for a little more excitement..."
    
menu: 
    "There's a funny itch behind her ear...":
        if dogEar < 1:
            $ dogEar += 1
            jump EarlyEarItching
        else:
            jump EarlyEarItching
        
    "Her breasts begin to tingle...":
        if titSize < 1:
            $ titSize += 1
            jump EarlyBreastExpansion
        else:
            jump EarlyBreastExpansion
    "She feels a sudden heat...":
        if heat < 1:
            $ heat += 1
            jump EarlyArousal
        else:
            jump EarlyArousal
            
label EarlyEarItching:
    "Megan clicks through the various websites she uses to fill the time, largely on autopilot. No library patrons interrupt her boredom, and the only stimulation she feels is an annoying tickle behind her ear. She idly scratches at it while she browses and yawns."

"It only gets worse, prompting her to put more effort into it. Before long she begins leaning her head into it, and scratching in quick, rough movements that shake her whole body. 
 It feels amazing, to the point where she practically growls in frustration as she’s interrupted by a check-out to process."

"The moment the patron heads out, Megan is back to scratching – this time behind her other ear. 
 Already the tickling was much reduced, but it was enough to keep her going back. Besides that, it just felt really, really good for some reason she couldn’t put her finger on…"

menu:
    "The feeling slowly recedes, but the changes remain...":
        jump RoundTwoMenu
    "She catches sight of her reflection, causing her to gasp!":
        jump WIP
    
label EarlyBreastExpansion:
    "Megan discreetly scratches herself as an odd tingling begins to spread in her chest. Even though no one is around to see, she still blushes profusely every second she tries to ease the strange and sudden itch. 
     That blush only deepens as she finds herself having to readjust her bra, as the strap seems to be almost painfully tight."

    "It makes no sense… This is one of her favorite bras, purely because of how comfy it typically was."

    "“Did it shrink or something?” she mutters, fidgeting uncomfortably."
    
menu:
    "Still growing...":
        if titSize < 2:
            $ titSize += 1
            jump EarlyBreastExpansion2
        else:
            jump EarlyBreastExpansion2
    "The tingling calms, though her bra still feels far too small.":
        jump RoundTwoMenu
        
label EarlyBreastExpansion2:
    "Helping a patron check out, Megan is interrupted by a sudden loud creaking sound. The lady she’s helping seems to notice, but says nothing as the bashful young librarian hastily does her job. 
     As the woman leaves, Megan feels the impossible sensation of the first hook of her bra giving out."

    "Panicking, Megan puts up her ‘Back in five minutes!’ sign and runs for the backroom. She’s not supposed to leave the desk unattended, but she doesn’t have the time to hunt down any of the other library employees – already she can feel the strap straining harder. 
     Worse is the unfamiliar feeling of weight on her chest as she goes, and the bouncing of her breasts with every hastened step."

    "She gets two steps into the ladies room when the bra gives in, popping open with a loud snap. Megan locks the door behind her, wishing under her breath that no one finds themselves with a sudden pressing need to come inside. 
     Only when the deadbolt clicks into place does she feel comfortable enough to start fearfully unbuttoning her blouse…"

menu:
    "Buttons begin to fly...":
        if titSize < 3:
            $ titSize += 1
            jump WIP
        else:
            jump WIP
    "They're big, but they've stopped growing for now.":
        "She’s already making excuses as her swollen breasts come into view – an allergic reaction, something stress-related, really late growth spurt; anything to explain the impossible sight of her own larger tits. 
         Taking off her blouse, she finds the clasp of her bra to be wholly unusable now, but that’s just as well – there’s no way she’d be able to fit anyway."
        "Megan is in humiliated shock as she slips her blouse back on and buttons it up."
        jump RoundTwoMenu

    
label EarlyArousal:
    "Megan is halfway done stifling another yawn when she begins to feel something more than a little unexpected. It starts slowly, with the slightest spread of warmth through her body, which is gradually joined by the steady thump of her quickened heartbeat. After only a few moments, it was unmistakable… Megan felt horny."

    "There was no cause, and she hadn’t been thinking of anything even remotely sexy, but there was no denying how she suddenly felt: a little like two glasses of wine, a good, slightly racy romance novel and some time to herself – only completely out of nowhere, and while sitting on the edge of her battered desk chair instead of her comfy bed at home."

    "Confused and embarrassed, the young librarian tries to put the sudden surge of arousal out of her mind. It’s nearly impossible, both due to the lack of work to keep her occupied, and the incredibly insistent feeling of need in her trembling body…"

menu:
    "She can't help it - it's too much! She NEEDS to let off some pressure.":
        if heat < 2:
            $ heat += 1
            jump WIP
        else:
            jump WIP
    "It's shameful and more than a little distracting, but she can bear it for now.":
        jump RoundTwoMenu
    
label RoundTwoMenu:
    jump WIP
        
label WIP:
    "This node is not yet fleshed out - Please go back!"
    $ renpy.rollback(force=True, checkpoints=1, defer=True, greedy=True, label=None)

    

label TODO:
    "Oops, you found a placeholder screen. There's nothing here. Return to main menu."
    ## Two things I didn't test: One is, if you're two branches deep, and the parent branch collapses before the little child branch. The other, is IF statements based on variables that allow for optional later paths. Both will need to be addressed with the node scanning code
    return