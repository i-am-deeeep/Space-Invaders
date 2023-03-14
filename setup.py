import cx_Freeze

executables = [cx_Freeze.Executable("SpaceInvaders.pyw")]

cx_Freeze.setup(
    name="Space Invaders",
    options={"build_exe": {"packages":["pygame","pygame.mixer","pygame.time","random","math"],
                           "include_files":["startgame.wav","overheat.wav","logopp3.png","highscore.wav","giftbox.png","coin.png","coin_collect.wav","bullet(2).png","bullet(1).png","bullet(-2).png","bullet(-1).png","box_collect.mp3","exee.txt","alien1.png","alien2.png","alien3.png","alien4.png","alien5.png","alien6.png","background-music.wav","background.png","bullet.png","crash.wav","enemy_bullet.png","explosion.wav","game-over.wav","icon.png","IndieFlower-Regular.ttf","laser.wav","README.md","spaceship.png","spaceship_dead.png"]}},
    executables = executables

    )



