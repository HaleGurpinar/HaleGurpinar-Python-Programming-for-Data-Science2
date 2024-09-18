# ##############################################
# List Comprehension ve Pandas Exercises
# #############################################

# ##############################################
# 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.
# ##############################################

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
print(df.columns)
print(df.info())
print(["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns])


# ##############################################
# 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.
# ##############################################
print([col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns])

# ##############################################
# 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ##############################################
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df.head())

# ##############################################
# Pandas 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
# ##############################################
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("Titanic")
print(df.head())
print(df.shape)

# ##############################################
# Pandas 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
# ##############################################
print(df["sex"].value_counts())

# ##############################################
# Pandas 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
# ##############################################
print(df.nunique())

# ##############################################
# Pandas 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
# ##############################################
print(df["pclass"].unique())

# ##############################################
# Pandas 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
# ##############################################
print(df[["pclass", "parch"]].nunique())

# ##############################################
# Pandas 6: embarked değişkeninin tipini kontrol ediniz.
# Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
# ##############################################
print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
print(df["embarked"].dtype)

# ##############################################
# Pandas 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
# ##############################################
print(df[df["embarked"] == "C"].head(10))

# ##############################################
# Pandas 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
# ##############################################
print(df[df["embarked"] != "S"].head(10))

# ##############################################
# Pandas 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
# ##############################################
print(df[(df["age"] < 30) & (df["sex"] == "female")].head())

# ##############################################
# Pandas 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
# ##############################################
print(df[(df["fare"] > 500) | (df["age"] > 70)].head())

# ##############################################
# Pandas 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
# ##############################################
# print(df.isnull.sum())
print(df.eq('').sum() + df.isnull().sum())

# ##############################################
# Pandas 12: who değişkenini dataframe’den çıkarınız.
# ##############################################
df.drop(["who"], axis=1, inplace=True)
print(df.columns)

# ##############################################
# Pandas 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
# ##############################################

type(df["deck"].mode())
print(df["deck"].mode()[0])

# df["deck"].fillna(df["deck"].mode()[0], inplace=True)

# when doing 'df[col].method(value, inplace=True)',
# try using 'df.method({col: value}, inplace=True)' or
# df[col] = df[col].method(value) instead,
# to perform the operation inplace on the original object.
print(df.head(15))

df.fillna({"deck": df["deck"].mode()[0]}, inplace=True)

print(df["deck"].isnull().sum())
print(df.head(15))

# ##############################################
# Pandas 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
# ##############################################
print(df["age"].median())
df.fillna({"age": df["age"].median()}, inplace=True)
print(df["age"].isnull().sum())
print(df.head(20))

# ##############################################
# Pandas 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
# ##############################################
print(df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]}))

# ##############################################
# Pandas 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde
#  age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
# ##############################################


def age_30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age_30(x))

# ##############################################
# Pandas 17: Seaborn kütüphanesi içerisinden tips veri setini tanımlayınız.
# ##############################################
import seaborn as sns
df = sns.load_dataset("tips")
print(df.head(10))

# ##############################################
# Pandas 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin
# toplamını, min, max ve ortalamasını bulunuz.
# ##############################################

print(df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]}))

# ##############################################
# Pandas 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
# ##############################################
print(df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]}))

# ##############################################
# Pandas 20: Lunch zamanına ve kadın müşterilere ait total_bill ve
# tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
# ##############################################
print(df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                          "tip": ["sum", "min", "max", "mean"]}))

# ##############################################
# Pandas 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
# ##############################################
print(df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean())

# ##############################################
# Pandas 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
# ##############################################
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
print(df.head())


# ##############################################
# Pandas 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
# ##############################################
new_df = df.sort_values(by="total_bill_tip_sum", ascending=False).head(30)
print(new_df.shape)

