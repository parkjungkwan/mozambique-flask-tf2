# from ml.stroke import STROKE_MENUS, stroke_menu
# from ml.stroke import StrokeService
from ml.crime import Crime, CRIME_MENUS, crime_menu
from ml.oklahoma import OKLAHOMA_MENUS, oklahoma_menu
from ml.oklahoma import OklahomaService
def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Crime()
    while True:
        menu = my_menu(CRIME_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            crime_menu[menu](t)
            '''
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")
            '''