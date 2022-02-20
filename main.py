import tkinter
import time
import win32gui
from PIL import ImageGrab
import numpy as np
import cv2
import tkinter.font as tkfont
import pygame
pygame.mixer.init()

class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("하드 진힐라 자동 타이머")
        self.pack(fill='both', expand=True)

        self.game_hwnd = 0

        windows_list = []
        toplist = []

        def enum_win(hnd, result):
            win_txt = win32gui.GetWindowText(hnd)
            windows_list.append((hnd, win_txt))

        win32gui.EnumWindows(enum_win, toplist)
        print(windows_list)
        for (hwnd, win_text) in windows_list:
            if "MapleStory" in win_text:
                position = win32gui.GetWindowRect(hwnd)
                screenshot = ImageGrab.grab(position)
                screenshot = np.array(screenshot)
                if len(screenshot[0]) == 1372:
                    self.game_hwnd = hwnd
                    print('detected')
                    break
        fnt = tkfont.Font(family="맑은 고딕", size=16)
        self.phasecool = 0
        self.mcool = 0

        self.timeon = 0

        self.timeleft = 60 * 30
        self.nowtime = time.time()

        self.phase = 0
        self.period = [166, 152, 126, 100]  # Hard
        # self.period = [196, 182, 151, 120]  # Normal
        self.timenext = self.timeleft - self.period[0]
        self.timetogo = self.timeleft - self.timenext

        self.txt_a = 1
        self.tmpvar = 0

        self.label_now = tkinter.Label(root, text='현재 시간\n' + str(self.timeleft // 60) + ' : ' + str(self.timeleft % 60), fg="red", font=fnt)
        self.label_now.pack()

        self.label_next = tkinter.Label(root, text='다음 낫베기\n' + str(self.timenext // 60) + ' : ' + str(self.timenext % 60), fg="red", font=fnt)
        self.label_next.pack()

        self.label_left = tkinter.Label(root, text='남은 시간\n' + str(self.timetogo // 60) + ' : ' + str(self.timetogo % 60), fg="red", font=fnt)
        self.label_left.pack()

        self.btn_start = tkinter.Button(root, padx=5, pady=5, text='시작', command=self.com_btn_start)
        self.btn_start.pack()

        self.btn_reset = tkinter.Button(root, padx=5, pady=5, text='리셋', command=self.com_btn_reset)
        self.btn_reset.pack()

        self.btn_plus = tkinter.Button(root, padx=5, pady=5, text='1초 +', command=self.com_btn_plus)
        self.btn_plus.pack()
        self.btn_minus = tkinter.Button(root, padx=5, pady=5, text='1초 -', command=self.com_btn_minus)
        self.btn_minus.pack()

    def com_btn_start(self, *_):
        if self.timeon == 0:
            self.nowtime = time.time()
            self.timeon = 1

    def com_btn_reset(self, *_):
        if self.timeon == 1:
            self.timeon = 0
            self.timeleft = 60 * 30
            self.nowtime = time.time()
            self.phase = 1
            self.period = [166, 152, 126, 100]
            self.timenext = self.timeleft - self.period[0]
            self.timetogo = self.timeleft - self.timenext
            self.relabel()

    def com_btn_plus(self, *_):
        if self.timeon == 1:
            self.nowtime += 1

    def com_btn_minus(self, *_):
        if self.timeon == 1:
            self.nowtime -= 1

    def void(self):
        if self.timeon == 1:
            newtime = time.time()
            self.timeleft = 60 * 30 - int(newtime - self.nowtime)
            # self.timenext = self.timeleft - self.period[0]
            self.timetogo = self.timeleft - self.timenext
            self.relabel()

            self.phasecool += 1
            self.mcool += 1

            if self.timetogo == 60 and self.mcool >= 300:
                self.mcool = 0
                pygame.mixer.music.load('1mleft.mp3')
                pygame.mixer.music.play()

            # Check Phase
            position = win32gui.GetWindowRect(self.game_hwnd)
            screenshot1 = ImageGrab.grab(position)
            screenshot = np.array(screenshot1)
            img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

            color1 = img[33, 497 + 4]  # 477, 497
            color2 = img[33, 648 + 4]  # 628, 648
            color3 = img[253, 1100]
            color4 = img[208, 1100]

            if color3[0] <= 10 and color3[1] <= 10 and color3[2] >= 250 and color4[0] <= 10 and color4[1] <= 10 and color4[2] <= 10 and self.phasecool >= 300:
                # phase next
                self.phasecool = 0
                def is1p(a, b, c):
                    if 102 - 10 <= a <= 102 + 10 and 51 - 10 <= b <= 51 + 10 and 245 - 10 <= c <= 245 + 10:
                        return 1
                    return 0
                def is2p(a, b, c):
                    a0 = 165
                    b0 = 88
                    c0 = 245
                    if a0 - 10 <= a <= a0 + 10 and b0 - 10 <= b <= b0 + 10 and c0 - 10 <= c <= c0 + 10:
                        return 1
                    return 0
                def is3p(a, b, c):
                    a0 = 33
                    b0 = 212
                    c0 = 192
                    if a0 - 10 <= a <= a0 + 10 and b0 - 10 <= b <= b0 + 10 and c0 - 10 <= c <= c0 + 10:
                        return 1
                    return 0
                def is4p(a, b, c):
                    a0 = 15
                    b0 = 130
                    c0 = 95
                    if a0 - 10 <= a <= a0 + 10 and b0 - 10 <= b <= b0 + 10 and c0 - 10 <= c <= c0 + 10:
                        return 1
                    return 0
                def is5p(a, b, c):
                    a0 = 75
                    b0 = 65
                    c0 = 80
                    if a0 - 10 <= a <= a0 + 10 and b0 - 10 <= b <= b0 + 10 and c0 - 10 <= c <= c0 + 10:
                        return 1
                    return 0
                print(color1[0], color1[1], color1[2])
                print(color2[0], color2[1], color2[2])
                if is1p(color2[0], color2[1], color2[2]) or is2p(color2[0], color2[1], color2[2]):
                    # 150
                    self.timenext = self.timeleft - self.period[1]
                    self.phase = 1
                    print('Phase 1')
                elif is3p(color2[0], color2[1], color2[2]) or (is4p(color2[0], color2[1], color2[2]) and is3p(color1[0], color1[1], color1[2])):
                    # 125
                    self.timenext = self.timeleft - self.period[2]
                    self.phase = 2
                    print('Phase 2')
                elif is4p(color1[0], color1[1], color1[2]) or is5p(color1[0], color1[1], color1[2]):
                    # 100
                    self.timenext = self.timeleft - self.period[3]
                    self.phase = 3
                    print('Phase 3')
                else:
                    self.timenext = self.timeleft - self.period[self.phase]
                    print('Phase ?, ' + str(self.phase))

                # play sound
                snd1t = (self.timenext // 60) // 10
                snd2t = (self.timenext // 60) % 10
                snd3t = (self.timenext % 60) // 10
                snd4t = (self.timenext % 60) % 10
                pygame.mixer.music.load('nextpt.mp3')
                pygame.mixer.music.play()
                self.after(1230, self.sndp, snd1t)
                self.after(1230 + 600, self.sndp, snd2t)
                self.after(1230 + 1200, self.sndp, snd3t)
                self.after(1230 + 1800, self.sndp, snd4t)

        self.after(200, self.void)

    def relabel(self):
        self.label_now.config(text='현재 시간\n' + str(self.timeleft // 60) + ' : ' + str(self.timeleft % 60))
        self.label_next.config(text='다음 낫베기\n' + str(self.timenext // 60) + ' : ' + str(self.timenext % 60))
        self.label_left.config(text='남은 시간\n' + str(self.timetogo // 60) + ' : ' + str(self.timetogo % 60))

    def sndp(self, time):
        pygame.mixer.music.load('%d.mp3' % time)
        pygame.mixer.music.play()





root = tkinter.Tk()
root.geometry("180x330+4+4")
root.resizable(False, False)
app = Application(root)
app.void()

root.mainloop()
