from menu import show_menu
import os

def main():
    while True:
        show_menu()
        s = input("請選擇：")
        # 運行 crapy crawl cnyesSpider 
        if s == '1':
            os.chdir('./Cnyes/Cnyes/spiders/')
            os.system('scrapy crawl cnyesSpider')
            os.chdir('../../..')
        # 運行 scrapy crawl taiwanindexSpider
        elif s == '2':
            os.chdir('./Taiwanindex/Taiwanindex/spiders/')
            os.system('scrapy crawl taiwanindexSpider')
            os.chdir('../../..')      
        # 運行 python3 kdj.py
        elif s == '3':
            os.system('python3 kdj.py')
        # 運行 python3 ebb.py
        elif s == '4':
            os.system('python3 ebb.py')
        # 運行 python3 poly.py
        elif s == '5':
            os.system('python3 poly.py')
        # 結束執行，直接退出
        elif s == 'q':
            return
        # 請重新輸入
        else:
            print("請重新輸入") 

main()