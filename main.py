import pygame
import ui_engine as ui


main_screen = pygame.display.set_mode((450,710))

main_text_surface = ui.custom_surface(main_screen,10,10,430,100)
main_text = ui.text_label(main_text_surface, 0,0,'',64,color= '#FFFFFF',placement= 4, placement_offset= [10,0])
main_text_surface.content.add(main_text)

main_answer_surface = ui.custom_surface(main_screen,10,120,430,100)
main_answer_text = ui.text_label(main_answer_surface, 0,0,'',64,color= '#FFFFFF',placement= 4, placement_offset= [10,0])
main_answer_surface.content.add(main_answer_text)

button_surface = ui.custom_surface(main_screen, 0,220,500,550)
button_surface.set_colorkey('#000000')

button_1 = ui.button(button_surface, 10,10,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_1_text = ui.text_label(button_1.button_rect,0,0,'1',64,placement= 5)
button_1.button_rect.content.add(button_1_text)

button_2 = ui.button(button_surface, 120,10,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_2_text = ui.text_label(button_2.button_rect,0,0,'2',64,placement= 5)
button_2.button_rect.content.add(button_2_text)

button_3 = ui.button(button_surface, 230,10,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_3_text = ui.text_label(button_3.button_rect,0,0,'3',64,placement= 5)
button_3.button_rect.content.add(button_3_text)

button_4 = ui.button(button_surface, 10,130,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_4_text = ui.text_label(button_4.button_rect,0,0,'4',64,placement= 5)
button_4.button_rect.content.add(button_4_text)

button_5 = ui.button(button_surface, 120,130,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_5_text = ui.text_label(button_5.button_rect,0,0,'5',64,placement= 5)
button_5.button_rect.content.add(button_5_text)

button_6 = ui.button(button_surface, 230,130,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_6_text = ui.text_label(button_6.button_rect,0,0,'6',64,placement= 5)
button_6.button_rect.content.add(button_6_text)

button_7 = ui.button(button_surface, 10,250,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_7_text = ui.text_label(button_7.button_rect,0,0,'7',64,placement= 5)
button_7.button_rect.content.add(button_7_text)

button_8 = ui.button(button_surface, 120,250,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_8_text = ui.text_label(button_8.button_rect,0,0,'8',64,placement= 5)
button_8.button_rect.content.add(button_8_text)

button_9 = ui.button(button_surface, 230,250,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_9_text = ui.text_label(button_9.button_rect,0,0,'9',64,placement= 5)
button_9.button_rect.content.add(button_9_text)

button_0 = ui.button(button_surface, 10,370,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_0_text = ui.text_label(button_0.button_rect,0,0,'0',64,placement= 5)
button_0.button_rect.content.add(button_0_text)

button_subtract = ui.button(button_surface, 340,10,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_subtract_text = ui.text_label(button_subtract.button_rect,0,0,'-',64,placement= 5)
button_subtract.button_rect.content.add(button_subtract_text)

button_add = ui.button(button_surface, 340,130,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_add_text = ui.text_label(button_add.button_rect,0,0,'+',64,placement= 5)
button_add.button_rect.content.add(button_add_text)

button_mutiply = ui.button(button_surface, 340,250,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_mutiply_text = ui.text_label(button_mutiply.button_rect,0,0,'X',64,placement= 5)
button_mutiply.button_rect.content.add(button_mutiply_text)

button_divide = ui.button(button_surface, 340,370,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_divide_text = ui.text_label(button_divide.button_rect,0,0,'/',64,placement= 5)
button_divide.button_rect.content.add(button_divide_text)

button_AC = ui.button(button_surface, 120,370,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_AC_text = ui.text_label(button_AC.button_rect,0,0,'AC',64,placement= 5)
button_AC.button_rect.content.add(button_AC_text)

button_equal = ui.button(button_surface, 230,370,100,100,['#2E4053','#D74B4B','#D35400'], elevation= 10)
button_equal_text = ui.text_label(button_equal.button_rect,0,0,'=',64,placement= 5)
button_equal.button_rect.content.add(button_equal_text)

button_list = [button_0,button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_subtract,button_add,button_mutiply,button_divide,button_AC,button_equal]

button_surface.content.add(button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_0)
button_surface.content.add(button_subtract,button_add,button_mutiply,button_divide,button_AC,button_equal)

def calculate(text):
    list = text.split(' ')
    while len(list) != 1:
        if list[1] == '+':
            list[0] = str(float(list[0]) + float(list[2]))
        if list[1] == '-':
            list[0] = str(float(list[0]) - float(list[2]))
        if list[1] == '*':
            list[0] = str(float(list[0]) * float(list[2]))
        if list[1] == '/':
            list[0] = str(float(list[0]) / float(list[2]))
        list.pop(1)
        list.pop(1)
    main_answer_text.text = list[0]
    main_answer_text.update()

run = True
while run:
    main_screen.fill('#1B2631')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                main_text.text = main_text.text[:-1]
                main_text.update()
    
    for index,button in enumerate(button_list):
        if button.press() == 'clicked':
            if index <=9: 
                main_text.text += str(index)
                main_text.update()
            if index == 10:
                main_text.text += ' - '
                main_text.update()
            if index == 11:
                main_text.text += ' + '
                main_text.update()
            if index == 12:
                main_text.text += ' * '
                main_text.update()
            if index == 13:
                main_text.text += ' / '
                main_text.update()
            if index == 14:
                main_text.text = ''
                main_text.update()
                main_answer_text.text = ''
                main_answer_text.update()
            if index == 15:
                calculate(main_text.text)
                main_text.text = ''
                main_text.update()


    main_text_surface.draw()
    main_answer_surface.draw()
    button_surface.draw()
    pygame.display.update()