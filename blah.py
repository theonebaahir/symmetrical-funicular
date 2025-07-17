from abc import ABC, abstractmethod

class india():
    def capital(self):
        print('new delhi is the capital of india')
    def language(self):
        print('hindi is the most widely spoken language of india')
    def type(self):
        print('india is a developing country')


class usa():
    def capital(self):
        print('dc is the capital of india')
    def language(self):
        print('english is the most widely spoken language of india')
    def type(self):
        print('usa is a developing country')
objind = india()
objusa = usa()

for country in (objind,objusa ):
    country.capital()
    country.language()
    country.type()




        
