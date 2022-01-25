import pygame

def addText(text, size, bg_color, text_color, coord) {
	fontObj = pygame.font.SysFont("arial", size)
	textSurfaceObj = fontObj.render(text, True, bg_color, text_color)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center  = coord
	window.blit(textSurfaceObj, textRectObj)
	pygame.display.update()
}