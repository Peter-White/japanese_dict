from base_chars.models import Hiragana, Katakana

def getAllGana():
    return Hiragana.objects.all()

def getGanaId(id):
    return Hiragana.objects.get(id=id)

def getGanaSymbol(sym):
    return Hiragana.objects.get(symbol=sym)

def createGana(sym, rom):
    Hiragana.objects.create(sym, rom)

def updateGanaSymbol(id, sym):
    gana = Hiragana.objects.get(id=id)
    gana.symbol = sym

def updateGanaRom(id, rom):
    gana = Hiragana.objects.get(id=id)
    gana.romaji = rom

def deleteGana(id):
    gana = Hiragana.objects.get(id=id)
    gana.delete()

def getAllKana():
    return Katakana.objects.all()

def getKanaId():
    return Katakana.objects.get(id=id)

def getKanaSymbol(sym):
    return Katakana.objects.get(symbol=sym)

def createKana(sym, rom):
    Katakana.objects.create(sym, rom)

def updateKanaSymbol(id, sym):
    kana = Katakana.objects.get(id=id)
    kana.symbol = sym

def updateGanaRom(id, rom):
    kana = Katakana.objects.get(id=id)
    kana.romaji = rom

def deleteGana(id):
    kana = Katakana.objects.get(id=id)
    kana.delete()