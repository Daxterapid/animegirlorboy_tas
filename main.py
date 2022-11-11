from pynput import mouse
from pynput import keyboard
import time

delay = 0.01

ms = mouse.Controller()
kb = keyboard.Controller()

girls = [(578, 292), (424, 424), (306, 234)]
boys = [(593, 292), (829, 415), (313, 240)]

girl_levels = [
    [(182, 373), (1085, 347)],
    [(1019, 238), (614, 449), (491, 266)],
    [(157, 474), (720, 495), (926, 501)],
    [(223, 531), (460, 308), (635, 291), (928, 500)],
    [(229, 260), (462, 484), (727, 267), (908, 476), (1122, 255)],
    [(182, 266), (299, 499), (552, 507), (853, 296), (980, 297), (1041, 518), (1039, 279)],
    [(91, 268), (126, 479), (304, 550), (688, 305), (708, 530), (1104, 352), (1101, 529)],
    [(210, 302), (228, 559), (400, 511), (583, 517), (587, 311), (719, 325), (911, 562), (1083, 533)],
    [(169, 487), (289, 354), (345, 500), (512, 497), (843, 338), (871, 535), (1018, 500), (1135, 322)],
    [(111, 510), (235, 511), (306, 331), (506, 332), (610, 328), (648, 522), (986, 490), (1097, 495)]
]

boy_levels = [
    [(199, 313), (775, 310)],
    [(136, 468), (285, 300), (974, 471)],
    [(530, 456), (738, 275), (879, 483)],
    [(616, 301), (812, 254), (1092, 464)],
    [(186, 245), (358, 236), (572, 502), (945, 319), (978, 487)],
    [(152, 504), (149, 326), (558, 258), (709, 250), (1119, 480), (1131, 253)],
    [(288, 492), (341, 281), (476, 254), (700, 464), (880, 279), (1011, 504), (1169, 278)],
    [(138, 552), (349, 321), (365, 524), (518, 511), (781, 291), (932, 491), (1079, 482), (1155, 269)],
    [(168, 534), (163, 323), (541, 321), (556, 524), (701, 525), (878, 498), (1124, 281)],
    [(264, 288), (269, 534), (431, 524), (644, 290), (943, 528), (959, 320), (1111, 306)]
]

time.sleep(3)

for pos in girls:
    ms.position = (pos[0], pos[1])
    time.sleep(delay)
    ms.click(mouse.Button.left)
    time.sleep(delay)

for level in girl_levels:
    for pos in level:
        ms.position = (pos[0], pos[1])
        time.sleep(delay)
        ms.click(mouse.Button.left)
        time.sleep(delay)
    
    kb.press(keyboard.Key.enter)
    time.sleep(delay)
    kb.release(keyboard.Key.enter)
    time.sleep(delay)

for pos in boys:
    ms.position = (pos[0], pos[1])
    time.sleep(delay)
    ms.click(mouse.Button.left)
    time.sleep(delay)

for level in boy_levels:
    for pos in level:
        ms.position = (pos[0], pos[1])
        time.sleep(delay)
        ms.click(mouse.Button.left)
        time.sleep(delay)
    
    kb.press(keyboard.Key.enter)
    time.sleep(delay)
    kb.release(keyboard.Key.enter)
    time.sleep(delay)
