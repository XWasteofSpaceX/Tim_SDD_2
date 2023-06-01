while start == False:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            hitButton = pygame.sprite.groupcollide(allButtons, darts, False, False)
            for balloon in (hitBalloons):
            # if the mouse is clicked on the
            # button the game is started
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                 start = True

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # if mouse is hovered on a button it
    # changes to lighter shade

    if ev.type == pygame.MOUSEMOTION:
        mousePosition[:] = list(ev.pos)
        dart.moveDart(mousePosition)


    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])
    # superimposing the text onto our button
    screen.blit(text, (width / 2 + 50, height / 2))
    screen.blit(text2, (width / 2 + 20, height / 1))
    screen.blit(but(0,0))
    # updates the frames of the game
    pygame.display.update()
