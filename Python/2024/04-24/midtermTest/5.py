def id_check(user_id: str) -> None:
    Region = {'A': '台北市', 'B': '台中市', 'C': '基隆市', 'D': '台南市', 'E': '高雄市',
              'F': '台北縣', 'G': '宜蘭縣', 'H': '桃園縣', 'I': '嘉義市', 'J': '新竹縣',
              'K': '苗栗縣', 'L': '台中縣', 'M': '南投縣', 'N': '彰化縣', 'O': '新竹市',
              'P': '雲林縣', 'Q': '嘉義縣', 'R': '台南縣', 'S': '高雄縣', 'T': '屏東縣',
              'U': '花蓮縣', 'V': '台東縣', 'W': '金門縣', 'X': '澎湖縣', 'Y': '陽明山',
              'Z': '連江縣'}
    while True:
        ID = user_id.upper()
        if len(ID) != 10:
            print("錯誤，身份證字號須為10碼")
            return
        elif not ID[0].isalpha():
            print("錯誤，第一碼須為英文字母")
            return
        elif not ID[1:].isdigit():
            print("錯誤，後九碼須為數字")
            return
        elif ID[1] < '1' or ID[1] > '2':
            print("錯誤，第一個數字須為1或2")
            return
        else:
            X = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
                 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
                 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35,
                 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
                 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31,
                 'Z': 33}
            num = X[ID[0]] // 10 + (X[ID[0]] % 10) * 9
            for i in range(2, 10):
                num += int(ID[-i]) * (i - 1)
            ans = 10 - num % 10
            if ans == int(ID[-1]):
                if ID[1] == '1':
                    sex = "男生"
                elif ID[1] == '2':
                    sex = "女生"
                print(ID + " 是正確的身分證字號", Region[ID[0]], sex)
                break
            else:
                print(ID + " 不是正確的身分證字號")
                break


def main() -> None:
    id_check(input("請輸入身分證字號: "))


if __name__ == '__main__':
    main()
