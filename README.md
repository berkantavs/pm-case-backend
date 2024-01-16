# pm-case-backend

Bu proje [Django](https://www.djangoproject.com/) kullanılarak geliştirilmiş bir web uygulamasıdır.

## Başlarken

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

Projeyi çalıştırmak için bilgisayarınızda [Python](https://www.python.org/) ve [Django](https://www.djangoproject.com/) yüklü olmalıdır.

### Kurulum

   git clone https://github.com/berkantavs/pm-case-backend.git

   cd pm-case-backend

   python -m venv venv

   venv\Scripts\activate

   pip install -r requirements.txt

   ** Mysql Workbench üzerinden "project-management" adlı database oluşturulmalı.

   ** Database bilgileri SETTINGS.PY içerisindeki DATABASES kısmına girilmeli.

   python manage.py migrate

   python manage.py makemigrations

   ** makemigrations işleminden sonra gelen seçenekten 2. seçilip devam edilebilir.

   python manage.py runserver

   ## KULLANIM

   ** Projenin çalıştığını kontrol etmek için;

   http://127.0.0.1:8000/units adresini kontrol ediniz.

   ** Proje başarılı bir şekilde çalışıyor ise, veri girişi için ilk aşamada 'add_unit' API'ını kullanarak birim oluşturun.

   http://127.0.0.1:8000/add_unit (POST)

   BODY
   
   {
  "birim_ad": "Birim1",
  "ust_birim_id": null,
  "user_type": null
   }

   ** Biriminiz oluştuktan sonra 'register' API'ı ile bu birime ait bir kullanıcı kayıt ediniz.

   http://127.0.0.1:8000/register (POST)

   BODY

   {
  "kullanici_ad": "JohnDoe",
  "email": "johndoe@example.com",
  "sifre": "1234",
  "ilce": "ExampleDistrict",
  "mahalle": "ExampleNeighborhood",
  "user_type": "admin",
  "birim":1
   }
