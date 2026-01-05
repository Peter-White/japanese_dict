from base_chars.models import Hiragana, Katakana

def getAllGana():
    return Hiragana.objects.all()

def getGanaId(id):
    return Hiragana.objects.get(id=id)

def getGanaSymbol(sym):
    return Hiragana.objects.get(symbol=sym)

def getGanaGroup(group):
    return Hiragana.objects.all().filter(group_num=group)

def getAllKana():
    return Katakana.objects.all()

def getKanaId():
    return Katakana.objects.get(id=id)

def getKanaSymbol(sym):
    return Katakana.objects.get(symbol=sym)

def getKanaGroup(group):
    return Katakana.objects.all().filter(group_num=group)