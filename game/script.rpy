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

define m = Character('Megan')
define k = Character('Kira')
define strange = Character('Strange Man')

# Set the default value.
init python:
    if persistent.Bestiality is None:
        persistent.Bestiality = True


# Declare characters used by this game.

define m = Character('Megan')
define k = Character('Kira')
define strange = Character('Strange Man')
define DT = Character ('Dog Trainer')

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
    jump meganIntro1
    
label meganIntro1:
    "The library is peaceful, housing the usual mix of hastily-studying students, placidly content bibliophiles, and a handful of eployees to sedately maintain order… Sometimes a little too sedately, it would seem, from the many pairs of glazed over eyes in sight."
    "In fact, of all the librarians in attendance today, only one of them looks pleased to be there: Megan."
    "She’s sitting at the main desk, alert and engaged with the task of efficiently sorting through and checking in a fairly sizable stack of returns. Despite the repetitive nature of the work to be done, the young woman seems more than pleased to be the one to do it." 
    "In fact, the only thing that seems to remotely dampen her perky demeanor and sunny spirits is the arrival of people looking to check-out. Every time someone steps up to the counter, there’s a small, but noticeable hesitation to her otherwise brisk movements." 
    "While she maintains an unwaveringly polite smile, her slightly trembling hands and nervously darting eyes make it clear that she’d rather be doing anything else but interacting with other people. 
    Still, despite her shyness, she manages to handle each patron with the same pleasant efficiency as with her more desirable tasks."
    "Each time they leave, though, it's as if a terrible weight was lifted. The very moment she’s left alone again the girl slumps down into her chair with a sigh of relief. She doesn’t relax for even a second before she moves back to the giant pile of books, though." 
    "From the way she looks over each tome with obvious interest and enthusiasm, it would seem as though being alone with her work is more than enough.
    Little does she know she’s not alone at all, and the presence of other human beings should be the least of her worries…"
    with fade
    ## From here, we do a fade out, and move to the dvd scene. Will work on the transition later. The reason these are separate is to allow for easier branches - things like different tfs and such that might not do the dvd scene.
    jump meganIntro2
    
label meganIntro2:
    ## bendzz added this for testing the branch display system, which will need python
    ## Stray The segment here is separated into two lines for purely visual and ease of reading purposes - looks no different in game. I'll be continuing that trend in other segments as well.
    "Megan is in her usual spot, settled in behind the library counter. Every inch of her work area is well-maintained, and there isn’t a trace of a thing out of place or a book left to check in."
    "Being obligated to remain at the front desk, the normally perky and content girl is beginning to look almost as bored and anxious to leave as her fellow co-workers."
    "Left waiting for new arrivals and customers to assist, Megan turns to her work computer to pass the time."
    "Even though she’s done everything she was expected to do, as always she feels a little guilty to be on the internet during work hours. On top of that, the book trivia site she went to was starting to get more than a little stale, considering she knew most of the answers by heart already."
    "Still, she didn’t feel comfortable going beyond this one indulgence, and with an uncharacteristically bored sigh she brings up another round of trivia. It only takes a word or two on each before she recognizes the question and is able to click the correct answer." 
    "Before long, her eyes are almost glazed over, and her hand is practically moving the mouse on muscle memory alone.
    It’s  mind-numbing to the point of almost being worse than just staring off into space." 
    "It’s so bad that - despite her shyness - the young librarian actually finds herself wishing for a visitor or two.
    Anything to add a little more excitement or activity to this dreadfully dull day."
    jump meganDogstart1
    
