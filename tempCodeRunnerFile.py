for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    pause=False
                    restartGame()