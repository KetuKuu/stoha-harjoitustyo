# Bucket list /travel challenge sovellus


Sovelluksessa näkyy mantereet listattuna sivupalkissa. Jokaisen mantereen alla avautuu etusivulle "sort"-toiminto hyväksyvä kuvaruutu haasteista: haasteen nimi (esim. "24 parasta kohdetta Portugalissa") ja mahdollisuus tykätä kohteesta, minkä jälkeen se näkyy käyttäjän profiilissa. Näkyy myös "suoritettu", minkä jälkeen käyttäjäprofiilissä näkyy prosentti esim. "Europa 6/24 (24%)". Lisäksi voisi olla mahdollisuus jakaa sovelluksessa näkyviä haasteita ja ehkä kategorisoida myös haasteet. Klikkaamalla haasteen auki voi lukea haastekuvauksen ja nähdä haasteen. Haasteessa pystyy klikkaamaan jokaista haasteen sisältämää kohdetta erikseen suoritetuksi (näkyy käyttäjäprofiilissä klikkaamalla "vierailut") ja nähdä kartan (kartta sijainti mahdollisesti maksullinen myöhemmin). Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.


* Käyttäjä voi kirjautua sisään ja ulos ☑ sekä luoda uuden tunnuksen.
* Käyttäjä näkee mantereen (useita) ☑ → haasteet kuvauksineen (useita haasteita) → haasteen ja kartan
* Käyttäjä voi lisätä haasteita lempilistalleen, merkitä suoritetuksi (Extra: jakaa sosiaalisessa mediassa) ja nähdä, montako käyttäjää on suorittanut haasteen (numerolla, ei käyttäjänimillä).
* Ylläpitäjä voi lisätä ja poistaa haasteita sekä määrittää haasteesta näytettävät tiedot. Ylläpitäjä voi tarvittaessa poistaa käyttäjän suorittaman haasteen.
* Käyttäjä voi luoda ja muokata omia lisäämiään haasteita sekä määrittää näytettävät tiedot (paitsi kartta).
* Käyttäjä voi etsiä kaikki haasteet, joiden kuvauksessa on annettu sana.
* Käyttäjä näkee ja pystyy suodattamaan haasteet aakkos-, suosikki-, ja kategoriajärjestyksessä.
* Ylläpitäjä voi luoda kategorioita, joihin haasteet voi luokitella. Haaste voi kuulua yhteen tai useampaan kategoriaan.

# Käynistysohjeet
1. Kloonaa tämä repositorio omalle koneellesi ja siirry Challenge-app kansioon.
2. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
   
`DATABASE_URL=<tietokannan-paikallinen-osoite>`

`SECRET_KEY=<salainen-avain>`

3. Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
   
**<p>$ python3 -m venv venv</p>**
**<p>$ source venv/bin/activate</p>**
**<p>$ pip install -r ./requirements.txt</p>**

4. Määritä vielä tietokannan skeema komennolla
   
**<p>psql < schemaPolls.sql</p>**
**<p>psql < schemaUser.sql</p>**

5. Nyt voit käynnistää sovelluksen komennolla
   
**$ flask run**

# Nykyinen tilanne

Sovellus on vielä keskeneräinen. Sovelluksen käynnistyessä avautuu etusivu, Frontpage: Login-linkistä pääsee kirjautumaan sovellukseen, jonka jälkeen käyttäjälle avautuvat yläpalkit Home, Mypages, Polls, kirjautuneen käyttäjän käyttäjätunnus ja Log Out. Home, Polls ja Log Out toimivat. Sivun vasen palkki ja haastenäkymä eivät toimi vielä.

