from services import Crime_service
from common.models import DataTransferObject


class Crime_view(object):

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Housing 의 type \n {type(this)} ')
        print(f'2. Housing 의 column \n {this.columns} ')
        print(f'3. Housing 의 상위 1개 행\n {this.head()} ')
        print(f'4. Housing 의 null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)



    @staticmethod
    def main():
        util = Crime_service()
        dto = DataTransferObject()
        while 1:
            menu = input('0-Exit 1- 데이터프레임생성 \n')
            if menu == '0':
                break
            elif menu == '1':
                dto.dframe = util.new_model('housing')
                Crime_view.print_this(dto.dframe)
            else:
                continue


Crime_view.main()