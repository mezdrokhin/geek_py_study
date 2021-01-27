class Data:
    @classmethod
    def makeint(cls, data):
        r=data.split('-')
        rint=[int(s) for s in r]
        Data.checknumber(rint)
        return rint
    @staticmethod
    def checknumber(data2):
        if data2[0]<1 or data2[0]>31:
            print('Проверьте день')
        if data2[1]<1 or data2[1]>12:
            print('Проверьте месяц')
        if data2[2]<0 or data2[2]>9999:
            print('Проверьте год')

print(Data.makeint('11-32-2020'))