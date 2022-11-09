from scrapper.services import BugsMusic, MelonMusic


class ScrapController:
    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)

    @staticmethod
    def menu_2(arg):
        MelonMusic(arg)