# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define e = Character('joe', image = 'chuukichi' )


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Maybe I can use this to show the thoughts of the character."
    show chuukichi normal with moveinleft
    
    e "I'm testing writing my first game."

    e thinking "This is okay." with dissolve
    
    show chuukichi happy at right with dissolve
    
    e "There really isn't much to it."
    
    menu:
        "Choice 1":
            e "Okay"
            show joe blush at left with fade
        "Second Choice":
            "test"

    jump test

    # This ends the game.

    return
