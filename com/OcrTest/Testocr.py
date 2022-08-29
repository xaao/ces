import easyocr

reader= easyocr.Reader(['en','ch_sim'],gpu=False)
reuslt=reader.readtext(r"./images/img.png")

NUMocr=reader.readtext(r"./images/7921.png", allowlist ='0123456789')
print(reuslt)
print(NUMocr)
print("------------")

for res in reuslt:
    print(res)