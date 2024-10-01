
# ############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

# ############################################
# İş Problemi
# ############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


# ############################################
# Veri Seti Hikayesi
# ############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

# ################ Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

# ################ Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
pd.set_option("display.max_rows", None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.width', 500)
df = pd.read_csv("persona.csv")
print(df.head())
print(df.shape)
print(df.info())

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
print(df["SOURCE"].nunique())
print(df["SOURCE"].value_counts())

# Soru 3:Kaç unique PRICE vardır?
print(df["PRICE"].nunique())

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
print(df["PRICE"].value_counts())

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
print(df["COUNTRY"].value_counts())
print(df.groupby("COUNTRY")["PRICE"].count())
print(df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="count"))

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
print(df.groupby("COUNTRY").agg({"PRICE": "sum"}))
print(df.groupby("COUNTRY")["PRICE"].sum())
print(df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="sum"))

# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?
print(df["SOURCE"].value_counts())

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
print(df.groupby("COUNTRY").agg({"PRICE": "mean"}))

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
print(df.groupby("SOURCE").agg({"PRICE": "mean"}))

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
print(df.groupby(by=["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"}))


#############################################
# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
print(df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head())

#############################################
# Görev 3:Çıktıyı PRICE’a göre sıralayınız.
# Önceki sorudaki çıktıyı daha iyi görebilmek için
# sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values(by="PRICE", ascending=False)
print(agg_df.head())


#############################################
# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
agg_df = agg_df.reset_index()
print(agg_df.head())

#############################################
# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz. Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
labels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=labels)
print(agg_df.head())

#############################################
# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve
# veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek
# customers_level_based değişkenini oluşturmanız gerekmektedir.

# # YÖNTEM 1
# # değişken isimleri:
# agg_df.columns
#
# # gözlem değerlerine nasıl erişiriz?
# for row in agg_df.values:
#     print(row)
#
# # COUNTRY, SOURCE, SEX ve age_cat değişkenlerinin DEĞERLERİNİ yan yana koymak ve alt tireyle birleştirmek istiyoruz.
# # Bunu list comprehension ile yapabiliriz.
# # Yukarıdaki döngüdeki gözlem değerlerinin bize lazım olanlarını seçecek şekilde işlemi gerçekletirelim:
# [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
#
# # Veri setine ekleyelim:
# agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
# agg_df.head()
#
# # Gereksiz değişkenleri çıkaralım:
# agg_df = agg_df[["customers_level_based", "PRICE"]]
# agg_df.head()
#
# for i in agg_df["customers_level_based"].values:
#     print(i.split("_"))
#
#
# # Amacımıza bir adım daha yaklaştık.
# # Burada ufak bir problem var. Birçok aynı segment olacak.
# # örneğin USA_ANDROID_MALE_0_18 segmentinden birçok sayıda olabilir.
# # kontrol edelim:
# agg_df["customers_level_based"].value_counts()
#
# # Bu sebeple segmentlere göre groupby yaptıktan sonra price ortalamalarını almalı ve segmentleri tekilleştirmeliyiz.
# agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
#
# # customers_level_based index'te yer almaktadır. Bunu değişkene çevirelim.
# agg_df = agg_df.reset_index()
# agg_df.head()
#
# # kontrol edelim. her bir persona'nın 1 tane olmasını bekleriz:
# agg_df["customers_level_based"].value_counts()
# print(agg_df.head())

# Effective method 1
agg_df["customers_level_based"] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'AGE_CAT']].agg(lambda x: '_'.join(x).upper(), axis=1)
print(agg_df[["customers_level_based", "PRICE"]].head())
# Effective method 2
# agg_df["customers_level_based"] = ['_'.join(i).upper() for i in agg_df.drop(["AGE", "PRICE"], axis=1).values]
# print(agg_df[["customers_level_based", "PRICE"]].head())


#############################################
# Görev 7:Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
print(agg_df.head(30))
print(agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]}))


#############################################
# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?


new_user = "TUR_ANDROID_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user])

new_user1 = "FRA_IOS_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user1])

# new_user = "BRA_IOS_FEMALE_41_66"
# print(agg_df[agg_df["customers_level_based"] == new_user])

