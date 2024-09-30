# ##############################################
# Gezinomi Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
# (Calculating Potential Customer Return with Gezinomi Rule Based Classification)
# #############################################


# ##############################################
# 1: Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz..
# ##############################################
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
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


# ##############################################
# 2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.
# SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# Aralıkları ikna edici şekilde oluşturunuz. Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
# Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz.
# ##############################################
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuter", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)


# ##############################################
# 3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
# Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında
# ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz ?
# ##############################################
print(df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]}))
print(df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]}))
print(df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]}))

# ##############################################
# 4:  City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
# sort_values metodunu kullanınız. Elde ettiğiniz çıktıyı agg_df olarak kaydediniz.
# ##############################################

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
print(agg_df.head(20))


# ##############################################
# 5:  Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz
# ##############################################
agg_df.reset_index(inplace=True)
print(agg_df.head())


# ##############################################
# 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: sales_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir
# ##############################################