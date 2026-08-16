"""
==============================================================================
EMLAK SEKTÖRÜ TECRÜBESİNE DAYALI EV FİYATI TAHMİN MODELİ
==============================================================================
Amaç: 
    Metrekare, asansör ve otopark durumlarına bakarak Çoklu Doğrusal Regresyon
"""
EMLAK SEKTÖRÜ TECRÜBESİNE DAYALI EV FİYATI TAHMİN MODELİ
Amaç: 
    Metrekare, asansör ve otopark durumlarına bakarak Çoklu Doğrusal Regresyon
    (Multiple Linear Regression) algoritması ile ev fiyatlarını tahmin etmek.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 1. Sentetik Veri Setinin Oluşturulması
np.random.seed(42)
n_ev = 100

metrekare = np.random.randint(50, 200, n_ev)
asansor_var_mi = np.random.choice([0, 1], n_ev)
otopark_var_mi = np.random.choice([0, 1], n_ev)

# Sektörel mantığa göre fiyat hesaplama formülü
fiyat = (metrekare * 20) + (asansor_var_mi * 150) + (otopark_var_mi * 250) + np.random.randint(-50, 50, n_ev)

df_emlak = pd.DataFrame({
    "Metrekare": metrekare,
    "Asansor_Var_Mi": asansor_var_mi,
    "Otopark_Var_Mi": otopark_var_mi,
    "Ev_Fiyati_TL": fiyat * 1000
})

# 2. Veri Bölme (Train-Test Split)
X = df_emlak[["Metrekare", "Asansor_Var_Mi", "Otopark_Var_Mi"]]
y = df_emlak["Ev_Fiyati_TL"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Eğitimi (Çoklu Doğrusal Regresyon)
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Tahmin ve Metrikler
tahminler = model.predict(X_test)
print(f"Model Başarı Skoru (R²): {r2_score(y_test, tahminler):.4f}")

# 5. Grafik Çizimi ve Kaydetme
plt.figure(figsize=(7, 4))
plt.scatter(y_test, tahminler, color="blue", alpha=0.7, edgecolors="black", s=80)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="--", linewidth=2)
plt.title("Emlak Yapay Zekası: Gerçek Fiyat vs Tahmin Fiyatı")
plt.xlabel("Gerçek Ev Fiyatları (₺)")
plt.ylabel("Yapay Zekanın Tahmin Ettiği Fiyatlar (₺)")
plt.tight_layout()
plt.savefig("tahmin_basarisi.png") # Grafiği GitHub klasörüne kaydeder
plt.show()
