# coding=utf-8
from __future__ import unicode_literals
from ..address import Provider as AddressProvider


class Provider(AddressProvider):

    city_formats = ('{{city_name}}', )

    street_name_formats = ('{{street_name}}', )
    street_address_formats = ('{{street_name}} {{building_number}}', )
    address_formats = ('{{street_address}}\n{{postcode}} {{city}}', )

    building_number_formats = ('###', '##', '#', '#/#')

    street_suffixes_long = ('náměstí', )
    street_suffixes_short = ('nám.', )

    postcode_formats = ('### ##', )

    cities = (
        'Abertamy', 'Adamov', 'Andělská Hora', 'Bakov nad Jizerou', 'Bavorov', 'Bechyně', 'Benešov nad Ploučnicí', 
        'Benátky nad Jizerou', 'Bezdružice', 'Bečov nad Teplou', 'Blatná', 'Blovice', 'Blšany', 'Bochov', 
        'Bohušovice nad Ohří', 'Bojkovice', 'Bor', 'Borohrádek', 'Borovany', 'Boží Dar', 'Brandýs nad Orlicí', 
        'Brno', 'Broumov', 'Brtnice', 'Brumov-Bylnice', 'Brušperk', 'Budišov nad Budišovkou', 'Budyně nad Ohří', 
        'Bučovice', 'Buštěhrad', 'Bystré', 'Bystřice', 'Bystřice nad Pernštejnem', 'Bystřice pod Hostýnem', 'Bzenec', 
        'Bílovec', 'Bělá nad Radbuzou', 'Bělá pod Bezdězem', 'Březnice', 'Březová', 'Březová nad Svitavou', 'Břidličná', 
        'Chabařovice', 'Chlumec', 'Chlumec nad Cidlinou', 'Choceň', 'Chomutov', 'Chotěboř', 'Chrast', 'Chrastava', 
        'Chropyně', 'Chvaletice', 'Chyše', 'Chýnov', 'Chřibská', 'Cvikov', 'Dačice', 'Dašice', 'Desná', 'Deštná', 
        'Dobrovice', 'Dobruška', 'Dobřany', 'Dobřichovice', 'Dobříš', 'Doksy', 'Dolní Benešov', 'Dolní Bousov', 
        'Dolní Kounice', 'Dolní Poustevna', 'Dubá', 'Dubí', 'Dubňany', 'Duchcov', 'Děčín', 'Františkovy Lázně', 
        'Fryšták', 'Frýdek-Místek', 'Frýdlant', 'Frýdlant nad Ostravicí', 'Fulnek', 'Golčův Jeníkov', 'Habartov', 
        'Habry', 'Hanušovice', 'Harrachov', 'Hartmanice', 'Havířov', 'Hejnice', 'Heřmanův Městec', 'Hlinsko', 
        'Hluboká nad Vltavou', 'Hluk', 'Hodkovice nad Mohelkou', 'Holice', 'Holýšov', 'Hora Svaté Kateřiny', 
        'Horažďovice', 'Horní Benešov', 'Horní Blatná', 'Horní Bříza', 'Horní Cerekev', 'Horní Jelení', 'Horní Jiřetín', 
        'Horní Planá', 'Horní Slavkov', 'Horšovský Týn', 'Hostinné', 'Hostivice', 'Hostomice', 'Hostouň', 'Hořice', 
        'Hořovice', 'Hoštka', 'Hradec Králové', 'Hradec nad Moravicí', 'Hranice (okres Cheb)', 'Hrob', 'Hrochův Týnec', 
        'Hronov', 'Hrotovice', 'Hroznětín', 'Hrušovany nad Jevišovkou', 'Hrádek', 'Hrádek nad Nisou', 'Hulín', 'Husinec', 
        'Hustopeče', 'Ivanovice na Hané', 'Ivančice', 'Jablonec nad Jizerou', 'Jablonec nad Nisou', 'Jablonné nad Orlicí', 
        'Jablonné v Podještědí', 'Jablunkov', 'Janov', 'Janovice nad Úhlavou', 'Janské Lázně', 'Jaroměřice nad Rokytnou', 
        'Javorník', 'Jemnice', 'Jesenice (okres Rakovník)', 'Jevišovice', 'Jevíčko', 'Jihlava', 'Jilemnice', 'Jistebnice', 
        'Jiříkov', 'Jáchymov', 'Jílové', 'Jílové u Prahy', 'Kamenice nad Lipou', 'Kamenický Šenov', 'Kaplice', 
        'Kardašova Řečice', 'Karlovy Vary', 'Karolinka', 'Karviná', 'Kasejovice', 'Kaznějov', 'Kašperské Hory', 'Kdyně', 
        'Kelč', 'Kladno', 'Kladruby', 'Klecany', 'Klimkovice', 'Klobouky u Brna', 'Kojetín', 'Konice', 'Kopidlno', 
        'Koryčany', 'Kosmonosy', 'Kostelec na Hané', 'Kostelec nad Labem', 'Kostelec nad Orlicí', 
        'Kostelec nad Černými lesy', 'Kouřim', 'Košťany', 'Kožlany', 'Kralovice', 'Kraslice', 'Kravaře', 'Kryry', 
        'Králíky', 'Králův Dvůr', 'Krásno', 'Krásná Hora nad Vltavou', 'Krásná Lípa', 'Krásné Údolí', 'Kunovice', 
        'Kunštát', 'Kynšperk nad Ohří', 'Lanžhot', 'Ledeč nad Sázavou', 'Ledvice', 'Letohrad', 'Letovice', 'Liberec', 
        'Libochovice', 'Libušín', 'Libáň', 'Libčice nad Vltavou', 'Liběchov', 'Lipník nad Bečvou', 'Litovel', 'Lišov', 
        'Loket', 'Lom', 'Lomnice nad Lužnicí', 'Lomnice nad Popelkou', 'Loučná pod Klínovcem', 'Lovosice', 'Loštice', 
        'Luby', 'Luhačovice', 'Lučany nad Nisou', 'Luže', 'Lysá nad Labem', 'Lázně Bohdaneč', 'Lázně Bělohrad', 
        'Lázně Kynžvart', 'Manětín', 'Mašťov', 'Meziboří', 'Meziměstí', 'Mikulov', 'Mikulášovice', 'Miletín', 
        'Milevsko', 'Milovice', 'Mimoň', 'Miroslav', 'Mirotice', 'Mirovice', 'Mirošov', 'Mladá Boleslav', 
        'Mladá Vožice', 'Mnichovice', 'Mnichovo Hradiště', 'Mníšek pod Brdy', 'Modřice', 'Mohelnice', 
        'Moravské Budějovice', 'Moravský Beroun', 'Moravský Krumlov', 'Morkovice-Slížany', 'Most', 'Mýto', 
        'Městec Králové', 'Město Albrechtice', 'Město Touškov', 'Měčín', 'Mšeno', 'Nalžovské Hory', 'Napajedla', 
        'Nasavrky', 'Nechanice', 'Nejdek', 'Nepomuk', 'Netolice', 'Neveklov', 'Nová Bystřice', 'Nová Paka', 'Nová Role', 
        'Nová Včelnice', 'Nové Hrady', 'Nové Město nad Metují', 'Nové Město pod Smrkem', 'Nové Sedlo', 'Nové Strašecí', 
        'Nový Bydžov', 'Nový Knín', 'Náměšť nad Oslavou', 'Nýrsko', 'Nýřany', 'Němčice nad Hanou', 'Odolena Voda', 
        'Odry', 'Olešnice', 'Olomouc', 'Oloví', 'Opava', 'Opočno', 'Osek', 'Osečná', 'Oslavany', 'Ostrava', 'Pacov', 
        'Pardubice', 'Paskov', 'Pec pod Sněžkou', 'Petřvald', 'Pečky', 'Pilníkov', 'Planá', 'Planá nad Lužnicí', 
        'Plasy', 'Plesná', 'Plumlov', 'Plzeň', 'Plánice', 'Poběžovice', 'Podbořany', 'Podivín', 'Pohořelice', 
        'Police nad Metují', 'Polička', 'Polná', 'Postoloprty', 'Potštát', 'Počátky', 'Praha', 'Proseč', 'Prostějov', 
        'Protivín', 'Pyšely', 'Přebuz', 'Přelouč', 'Přerov', 'Přeštice', 'Přibyslav', 'Přimda', 'Příbor', 'Rabí', 
        'Radnice', 'Rajhrad', 'Ralsko', 'Raspenava', 'Rejštejn', 'Rokytnice nad Jizerou', 'Rokytnice v Orlických horách', 
        'Ronov nad Doubravou', 'Rosice', 'Rotava', 'Rousínov', 'Rovensko pod Troskami', 'Roztoky', 'Rožmberk nad Vltavou', 
        'Rožmitál pod Třemšínem', 'Rožďalovice', 'Rtyně v Podkrkonoší', 'Rudná', 'Rudolfov', 
        'Rychnov u Jablonce nad Nisou', 'Rychvald', 'Rájec-Jestřebí', 'Rýmařov', 'Sadská', 'Sedlec-Prčice', 'Sedlice', 
        'Sedlčany', 'Semily', 'Sezemice', 'Sezimovo Ústí', 'Seč', 'Skalná', 'Skuteč', 'Slatiňany', 'Slavičín', 
        'Slavkov u Brna', 'Slavonice', 'Slušovice', 'Smečno', 'Smiřice', 'Smržovka', 'Sobotka', 'Soběslav', 'Solnice', 
        'Spálené Poříčí', 'Staré Město (okres Uherské Hradiště)', 'Staré Město (okres Šumperk)', 'Starý Plzenec', 
        'Staňkov', 'Stochov', 'Stod', 'Strmilov', 'Stráž nad Nežárkou', 'Stráž pod Ralskem', 'Strážnice', 'Strážov', 
        'Studénka', 'Stárkov', 'Stříbro', 'Suchdol nad Lužnicí', 'Svoboda nad Úpou', 'Svratka', 'Světlá nad Sázavou', 
        'Sázava', 'Tanvald', 'Telč', 'Teplice', 'Teplice nad Metují','Teplá', 'Terezín', 'Tišnov', 'Toužim', 'Tovačov',
        'Trhové Sviny', 'Trhový Štěpánov', 'Trmice', 'Týn nad Vltavou', 'Týnec nad Labem', 'Týnec nad Sázavou', 
        'Týniště nad Orlicí', 'Třebechovice pod Orebem', 'Třebenice', 'Třeboň', 'Třemošnice', 'Třemošná', 'Třešť', 
        'Uherský Ostroh', 'Uhlířské Janovice', 'Unhošť', 'Valašské Klobouky', 'Valtice', 'Vamberk', 'Vejprty', 
        'Velešín', 'Velká Bystřice', 'Velká Bíteš', 'Velké Bílovice', 'Velké Hamry', 'Velké Opatovice', 
        'Velké Pavlovice', 'Velký Šenov', 'Veltrusy', 'Velvary', 'Verneřice', 'Veselí nad Lužnicí', 'Vidnava', 'Vimperk', 
        'Vizovice', 'Vlachovo Březí', 'Vodňany', 'Volary', 'Volyně', 'Votice', 'Vracov', 'Vratimov', 'Vrbno pod Pradědem', 
        'Vroutek', 'Vysoké Veselí', 'Vysoké nad Jizerou', 'Vyšší Brod', 'Vítkov', 'Výsluní', 'Všeruby', 'Zbiroh', 
        'Zbýšov', 'Zdice', 'Zlaté Hory', 'Zliv', 'Zlín', 'Zruč nad Sázavou', 'Zubří', 'Zákupy', 'Zásmuky', 
        'Újezd u Brna', 'Úpice', 'Úsov', 'Ústí nad Labem', 'Úterý', 'Úvaly', 'Úštěk', 'Černovice', 'Černošice', 
        'Černošín', 'Červená Řečice', 'Červený Kostelec', 'Česká Kamenice', 'Česká Skalice', 'České Budějovice', 
        'České Velenice', 'Český Brod', 'Český Dub', 'Řevnice', 'Šenov', 'Šlapanice', 'Šluknov', 'Špindlerův Mlýn', 
        'Štramberk', 'Štíty', 'Štětí', 'Švihov', 'Žacléř', 'Žamberk', 'Žandov', 'Ždánice', 'Ždírec nad Doubravou', 
        'Žebrák', 'Železnice', 'Železná Ruda', 'Železný Brod', 'Židlochovice', 'Žirovnice', 'Žlutice', 'Žulová'
    )

    streets = (
        'Horní Stromky', 'Vizovická', 'K Brusce', 'Mírová', 'Rašínská', 'Boušova', 'Pobřežní', 'Dolnobřežanská', 
        'Černá', 'Šůrova', 'Červenkova', 'Nad Mostem', 'Libuňská', 'Chotovická', 'Petříkova', 'Pod Vodárenskou Věží', 
        'Na Fišerce', 'Ke Březině', 'Za Lázeňkou', 'Nad Šafránkou', 'Na Laurové', 'Nám. Republiky', 'Vlašimská', 
        'Nad Rohatci', 'Tylišovská', 'Nábřeží Kapitána Jaroše', 'Lešovská', 'U Podjezdu', 'Průškova', 'Estonská', 
        'Máslova', 'K Otočce', 'Jižní', 'Švecova', 'Mongolská', 'Kalská', 'Nad Rokytkou', 'Malešovská', 'Plzeňská', 
        'V Hájkách', 'Úpská', 'Ambrožova', 'Pikovická', 'Neužilova', 'Na Staré Vinici', 'Vstupní', 'Nýdecká', 
        'U Společenské Zahrady', 'Ostrovského', 'Bazovského', 'Lešenská', 'Na Štamberku', 'Na Svahu', 'Výhledské Nám.', 
        'K Lipám', 'Za Stadionem', 'Opletalova', 'Nábřeží Ludvíka Svobody', 'Komenského Nám.', 'Křimická', 'Domkovská', 
        'Pyšelská', 'Štychova', 'Horákova', 'Nad Zavážkou', 'K Prelátům', 'Vašátkova', 'Benákova', 
        'Náměstí Prezidenta Masaryka', 'Mílovská', 'U Hostivařského Nádraží', 'Jihovýchodní I', 'Hostivařské Nám.', 
        'Zbynická', 'Heineho', 'U Dobešky', 'Doubická', 'Ke Břvům', 'Na Záhonech', 'Kloboukova', 'Kostnické Náměstí', 
        'Pelclova', 'Smotlachova', 'Pod Spiritkou', 'Hůlkova', 'Matenská', 'Do Zahrádek Ii', 'Dobrošovská', 'Lovčenská', 
        'Jasná I', 'Škrétova', 'Moravanů', 'Budapešťská', 'Kojetická', 'Náměstí I. P. Pavlova', 'Bajkalská', 
        'U Větrolamu', 'Vlčická', 'Jarešova', 'Sámova', 'Kotrčová', 'Musílkova', 'Ingrišova', 'U Nových Domů I', 
        'Dělostřelecká', 'Ke Hrázi', 'Mochovská', 'Rýmařovská', 'Dolní Chaloupky', 'Za Arielem', 'U Rajské Zahrady', 
        'K Šedivce', 'Březová', 'Doubravínova', 'Mládkova', 'Tachovské Náměstí', 'Lehárova', 'Severní X', 
        'V Tehovičkách', 'Bermanova', 'Grammova', 'Spojovací', 'Verdunská', 'Závrchy', 'Čerpadlová', 'Vítězná', 
        'Nad Plynovodem', 'U Smíchovského Hřbitova', 'Nedvědovo Náměstí', 'Bachova', 'U Dálnice', 'Všejanská', 
        'Maňákova', 'Rokytnická', 'Loděnická', 'U Pumpy', 'Michnova', 'Záblatská', 'Poslední', 'Hněvkovského', 
        'Za Křížem', 'Nad Návsí', 'Jablonecká', 'Súdánská', 'Mazancova', 'Pod Čertovou Skalou', 'Weilova', 
        'Čajkovského', 'Nad Zátiším', 'Moldavská', 'Juarézova', 'Žižkova', 'Pod Lochkovem', 'Nad Vernerákem', 
        'Žherská', 'Prusíkova', 'Výtoňská', 'Na Srážku', 'Šachovská', 'Nučická', 'Novákovo Náměstí', 'Sitteho', 
        'U Vápenice', 'Na Kuthence', 'Čelakovského Sady', 'V Závitu', 'Na Vartě', 'Oválová', 'Machovická', 
        'Nad Olšinami', 'Vajgarská', 'Kulhavého', 'Kodaňská', 'Kralupská', 'Lednická', 'Pod Velkým Hájem', 
        'Hvězdonická', 'Na Kozinci', 'Semická', 'K Dálnici', 'Trytova', 'Vyhlídkova', 'Pohnertova', 'U Nového Dvora', 
        'K Vodě', 'Nad Libří', 'K Matěji', 'V Kotcích', 'Kohoutových', 'Na Cikánce', 'Chládkova', 'Slatiňanská', 
        'Pod Kostelem', 'Na Spojce', 'Na Zahrádkách', 'Nad Obcí', 'K Přehradám', 'Na Náspu', 'V Nížinách', 
        'Josefa Houdka', 'Na Pěšině', 'Hnězdenská', 'Za Statky', 'Kremnická', 'Čestmírova', 'U Rakovky', 'Kodicilova', 
        'K Lučinám', 'Nouzov', 'Krátký Lán', 'Anny Drabíkové', 'Kadaňská', 'Stroupežnického', 'Jírova', 
        'U Dětského Hřiště', 'Žofie Podlipské', 'Nad Šancemi', 'Lošáková', 'Roblínská', 'Mezi Sklady', 'Na Pomezí', 
        'U Mlýnského Rybníka', 'Makedonská', 'K Dýmači', 'V Zátiší', 'Pohořelec', 'Jiřinková', 'U Nové Dálnice', 
        'Čuprova', 'Vraňanská', 'Severovýchodní Vi', 'Petřínská', 'K Hořavce', 'Sádovská', 'Pod Průsekem', 'Konžská', 
        'Dřítenská', 'Pirinská', 'U Hřiště', 'Kukelská', 'Moravanská', 'Koclířova', 'Žilinská', 'Ve Žlíbku', 
        'Veronské Nám.', 'U Větrníku', 'Svojsíkova', 'Izraelská', 'Staňkovka', 'Na Viničních Horách', 'Čankovská', 
        'Na Špitálce', 'Valdovská', 'Rudoltická', 'Ke Strašnické', 'Paťanka', 'Panuškova', 'Pankrácké Nám.', 
        'Budčická', 'Šermířská', 'Medlovská', 'K Vidouli', 'Horní Chaloupky', 'V Americe', 'Dejvická', 'Klášterecká', 
        'Šárovo Kolo', 'Mladoboleslavská', 'Palackého', 'Lumiérů', 'Ivančická', 'Za Valem', 'Na Břevnovské Pláni', 
        'Tichonická', 'Náměstí Hrdinů', 'Mistřínská', 'Křížkovského', 'Tanvaldská', 'V Padolině', 'Před Skalkami Ii', 
        'Na Křivce', 'Nad Zámečkem', 'Nad Krocínkou', 'Podlešínská', 'Nad Popelkou', 'Oderská', 'Jeruzalémská', 
        'Smolenská', 'Lebeděvova', 'Libichovská', 'Na Šafránce', 'Průjezdná', 'Záluské', 'Branišovská', 'Spinozova', 
        'K Betáni', 'Machuldova', 'Podohradská', 'Cerhenická', 'V Brůdku', 'U Vlachovky', 'Pod Letištěm', 
        'Vlastislavova', 'Klecanská', 'Žinkovská', 'Maltézské Náměstí', 'Boršov', 'Mukařovského', 'Josefa Šimůnka', 
        'Suchdolská', 'Opočínská', 'Heydukova', 'Vršovka', 'Thurnova', 'Mezilesní', 'Za Pivovarem', 'Uljanovská', 
        'Panenská', 'Sladovnická', 'Plynární', 'Kozácká', 'Vlasákova', 'Javornická', 'Ševčíkova', 'Podle Náhonu', 
        'Doubravická', 'Františka Černého', 'Chotětovská', 'K Háječku', 'Pod Výšinkou', 'U Šesté Baterie', 'Drahanská', 
        'Augustova', 'U Balabenky', 'Boční I', 'Jirčanská', 'Na Šubě', 'Brixiho', 'Klímova', 'Kazín', 
        'Fügnerovo Náměstí', 'Na Příčné Mezi', 'Plánická', 'Africká', 'Vratislavova', 'Olympijská', 'Na Bojišti', 
        'K Nádrži', 'Vokrojova', 'Bořetínská', 'Kováříkova', 'Lánovská', 'U Staré Pošty', 'Na Poustkách', 'V Poli', 
        'Meziškolská', 'Pajerova', 'Habartovská', 'Mlékárenská', 'Dělnická', 'U Štěpu', 'Družná', 'Klouzková', 
        'Před Rybníkem', 'Nad Košinkou', 'Spolupráce', 'V Humenci', 'Adélčina', 'Březanova', 'Pod Kesnerkou', 
        'Kosmonoská', 'Do Dubin', 'Nad Lávkou', 'Mezi Lysinami', 'Na Topolce', 'Snopkova', 'Severní Viii', 'Okrová', 
        'Třebihošťská', 'Mádrova', 'Na Lázeňce', 'Slivenecká', 'Nám. Barikád', 'Nad Strouhou', 'Jindřicha Plachty', 
        'Pod Srázem', 'U Waltrovky', 'Bratří Čapků', 'Onšovecká', 'Machnova', 'Kostková', 'Rožmberská', 'Zapských', 
        'Přípřežní', 'Výravská', 'Podléšková', 'Štěchovická', 'Poleradská', 'Jilmová', 'Hostýnská'
    )

    states = (
        'Hlavní město Praha',
        'Středočeský kraj',
        'Jihočeský kraj',
        'Plzeňský kraj',
        'Karlovarský kraj',
        'Ústecký kraj',
        'Liberecký kraj',
        'Královéhradecký kraj',
        'Pardubický kraj',
        'Kraj Vysočina',
        'Jihomoravský kraj',
        'Olomoucký kraj',
        'Moravskoslezský kraj',
        'Zlínský kraj',
    )

    countries = (
        'Afghánistán', 'Albánie', 'Alžírsko', 'Andorra', 'Angola', 'Antigua a Barbuda', 'Argentina', 'Arménie', 
        'Austrálie', 'Bahamy', 'Bahrajn', 'Bangladéš', 'Barbados', 'Belgie', 'Belize', 'Benin', 'Bhútán', 'Bolívie', 
        'Bosna a Hercegovina', 'Botswana', 'Brazílie', 'Brunej', 'Bulharsko', 'Burkina Faso', 'Burundi', 'Bělorusko', 
        'Chile', 'Chorvatsko', 'Cookovy ostrovy', 'Demokratická republika Kongo', 'Dominika', 'Dominikánská republika', 
        'Dánsko', 'Džibutsko', 'Egypt', 'Ekvádor', 'Eritrea', 'Estonsko', 'Etiopie', 'Federativní státy Mikronésie', 
        'Fidži', 'Filipíny', 'Finsko', 'Francie', 'Gabon', 'Gambie', 'Ghana', 'Gruzie', 'Guatemala', 'Guinea', 
        'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Indie', 'Irsko', 'Irák', 'Island', 'Itálie', 'Izrael', 
        'Jamajka', 'Japonsko', 'Jemen', 'Jihoafrická republika', 'Jižní Súdán', 'Jordánsko', 'Kambodža', 'Kamerun', 
        'Kanada', 'Kapverdy', 'Katar', 'Kazachstán', 'Keňa', 'Kiribati', 'Kolumbie', 'Kostarika', 'Kuba', 'Kypr', 
        'Kyrgyzstán', 'Laos', 'Lesotho', 'Libanon', 'Libye', 'Lichtenštejnsko', 'Litva', 'Lotyšsko', 'Lucembursko', 
        'Madagaskar', 'Makedonie', 'Malajsie', 'Malawi', 'Maledivy', 'Mali', 'Malta', 'Maroko', 'Marshallovy ostrovy', 
        'Mauricius', 'Mauritánie', 'Maďarsko', 'Mexiko', 'Moldavsko', 'Monako', 'Mongolsko', 'Mosambik', 'Myanmar', 
        'Namibie', 'Nauru', 'Nepál', 'Niger', 'Nigérie', 'Nikaragua', 'Niue', 'Nizozemsko', 'Norsko', 'Nový Zéland', 
        'Německo', 'Omán', 'Palau', 'Panama', 'Papua-Nová Guinea', 'Paraguay', 'Peru', 'Pobřeží slonoviny', 'Polsko', 
        'Portugalsko', 'Pákistán', 'Rakousko', 'Republika Kongo', 'Rovníková Guinea', 'Rumunsko', 'Rusko', 'Rwanda', 
        'Salvador', 'Samoa', 'San Marino', 'Saúdská Arábie', 'Senegal', 'Severní Korea', 'Seychely', 'Sierra Leone', 
        'Singapur', 'Slovensko', 'Slovinsko', 'Somálsko', 'Spojené arabské emiráty', 'Spojené království', 
        'Spojené státy americké', 'Srbsko', 'Středoafrická republika', 'Surinam', 'Svatá Lucie', 'Svatý Kryštof a Nevis', 
        'Svatý Tomáš a Princův ostrov', 'Svatý Vincenc a Grenadiny', 'Svazijsko', 'Súdán', 'Sýrie', 'Tanzanie', 
        'Thajsko', 'Togo', 'Tonga', 'Trinidad a Tobago', 'Tunisko', 'Turecko', 'Turkmenistán', 'Tuvalu', 'Tádžikistán', 
        'Uganda', 'Ukrajina', 'Uruguay', 'Uzbekistán', 'Vanuatu', 'Vatikán', 'Venezuela', 'Vietnam', 'Východní Timor', 
        'Zambie', 'Zimbabwe', 'Ázerbájdžán', 'Írán', 'Čad', 'Černá Hora', 'Česko', 'Čína', 'Řecko', 'Šalamounovy ostrovy', 
        'Španělsko', 'Srí Lanka', 'Švédsko', 'Švýcarsko'
    )

    @classmethod
    def street_suffix_short(cls):
        return cls.random_element(cls.street_suffixes_short)

    @classmethod
    def street_suffix_long(cls):
        return cls.random_element(cls.street_suffixes_long)

    @classmethod
    def city_name(cls):
        return cls.random_element(cls.cities)

    @classmethod
    def street_name(cls):
        return cls.random_element(cls.streets)

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)