label meganDogstart1:
    
    strange "I found this."
    m "Eeek!"
    "Megan sits upright with an embarrassingly loud squeak of surprise. She hadn’t noticed the man even come inside the library, much less approach her counter."
    "'I must have been more into the trivia than I thought… Or I nodded off,' Megan thinks to herself."
    "Her visitor showed no signs of caring one way or the other. 
     In fact, he barely seems to notice her at all, aside from thrusting what looks like an unmarked dvd case in her general direction."
    "Though she blushes furiously at both the sound she made and the possibility of being caught asleep at her desk, Megan quickly recovers."
    "In the space of a heartbeat she gets herself back into her polite-problemsolver mode, turning to face her visitor with the usual smile and undercurrent of anxiety."
    m "I can certainly help you with-"
    strange "I found this."
    "There’s a strange urgency to the man’s voice that’s at odds with the vacant stare he seems to be giving to the wall right behind Megan’s head. 
    It gives the young woman a chill, prompting her to take the case from the man - if only to get him to leave a bit sooner."
    "As uneasy as she’s feeling, Megan cherishes the opportunity to have something other than her visitor to look at. 
    It takes only a cursory glance to see there are no barcodes or labels on the case, but she takes her time staring down at it intently – mostly to have a moment to calm her nerves."
    m "Thank you for showing me this, but I don’t think this is one of our-"
    "Looking up, Megan pauses mid-sentence." 
    "The man is nowhere to be seen. She had heard no sound, and there was no sign he had been there at all aside from the case still in her hands." 
    "As unsettling as his exit was, the young librarian is just glad her visitor is gone, and without incident."
    k "Hey, I heard a-"
    m "Eeek!"
    "Megan’s heart thuds in her chest while her coworker, Kira, bursts into a gale of laughter."
    k "Yeah *giggle* that’s about what I heard!"
    m "J-just shut up!"
    "Kira looks on in shock as Megan pushes past. She’s never seen the other girl so worked up before, and its clear she regrets making light of things."
    k "Hey, I’m sorry… Everything okay?"
    m "I’m fine! J-just watch the front for me, will you?"
    k "Sure, but..."
    with fade
    jump meganDvd1
    
