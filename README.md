# Flask RESTPlusAPI

## What is the purpose of this repo?

It is a simple Flask RESTful web service which is builded with [RESTPlus extension](https://flask-restplus.readthedocs.io/en/stable/). So, **app.py** file can be used as a template to create a RESTful API. Here, also, use of this extension and building a RESTful web service from scratch is explained in Turkish. ![Turkish](https://image.flaticon.com/icons/svg/197/197518.svg =20x20) 
  

## ![English](https://image.flaticon.com/icons/svg/1377/1377975.svg =20x20) Requirements, Installation and Usage 
- Install the required packages if you not already:
` pip install Flask `
` pip install flask-restplus`
- Download the "**app.py**" file or clone the repository via Git:
`git clone https://github.com/furkanmtorun/Flask-RESTPlusAPI.git` 
- Open your terminal and type following command:
`python app.py`
- It's ready to use on `http://127.0.0.1:5000/api`
> In the process of development, I have used Python 3. If you use both Python 2 and Python 3, specify your command as "**pip3**" and "**python3**" while installing the packages and running.

## Screenshots
![Page](https://user-images.githubusercontent.com/49681382/66161269-968cab80-e634-11e9-880f-151b708df6de.png)

![Argument parsing](https://user-images.githubusercontent.com/49681382/66161377-d358a280-e634-11e9-9afc-750b7b47f2e5.png)
![Get](https://user-images.githubusercontent.com/49681382/66161460-ff742380-e634-11e9-899b-8fffd70e3ea9.png)

# :hash: Türkçe Kılavuz / Doküman
- **İçerik/Başlıklar:**
	 - :hash:Flask Nedir, RESTFul API Nedir?
	 - :hash:Flask Kurulumu ve "Merhaba Flask!"
	 - :hash:RESTPlus eklentisinin kullanımı
	 - :hash:Kaynaklar / Referanslar

*****

### :hash: Flask nedir, RESTFul API Nedir?
**Flask nedir?**
[Flask](https://palletsprojects.com/p/flask/) web uygulamaları geliştirmenize olanak sağlayan Python temelli bir *microframework*tür. Ölçeklenebilir ve sürdürelebilir web uygulamlarını oluşturmaya fırsat vermesi ve çeşitli paket/modüllerini barındıran bir framework olması ile birçok kurum ve kuruluş tarafından kullanılmaktadır.  Kurum ve kuruluşların listesi için [bu](https://stackshare.io/flask) ve [şu](https://github.com/rochacbruno/flask-powered) adresi ziyaret edebilirsiniz. 👍 🙏

**RESTFul API nedir?**
REST (REpresentational State Transfer) (*Temsili Durum Transferi*), HTTP protokolü sayesinde  istemci ve sunucu arasında JSON,XML, HTML, TEXT gibi pek çok formatta veri formatı ile uygulamaların haberleşmesini sağlar. [\[1\]](https://ceaksan.com/tr/rest-soap-api-nedir/), [\[2\]](https://denizirgin.com/rest-ve-restful-web-servis-kavram%C4%B1-30bc4400b9e0) REST standartlarına uygun yazılan web servislerine RESTful servisler denir. [\[1\]](https://ceaksan.com/tr/rest-soap-api-nedir/), [\[2\]](https://denizirgin.com/rest-ve-restful-web-servis-kavram%C4%B1-30bc4400b9e0) 

### :hash: Flask Kurulumu ve "Merhaba Flask!"

**Flask'ın *pip* üzerinden kurulumu için:**
`pip install Flask`

**İlk Flask uygulamamız: "Merhaba Flask!"**
Python (.py) uzantılı dosyamızı oluşturduktan hemen sonra Flask kütüphanesini projemize dahil edelim:
`from flask import Flask`

Hemen sonrasında `app = Flask(__name__` ile Flask objemizi `__name__` değişkenin ile beraber oluşturuyor ve ardından bir if koşulu ile mevcut dosyamız doğrudan mı çalıştırılmış yoksa modül olarak bir başka yerden mi çalıştırılmış kontrol ediyoruz. Oluşturduğumuz dosya doğrudan çalışıtırılması durumunda `__main__` parametresini alacak ve Flask uygulamamızı `debug=True` değişkeni sayesinde hata ayıklamayı aktif hale getirmiş olarak çalıştıracağız.
````
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
````

Şimdi ise hemen basit bir sayfa hazırlayalım. Bu noktada Flask ile statik ve dinamik bağlatıların oluşturulumasının çok kolay olduğunu not etmekte fayda var:
````
@app.route("/")
def ana_sayfa():
    return "Merhaba Flask!"
````
Buradaki kod bloğunda bulunan `@app.route()` ile ilk sayfamızı `"/"` dizininde oluşturmayı başardık. Sonrasında bir fonksiyon tanımlayarak, ekrana bir yazıyı basmasını sağladık. 
Son olarak dosyanın bulunduğu dizinde komut istemcisinden `python app.py` komutunu verelim. 
**Tebrikler!** `127.0.0.1:5000` sayfasından ilk Flask web sayfanıza ulaşabilirsiniz!

### :hash: RESTPlus eklentisinin kullanımı
Eklentiyi yüklemek adına `pip install flask-restplus`  komutunu çalıştırabilirsiniz.
Sonrasında eklentiyi (app'i tanımlamak adına **Api**'ı, bir çok sınıfta parametre olarak alınan **Resource**'u) projemize çağıralım:
 `from flask_restplus import Api, Resource`

Şimdi ise uygulamamızı `api = Api(app)` ve onun temel özelliklerini *`(version, title, description)`* tanımlayalım:
`api = Api(app, version="0.1", title="People API with Flask-RESTPlus", description="A quite simple API to working with personal data")`
![Api bilgileri](https://user-images.githubusercontent.com/49681382/66167962-77961580-e644-11e9-88aa-c6db4c348c04.png)


Hemen sonrasında *`"peopleCollection_api"`* olarak bir isim alanı *`(namespace)`* tanımlayalım:
 
`peopleCollection_api = api.namespace("peopleCollection", description="People Collection Operations")`

> Burada not edilmesi gereken nokta, oluşturulan her namespace Swagger arayüzünde birer başlık olarak gözükecektir. (Ekran görüntüleri *"Screenshots"* başlığı altındaki ilk görselden anlaşıldığı üzere bu örnek RESTFul servisinde 3 namespace tanımlandı.) Ek olarak, bu namespace için belirlenen URL'de şu şekildedir:  **`127.0.0.1:5000/peopleCollection/`**

Son olarak, oluşturduğumuz namespace'ler üzerinden tıpkı normal sayfaları hazırlar gibi route'ları 
belirteceğiz: `peopleCollection_api.route("/")`

Daha sonrasında bir sınıf oluşturup, ilk GET çağrımızı peopleList adındaki basit bir sözlük (dictionary)'ü çıktı veren bir fonksiyon ile hazırlayacağız:

    class PeopleCollection(Resource): 
        def get(self): 
            return peopleList

Yapılan tüm bu çalışmayı denemek için hemen **`127.0.0.1:5000`** 'e bakalım: **Tebrikler!** 
![İlk API](https://user-images.githubusercontent.com/49681382/66167270-53393980-e642-11e9-82dd-87d4259d989e.png)

**Model tanımlamak**
Modeller, belirli bir format çerçevesinde (örneğin JSON) veri yollamak ya da çağırmak için kullanılmaktadır. Şimdi `people` isimli modeli `people_model` 'a tanımlayalım:

Tabii ki bunun için ilgili veri türlerini tanımlamak adına  `fields`'ı da projemize dahil etmemiz gerekiyor:
 `from flask_restplus import Api, Resource, fields`

````
people_model = api.model("people", 
	{
		"id": fields.Integer(description="ID Number", example=123456798, readonly=True),
		"name": fields.String(description="Full name", example="Richard Hendricks", required=True, min=5),
		"email": fields.String(description="Email Adress", example="richardhendricks@piedpier.com", required=True, min=10),
		"github": fields.String(description="Github username", example="richardhendricks"),
		"twitter": fields.String(description="Twitter username", example="richardhendricks"),
		"country": fields.String(description="Country", example="USA")
	}
)
````
Modelimiz, ana sayfada artık bu şekilde gözükmekte:
![Model](https://user-images.githubusercontent.com/49681382/66168919-4ec34f80-e647-11e9-853b-2e223204161d.png)



Şimdi ise `PeopleCollection` isimli *(daha önce içerisine `get` fonksiyonunu tanımladığımız)* sınıfımıza post metodunu içeren fonksiyonunu hazırlayalım ve bu modeli de entegre edelim:

````
@peopleCollection_api.response(200, "Success")
@peopleCollection_api.response(400, "Bad Request or Invalid Argument")
@peopleCollection_api.expect(people_model)
def  post(self):
	new_person = api.payload
	new_person["id"] =  max([temp_id["id"] for temp_id in peopleList]) +  1
	peopleList.append(new_person)
	return new_person
```` 

Burada ilk satırdaki komut ile 200 nolu [HTTP Status Code (HTTP Durum Kodları)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) için bir tanımlama yaptık.  
![HTTP Status Kodları](https://user-images.githubusercontent.com/49681382/66168954-6b5f8780-e647-11e9-9e1f-bcfa9563a3ea.png)


Sonrasında ise yukarıda tanımladığımız `"people"` isimli modelimizi `post` fonksiyonumuz için tanıttık. 
Bu fonksiyonda ise daha önce tanımladığımız sözlüğe (dictionary) gönderilen veri girişinin yapılmasını sağladık.

Bu arada HTTP isteklerini de kısa özetini de ekleyelim: 

1.  **GET:**  Veri görüntüler/listeler
2.  **POST:**  Yeni veri ekler/oluşturur
3.  **PUT:**  Var olan bir veriyi günceller/üzerine yeni veri ekler
4.  **DELETE:**  Veri siler
5.  **PATCH:**  Verinin bölümünü günceller
6.  **OPTIONS:**  Kabul edilen istekler konusunda bilgi iletir

### :hash: Kaynaklar/Referanslar:
* Yazı dizini içinde belirtilmeyen kaynaklar ve detaylı okumaları içeren bağlantıların listesi:
* [https://flask-restplus.readthedocs.io/en/stable/](https://flask-restplus.readthedocs.io/en/stable/)
* [https://www.youtube.com/watch?v=OTWs0wPHU-g](https://www.youtube.com/watch?v=OTWs0wPHU-g)
* [https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f](https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f)


  
