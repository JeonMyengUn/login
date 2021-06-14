from tkinter import *
import pandas as pd
import os   #폴더를 만들고 삭제...현재 폴더 위치.

class Windows:

    def __init__(self, window):
        self.window = window
        self.window.title = "My Dictionary"
        self.dat = pd.read_csv("국토교통부_항공안전데이터_표준분류.csv", encoding="CP949", error_bad_lines=False)
        # GUI 구성
        # 02 텍스트 입력이 가능한 상자(Entry)
        self.entry = Entry(window, width=15, bg="light yellow")
        self.entry.grid(row=1, column=0, sticky=W)  # sticky 위치 w동쪽  좌, 우
        # 02 텍스트 입력이 가능한 상자(Entry)
        self.Destroy_entry = Entry(window, width=15, bg="Gray")
        self.Destroy_entry.grid(row=1, column=3, sticky=W)  # sticky 위치 w동쪽  좌, 우
        # 04 설명 레이블 - 의미
        self.label2 = Label(window, text="\n입력한 단어의 정의")
        self.label2.grid(row=3, column=0, sticky=W)
        self.create_label = Label(window, text="\n추가 약어")
        self.create_label.grid(row=0, column=4, sticky=W)
        self.create_entry = Entry(window, width=15, bg="light yellow")
        self.create_entry.grid(row=1, column=4, sticky=W)  # sticky 위치 w동쪽  좌, 우
        self.create_label = Label(window, text="\n추가 용어")
        self.create_label.grid(row=2, column=4, sticky=W)
        self.create_entry2 = Entry(window, width=15, bg="light yellow")
        self.create_entry2.grid(row=3, column=4, sticky=W)  # sticky 위치 w동쪽  좌, 우
        # 01 입력 상자 설명 레이블
        self.label = Label(window, text="약어 입력")
        self.label.grid(row=0, column=0, sticky=W)  # 장착 시킴
        # 02 텍스트 입력이 가능한 상자(Entry)
        self.entry = Entry(window, width=15, bg="light yellow")
        self.entry.grid(row=1, column=0, sticky=W)  # sticky 위치 w동쪽  좌, 우
        # 03 제출버튼
        self.button = Button(window, width=5, text="제출", command=lambda : self.click(self.entry))
        self.button.grid(row=2, column=0, sticky=W)
        # 03 추가
        self.button = Button(window, width=17, text="추가", command=lambda : self.create_dat(self.create_entry, self.create_entry2))
        self.button.grid(row=4, column=4, sticky=SW)
        # 03 삭제
        self.button = Button(window, width=5, text="삭제", command=lambda : self.del_dat(self.Destroy_entry))
        self.button.grid(row=2, column=3, sticky=W)
        # 05 텍스트 박스 입력 상자
        # columnspan=2 는 (4,0)~(4,1) 위치까지 분포
        self.output = Text(window, width=20, height=6, wrap=WORD, background="light yellow")  # wrap
        self.output.grid(row=4, column=0, columnspan=2, sticky=S)

    def click(self, entry):
        word = self.entry.get() #아래 엔트리 상자의 내용을 text 넣는다
        # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
        # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 쓴다.
        self.output.delete(0.0, END)  # 텍스트 박스 내용을 지운다.
        try:
            def_word = self.dat.loc[self.dat["약어"] == word, '정의'].values[0]
        except:
            def_word = "단어를 뜻을 찾을 수 없음."

        self.output.insert(END, def_word)

    def del_dat(self, entry):
        word = self.Destroy_entry.get()
        self.output.delete(0.0, END)
        try:
            df = self.dat.loc[self.dat["약어"] == word].index
            self.dat.drop(df, inplace=True)
            print(self.dat)
            message = "삭제완료"
        except:
            message = "해당 약어가 데이터에 없습니다."

        self.output.insert(END, message)

    def create_dat(self, entry, entry2):


        self.output.delete(0.0, END)
        def_word = "create command"
        self.output.insert(END, def_word)

if __name__ == "__main__":
    window=Tk()
    Windows(window)
    window.mainloop()
