# Bucket list /travel challenge sovellus


Sovelluksessa näkyy mantereet listattuna sivupalkissa. Etusivulle avautuu kuvaruutut haasteista: haasteen nimi (esim. "24 parasta kohdetta Portugalissa") ja mahdollisuus tykätä kohteesta, minkä jälkeen se näkyy käyttäjän profiilissa. Näkyy myös "suoritettu", minkä jälkeen käyttäjäprofiilissä näkyy esim. "Europa 6/24". Haasteita pystyy klikkaamaan auki minkä jälkeen voi lukea haastekuvauksen ja nähdä haasteen kuvan. Käyttäjä pystyy lisäämään sekä täydentämään haasteita. Jatkokehityksenä voisi olla mahdollisuus jakaa sovelluksessa näkyviä haasteita ja ehkä kategorisoida myös haasteet. Klikkaamalla haasteen auki voisi pystyä klikkaamaan jokaista haasteen sisältämää kohdetta erikseen suoritetuksi (näkyy käyttäjäprofiilissä klikkaamalla "vierailut") ja nähdä kartan (kartta sijainti mahdollisesti maksullinen myöhemmin). Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.


* Käyttäjä voi kirjautua sisään ja ulos ☑. Käyttäjä voi luoda käyttäjätunnuksen ☑. 
* Käyttäjä näkee mantereen (useita) ☑ → Haasteet kuvauksineen (useita haasteita) ☑  → Pysty avaamaan haasteen  ☑ ja kartan (Jatkokehitys)
* Käyttäjä voi lisätä haasteita lempilistalleen, merkitä suoritetuksi ☑ (Extra: jakaa sosiaalisessa mediassa) ja nähdä yhteenveton haasteista omalla sivulla ☑.
* Ylläpitäjä voi lisätä ja poistaa haasteita sekä määrittää haasteesta näytettävät tiedot. Ylläpitäjä voi tarvittaessa poistaa käyttäjän suorittaman haasteen.(Jatkokehitys)
* Käyttäjä voi luoda ☑ ja täydentää omia haasteita ☑.
* Käyttäjä voi etsiä kaikki haasteet, joiden kuvauksessa on annettu sana.
* Käyttäjä näkee ja pystyy suodattamaan haasteet aakkos-, suosikki-, ja kategoriajärjestyksessä.(Jatkokehitys)
* Ylläpitäjä voi luoda kategorioita, joihin haasteet voi luokitella. Haaste voi kuulua yhteen tai useampaan kategoriaan.(Jatkokehitys)

# Käynistysohjeet

1. Avaa terminaalissa kansio, johon haluat kloonata projektin ja käytä komentoa: 
	
	`git clone https://github.com/KetuKuu/stoha-harjoitustyo.git`

2. Siirry Challenge-app kansioon.

3. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
   
   `DATABASE_URL=<tietokannan-paikallinen-osoite>`

   `SECRET_KEY=<salainen-avain>`


4. Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
   
   **<p>$ python3 -m venv venv</p>**
   **<p>$ source venv/bin/activate</p>**
   **<p>$ pip install -r config/requirements.txt</p>**

5. Määritä vielä tietokannan skeema komennolla
   
   **<p>psql < config/schema.sql</p>**
  
6. Nyt voit käynnistää sovelluksen komennolla
  
   **$ flask run**

# Nykyinen tilanne

Sovellus on edistynyt toivotulla tavalla ja käyttäjä voi ottaa sovelluksen käyttöön.
Sovelluksen käynnistyessä avautuu etusivu, Frontpage: Login-linkistä pääsee kirjautumaan sovellukseen, jonka jälkeen käyttäjälle avautuvat yläpalkit Home, Mypages, Polls, kirjautuneen käyttäjän käyttäjätunnus ja Log Out.
Sivun keskiosassa näkyy yksi tyhjä haasteruutu haasteen lisäämistä varten ja lisätyt haasteet ilmestyvät staattisesti etusivulle haasteruutukkoon (cards). Käyttäjä pystyy lisäämään lisää kuvia ja kuvauksia klikkaamalla omia haasteita haasteruutukosta. Käyttäjä voi myös merkitä haasteita suoritetuiksi, jonka jälkeen yhteenveto näkyy Mypages-sivulla.
Lisäsin sovellukselle kyselysivun, jossa käyttäjät voivat esittää kysymyksiä ja nähdä toisten käyttäjien vastauksia.
Alkuperäinen suunnitelma poikkeaa sovelluksestasen verran että lempilista- ja etsi-toiminnot puuttuvat. Sen sijaan lisäsin kyselymahdollisuuden


