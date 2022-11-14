from mypandas.mpg import Mpg, mpg_menu, MPG_MENUS
def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')
if __name__ == '__main__':
    t = Mpg()
    while True:
        menu = my_menu(MPG_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                mpg_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")

