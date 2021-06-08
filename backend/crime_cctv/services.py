import pandas as pd
import xlwings as xw
from common.models import DataTransferObject


class Crime_service(object):
    ccm = DataTransferObject()

    def new_model(self, payload):
        this = self.ccm
        this.context = './data/'
        this.fname = payload

        df = pd.read_csv(this.context + payload + '.csv')
        return df