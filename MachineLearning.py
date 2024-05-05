from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import DataBase as db
class MakineOgrenimi:

    def __init__(self, veritabani):
        self.veritabani = veritabani

    def verileri_getir(self):
        veriler = self.veritabani.veri_goster()
        X = []
        y = []
        for veri in veriler:
            X.append(veri[1:-2])  # Zaman ve id sütunlarını almayın
            y.append(veri[-1])    # Su vanası sütununu hedef değişken olarak alın
        print("X:",X)
        return X, y

    def model_olustur(self):
        X, y = self.verileri_getir()

        # Verileri eğitim ve test setlerine bölelim
        X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Verileri ölçeklendirme
        scaler = StandardScaler()
        X_egitim = scaler.fit_transform(X_egitim)
        X_test = scaler.transform(X_test)

        # Model oluşturma
        model = LogisticRegression()
        model.fit(X_egitim, y_egitim)

        # Modelin performansını değerlendirme
        tahminler = model.predict(X_test)
        dogruluk = accuracy_score(y_test, tahminler)
        print("Modelin doğruluğu:", dogruluk)

if __name__ == "__main__":
    # Veritabanından verileri çekerek makine öğrenimi modelini oluşturma
    sulama_veritabani = db.SulamaVeritabani("sulama_veritabani.db")
    makine_ogrenimi = MakineOgrenimi(sulama_veritabani)
    makine_ogrenimi.verileri_getir()
    makine_ogrenimi.model_olustur()
