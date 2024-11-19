class india():
    def type(self):
        print("India is a developing country")
    def capital(self):
        print("Delhi is the capital of india")
    def language(self):
        print("Hindi is the main language")
class usa():
    def type(self):
        print("Usa is a developed country")
    def language(self):
        print("english is the most widely spoken language")
    def capital(self):
        print("Washington D.C. is the capital of USA")
objindia=india()
objusa=usa()
for country in (objindia,objusa):
    country.capital()
    country.language()
    country.type()