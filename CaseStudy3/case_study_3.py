# ##############################################
# Gezinomi Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
# (Calculating Potential Customer Return with Gezinomi Rule Based Classification)
# #############################################


# ##############################################
# 1: Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz..
# ##############################################
import pandas as pd

df = pd.read_excel(r'miuul_gezinomi.xlsx', engine='openpyxl')
pd.set_option('display.max_columns', None)  # Get rid of 3 dots(...). Generally not prefer in dataset has many columns.
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(df.head())
print(df.shape)
print(df.info())

# ##############################################
# 1: Soru 2:Kaç unique şehir vardır? Frekansları nedir?
# ##############################################
print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# ##############################################
# 1: Soru 3:Kaç unique Concept vardır?
# ##############################################
print(df["ConceptName"].nunique())

# ##############################################
# 1: Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
# ##############################################
print(df["ConceptName"].value_counts())

# ##############################################
# 1: Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
# ##############################################
print(df.groupby("SaleCityName").agg({"Price": "sum"}))

# ##############################################
# 1: Soru6: Concept türlerine göre göre ne kadar kazanılmış?
# ##############################################
print(df.groupby("ConceptName").agg({"Price": "sum"}))

# ##############################################
# 1: Soru7: Şehirlere göre PRICE ortalamaları nedir?
# ##############################################
print(df.groupby("SaleCityName").agg({"Price": "mean"}))
# print(df.groupby(by=['SaleCityName']).agg({"Price": "mean"}))

# ##############################################
# 1: Soru 8: Conceptlere göre PRICE ortalamaları nedir?
# ##############################################
print(df.groupby("ConceptName").agg({"Price": "mean"}))

# ##############################################
# 1: Soru 9: Şehir-Concept kırılımında PRICE ortalamalarınedir?
# ##############################################
print(df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"}))