label meganDvd1:
    "Most of the other employees would head to the break room to relax, but the cluttered kitchenette gave the shy girl no solace. 
    Instead, she heads to where she usually goes to hide on her breaks: the AV room."
    "Easily the least populated area in the entire library, the AV room is the perfect refuge for the unsettled girl. 
    Housing nothing more than a battered lounge chair and TV that were both older than most of the library employees, there’s little reason for anyone to bother with the place beyond checking some of the more banged up bits of media for defects."
    "Settling into the scuffed and slightly musty-smelling chair, Megan takes a few long, deep breaths. It’s a tactic she’s used many times before to deal with her anxiety issues, and it works just as well now to help clear her head."
    "Soon enough she’s actually almost laughing at herself – held back only by her embarrassment over how she’d acted."
    m "He was probably just awkward like me… All he wanted to do was return some DVD he-"
    "Looking down, Megan realized she was still holding the scuffed-up case in her hands. Immediately after, her eyes flicked up to the ancient TV in front of her, and the third rate DVD player mounted on top of it. All at once, she just knew she had to see what was on the disc."
    "Part of it was shame over how she’d reacted, and another part was sheer curiousity… but beyond that, she simply felt compelled in a way she couldn’t quite parse."
    "Before she knew it, Megan began popping open the case. The disk was unmarked, just the same as the container which held it. Little hints of anxiety began to bleed back into the young woman." 
    "There was no way this was library property, and there was no knowing what would show up on that dimly lit screen once she pressed play."
    m "Please don’t be porn... Please don’t be porn... Please don’t be porn..."
    "There were also about a million other things she didn’t want it to be, but porn was easily the most likely. 
    This isn’t the first time she’s had to stare down the barrel of some mystery content - and nearly every other time the wrong disc came back in, she got a momentary eye-ful of fucking before she could react."
    "Knowing not to lower her guard, Megan’s finger hovers over the stop button as she presses play with her other hand. Again, she takes a few deep breaths, preparing herself for all manner of unsavory sights."
    DT "Welcome to the Happy Puppy Training DVD, where we help you turn your malevolent mutts into docile, dutiful doggies!"
    m "Huh."
    "An obedience training program wasn’t at all what she was expecting, though she’s certainly glad to be faced with an exception in this case. Flooded with relief, the young woman flops back into her seat."
    DT "Now, the key to a well-behaved bitch is making sure she understands her role. Even very good doggies can get confused if they’re not sure how they should act. This is especially true if the dog is a shy one – anxiety can make a bitch forget her training."
    m "Ugh, that’s the truth."
    "Megan knows the man is talking about dogs, and not anxiety-ridden young librarians, but she can’t help but think about how poorly she reacted to the man before, purely because of her own nerves."
    DT "Once the bitch truly knows her place, she can react appropriately to even the most stressful of situations."
    "Megan nods along with the man’s confident words. Just the thought of having someone finally give her a solid answer to her shyness was enough to have her kind of wishing she was one of the dogs he was talking about…"
    DT "Now, just to start things right, I’m going to talk directly to the deviant doggy in the room. I’m going to tell her exactly what’s expected of her, so that there’s no more confusion, and no more stress."
    "Again, Megan finds herself nodding."
    m "No more confusion… No more stress…"
    DT "Hey there! Who’s a good girl, huh? Who’s a good girl?"
    "Megan feels a sudden rush of excitement, sitting up her chair fast enough to leave her a little dizzy. Holding her head a moment, she laughs at herself for reacting like she did. Even though the  man is looking straight at her, he’s talking to the dog he’s assuming is there."
    DT "It’s okay to be excited, girl! Go on, show me who’s a good girl!"
    "He just sounds so excited, and Megan is so, so confused – she can’t help it any longer. Suddenly she’s up from the chair, practically hopping in front of the TV."
    m "I am! I’m a good girl!"
    "Before she can stop and think about what she’s doing, the man on the DVD continues."
    DT "That’s right! You’re a very good doggy! Oh, yes you are! You’re a good girl!"
    "Megan shivers with delight at the massive pleasure-rush that slams into her mind. The gasp that follows leaves her literally panting, as every inch of her tingles with sweet assurance and approval."
    DT "See? You want to be a good doggy, don’t you, girl?"
    m "Y-yes!"
    "Megan is too far gone to notice how much her reply sounds like a sharp, eager bark."
    DT "Good girl!"
    "Again, there’s that rush of pure bliss, leaving Megan weak in the knees… and mind."
    DT "I’m going to help you be the best doggy you can be! Now sit!"
    "Megan hits the floor faster than her mind can process what she’s doing. The movement is so sharp and immediate that the seam on her long skirt actually begins to split as she drops to a very canine-looking crouch."
    "Knees wide enough to stretch out her clothes, the young librarian tries very hard to sit like she was told. Her outfit - so comfortable a moment ago – begins to feel like a terrible, tangling net. 
    Even her blouse is ill-fitting, holding her back from comfortably resting her front paws in front of her…"
    "Megan feels guilty as she stands and begins to frantically shuck off her clothing. It’s not modesty or shyness now that bothers her now,  it’s the feeling of disappointment and shame at not being able to perform even this one simple trick." 
    "It’s strong enough that she’s begun to whimper loudly during her efforts, punctuated by low growls when her paws fumble at the buttons and clasps."
    "While it feels like an eternity to the panting, whimpering girl, it only takes a few moments before she’s happily, comfortably nude. Only her necklace and hair ties remain on, and only because neither got in the way of her obedience."
    "A dopey smile spreads on her face as she drops down into a crouch once more, planting her front paws down on the dirty ground right below her crotch. The position isn’t easy to maintain, while also managing to keep her eyes on the screen. For a moment she even considers hopping up into the chair, but the thought fades quickly. Dogs aren’t allowed on the furniture."
    "Still feeling some lingering guilt over how long it took her to sit, Megan looks meekly up at the screen. Her ass wiggles tentatively behind her, and a soft whine periodically slips in through her panting. Thankfully, it seems the nice, smart man on the TV is still talking to her owner."
    "There’s a whole bunch of things he says about food she should be fed, and ways to prepare her for meeting other dogs, but none of that interests Megan. She hears it, and it sinks into her vulnerable mind more so every second, but it’s all well beyond her."
    DT "Now, back to our well-behaved bitch!"
    "The higher, more excited tone of the man’s voice causes Megan’s excitement to hit overdrive again, with only the order to sit keeping her from crawling over to the TV and lapping happily at the screen. Her ass wags fast enough to make her small breasts sway - held back only by the awkward position – and drool drips from her tongue unimpeded."
    DT "We’re going to do a few more tricks, just so you can show your owner what a good doggy you are!"
    m "Arf! Arf!"
    DT "That’s a good girl! Now roll over!"
    "The carpet is covered in random dust and detritus, and there’s a sizeable wet spot where Megan’s drool had sunk in. Despite all that, it feels like pure heaven to the panting girl as she rolls her naked body over on it."
    "She ends up on her back, paws up and eyes intently on the screen as she waits for either new orders, or a belly rub. Pure exhilaration pumps through her - pounding in her silly, canine brain – echoing the words ‘Good doggy, good girl, good doggy, good girl’."
    "While she waits obediently, the man says a few more things to her absent owner. Like before, the words either make no sense, or hold no interest to Megan. Regardless, much of what he’s saying is focused on a word she seems to know… a word that she feels might be very, very important: heat."
    "She doesn’t try to figure out the meaning – not consciously anyway. Instead, her body seems to figure it out for her, letting her mind stay mired in it’s blissful, doggy haze. "
    "It begins with a light, soft tingle, spreading over her skin. Pleasure swirls around, even seeming to almost caress her exposed belly like a rub from her owner. The sensation is excrutiatingly brief,  moving lower and deeper, and leaving Megan wanting more, more, more."
    "The sense of wanting becomes an aching need as the heat hits her bare sex. Her knees spread little by little, exposing the glistening wetness that’s begun to trickle down from her swollen lips. The blush that began with excitement now deepens with animal lust, and her once-focused eyes become glazed over with the need to be bred."
    DT "Up girl! Beg!"
    "Despite her growing urges, Megan responds with perfect obedience. She no longer even thinks about the tricks she’s to perform – the actions are now as natural to her as her heat has become." 
    "Before she knows it, the young librarian is perched up on the balls of her feet, her paws flanking her perky breasts."
    "Still the need to mate intensifies, mingling with the overwhelming joy that follows when the man on the screen tells her she’s a good girl once more. The throbbing inside grows deeper, leaving her trembling with every pulse."
    DT "You want a treat, don't you, girl? Don't you?"
    "Megan doesn’t nod, or reply. Instead, she shivers in place, whining for release, while her pussy drips obscenely below her. Like her unfaltering obedience, her want for a treat is implied by her adherence to her trainer’s wishes."
    DT "Alright, if you’ve gotten this far you’ve been a very good doggy. Have a treat!"
    "The man goes on to talk to Megan’s owner about treats, reinforcement and part two of the DVD. Megan hears none of this. Instead, the shy girl falls forward onto all fours, bucking her hips wildly as she experiences the single most intense climax of her entire life."
    "{i}Good girl. Good dog. Have a treat. Good girl. Good dog. Have a treat.{/i}"
    "The words pound into her like the frenzied thrusts of a rutting hound, each repetition only carving the pround messages more permanently into her very core."
    "After an eternity the flames of heat begin to gutter out inside of Megan, taking the very last of her excitement and energy along with them. Bereft of her instinctual need and the voice that guided her, the young woman collapses onto the damp, dirty carpet." 
    "As unconsciousness overtakes her, she glances up just in time to see the television flick off, entirely on its own."
    
    jump WIP

label beginning: 
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