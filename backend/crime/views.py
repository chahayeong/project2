import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
from crime.services import CrimeService


class Crime_API(object):

    @staticmethod
    def main():
        crimeService = CrimeService()
        while 1:
            menu = input('0-Exit 1-서울CCTY DF 2-서울범죄 DF 3-경찰서위치 DF 4-실업률 DF 5-엑셀POP \n')
            if menu == '0':
                break
            elif menu == '1':
                crimeService.csv({'context':'./data/', 'fname':'cctv_in_seoul'})
            elif menu == '2':
                crimeService.csv({'context': './data/', 'fname': 'crime_in_seoul'})
            elif menu == '3':
                crimeService.csv({'context': './data/', 'fname': 'police_position'})
            elif menu == '4':
                crimeService.csv({'context':'./data/', 'fname':'us_unemployment'})
            elif menu == '5':
                crimeService.xls({'context': './data/', 'fname': 'pop_in_seoul'})
            else:
                continue


Crime_API.main()
