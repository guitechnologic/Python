from translate import Translator
#   pip install translate

s = Translator (from_lang="english",
    to_lang = "Spanish")
res = s.translate("hello guys")
print(res)