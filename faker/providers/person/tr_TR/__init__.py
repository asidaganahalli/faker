from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{first_name_female}} {{last_name}} {{last_name}}",
        "{{first_name_female}} {{last_name}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{first_name_female}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{first_name_female}} {{last_name}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}} {{last_name}}",
    )

    formats_male = (
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{first_name_male}} {{last_name}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{first_name_male}} {{last_name}}",
    )

    formats = formats_male + formats_female

    first_names_female = (
        "Abiye",
        "Acarkan",
        "Adal",
        "Adila",
        "Adviye",
        "Afife",
        "Ahter",
        "Akay",
        "Akgüneş",
        "Akise",
        "Akmaral",
        "Aksoy",
        "Akyıldız",
        "Alabezek",
        "Alaz",
        "Algış",
        "Alize",
        "Almast",
        "Alsoy",
        "Altınbike",
        "Altınçiçek",
        "Alışık",
        "Amre",
        "Anargül",
        "Anka",
        "Aral",
        "Armahan",
        "Arziye",
        "Arıpınar",
        "Asiman",
        "Asliye",
        "Asu",
        "Atanur",
        "Atiyye",
        "Avunç",
        "Ayasun",
        "Aybet",
        "Aycagül",
        "Aydar",
        "Ayduru",
        "Aygönenç",
        "Ayhan",
        "Aykut",
        "Aylil",
        "Aynilhayat",
        "Aynımah",
        "Aysema",
        "Aysevim",
        "Aysuna",
        "Ayten",
        "Aytöz",
        "Ayyaruk",
        "Ayçan",
        "Ayülker",
        "Ayşeana",
        "Ayşenur",
        "Azade",
        "Azize",
        "Açılay",
        "Ağbegim",
        "Aşhan",
        "Badegül",
        "Bahtinur",
        "Balca",
        "Ballı",
        "Banü",
        "Basriye",
        "Bağdat",
        "Bediriye",
        "Begim",
        "Behiza",
        "Belgizar",
        "Belkize",
        "Benek",
        "Benice",
        "Beray",
        "Bergen",
        "Beriye",
        "Berrin",
        "Besey",
        "Beste",
        "Beyhatun",
        "Bezek",
        "Bidayet",
        "Bilay",
        "Bilginur",
        "Bilkay",
        "Binay",
        "Birben",
        "Birgül",
        "Birsan",
        "Bitül",
        "Burcuhan",
        "Buşra",
        "Büreyre",
        "Büşranur",
        "Canan",
        "Canfeza",
        "Cannur",
        "Canseven",
        "Canur",
        "Cedide",
        "Cemiyle",
        "Cevale",
        "Ceyhun",
        "Cihan",
        "Cuheyna",
        "Damlanur",
        "Deha",
        "Deniz",
        "Deryanur",
        "Değer",
        "Dilara",
        "Dilcan",
        "Dilfeza",
        "Dilhuş",
        "Dilsitan",
        "Dilşat",
        "Divan",
        "Doğannur",
        "Duha",
        "Durgadin",
        "Dursadiye",
        "Duyguhan",
        "Döner",
        "Dürrüşehvar",
        "Ecegül",
        "Edaviye",
        "Efil",
        "Egenur",
        "Elamiye",
        "Elgin",
        "Elifnur",
        "Elvan",
        "Emal",
        "Emine.",
        "Emiş",
        "Enfes",
        "Erbay",
        "Erem",
        "Ergül",
        "Eriş",
        "Ervaniye",
        "Esengün",
        "Esmanperi",
        "Esna",
        "Evde",
        "Evrim",
        "Ezgin",
        "Eşim",
        "Fadile",
        "Fadıla",
        "Faize",
        "Fatigül",
        "Fatinur",
        "Fatmanur",
        "Fayize",
        "Feden",
        "Fehmiye",
        "Ferahdiba",
        "Feraye",
        "Ferhan",
        "Ferinaz",
        "Fermuta",
        "Feryas",
        "Feyha",
        "Feyzin",
        "Fidaye",
        "Fildan",
        "Firdevis",
        "Fitnat",
        "Fügen",
        "Gabel",
        "Ganiye",
        "Gelengül",
        "Gilman",
        "Goncafer",
        "Gök",
        "Gökperi",
        "Gökçe",
        "Göli",
        "Görsev",
        "Gözem",
        "Gül",
        "Gülay",
        "Gülbani",
        "Gülbeyan",
        "Gülbiye",
        "Gülcegün",
        "Güldam",
        "Gülder",
        "Güldünya",
        "Gülenay",
        "Güler",
        "Gülev",
        "Gülfari",
        "Gülfeza",
        "Gülgen",
        "Gülgüzel",
        "Gülhisar",
        "Gülinaz",
        "Gülkadın",
        "Güllühan",
        "Gülmisal",
        "Gülnaziye",
        "Gülper",
        "Gülsalın",
        "Gülselin",
        "Gülseren",
        "Gülsevil",
        "Gülsiye",
        "Gülsü",
        "Gülter",
        "Gülzadiye",
        "Gülçe",
        "Gülözge",
        "Gülüs",
        "Gülşa",
        "Gülşeref",
        "Günar",
        "Günebakan",
        "Güngören",
        "Günsel",
        "Günver",
        "Gürcüye",
        "Gürten",
        "Güverçin",
        "Güzey",
        "Habibe",
        "Hacile",
        "Hadrey",
        "Hafıza",
        "Halenur",
        "Haliye",
        "Hamiyet",
        "Hanbiken",
        "Hanim",
        "Hansultan",
        "Harbinaz",
        "Hasgül",
        "Hasret",
        "Hatin",
        "Havali",
        "Havse",
        "Hayel",
        "Hayrünnisa",
        "Hazine",
        "Hekime",
        "Henife",
        "Heva",
        "Hezniye",
        "Hilayda",
        "Hinet",
        "Hoşkadem",
        "Huban",
        "Hurican",
        "Hurşide",
        "Hüda",
        "Hümeyra",
        "Hürmet",
        "Hürüyet",
        "Hüsnühâl",
        "Ildız",
        "Irıs",
        "Işin",
        "Işın",
        "Jaruthip",
        "Kader",
        "Kadınana",
        "Kandef",
        "Kardelen",
        "Kaver",
        "Kefser",
        "Kerime",
        "Kezban",
        "Kifaye",
        "Kitan",
        "Koncagül",
        "Kumral",
        "Kutgün",
        "Kutun",
        "Kâzime",
        "Kübran",
        "Kısmet",
        "Laika",
        "Laze",
        "Lerze",
        "Leyli",
        "Lezize",
        "Limon",
        "Lâle",
        "Lüfen",
        "Macide",
        "Mahigül",
        "Mahnaz",
        "Mahter",
        "Maksüde",
        "Masume",
        "Maynur",
        "Maşide",
        "Mecide",
        "Mefharet",
        "Mehdiye",
        "Mehrigül",
        "Melaha",
        "Meleknur",
        "Melikkan",
        "Melûl",
        "Menfeat",
        "Menişan",
        "Merba",
        "Merim",
        "Merva",
        "Meryeme",
        "Mesude",
        "Meveddet",
        "Mevlüdiye",
        "Meyhanim",
        "Mezide",
        "Mihrab",
        "Mihriye",
        "Minibe",
        "Miray",
        "Misra",
        "Miyesser",
        "Muarra",
        "Mufide",
        "Muhiye",
        "Mujde",
        "Mukbile",
        "Musaffa",
        "Muvahhide",
        "Mübetcel",
        "Mücevher",
        "Müferrih",
        "Müjde",
        "Mükrüme",
        "Mümtaze",
        "Münezzer",
        "Müret",
        "Müsemma",
        "Müveddet",
        "Müğber",
        "Müşüre",
        "Nades",
        "Nafile",
        "Naide",
        "Nalân",
        "Narhanim",
        "Nasiba",
        "Natalia",
        "Naz",
        "Nazende",
        "Nazi",
        "Nazimet",
        "Nazlihan",
        "Nazıdil",
        "Nebiha",
        "Necilal",
        "Necva",
        "Nefaret",
        "Nefiye",
        "Nejdet",
        "Neptün",
        "Neriban",
        "Nesfe",
        "Neslinur",
        "Neval",
        "Nevgin",
        "Nevise",
        "Nevsale",
        "Neyran",
        "Nezengül",
        "Nezize",
        "Neşrin",
        "Nihan",
        "Nilcan",
        "Nili",
        "Nirgül",
        "Niğmet",
        "Nura",
        "Nurbanu",
        "Nurda",
        "Nurdeniz",
        "Nurey",
        "Nurgil",
        "Nurhayet",
        "Nuriyet",
        "Nurmelek",
        "Nurseda",
        "Nurser",
        "Nursim",
        "Nurtaç",
        "Nurveren",
        "Nurşan",
        "Nüdret",
        "Nürice",
        "Oguş",
        "Oluş",
        "Orçin",
        "Paksu",
        "Paye",
        "Pekkan",
        "Pembesin",
        "Peren",
        "Perinur",
        "Permun",
        "Pesent",
        "Piran",
        "Pürçek",
        "Rabbiye",
        "Rafia",
        "Rahiye",
        "Rakide",
        "Rana",
        "Rayla",
        "Rebihat",
        "Refet",
        "Rehime",
        "Rengül",
        "Revza",
        "Rezin",
        "Risalet",
        "Rojnu",
        "Ruhide",
        "Ruhugül",
        "Rumeysa",
        "Rümeysa",
        "Rıfkıye",
        "Sabihe",
        "Sabır",
        "Sadeti",
        "Sadiye",
        "Safinaz",
        "Safura",
        "Sahil",
        "Saire",
        "Salimet",
        "Samahat",
        "Sanavber",
        "Sanur",
        "Sarya",
        "Satıa",
        "Saygın",
        "Saçı",
        "Sebigül",
        "Seblâ",
        "Sedife",
        "Sefer",
        "Sehel",
        "Sejda",
        "Selcen",
        "Selime",
        "Selmin",
        "Selvi",
        "Selçuk",
        "Semat",
        "Semine",
        "Semrin",
        "Seniha",
        "Serda",
        "Serfinaz",
        "Serma",
        "Sernur",
        "Servinaz",
        "Sevcan",
        "Sevdinar",
        "Sevgen",
        "Sevginur",
        "Sevican",
        "Sevim",
        "Sevla",
        "Sevsevil",
        "Seyhan",
        "Seyyide",
        "Sezen",
        "Seçgül",
        "Sidar",
        "Silanur",
        "Simber",
        "Simten",
        "Sirap",
        "Siti",
        "Solma",
        "Sonnur",
        "Soykan",
        "Subutiye",
        "Sultane",
        "Sunay",
        "Susam",
        "Söyler",
        "Süheyda",
        "Süleyla",
        "Sümerya",
        "Süner",
        "Süsen",
        "Süzer",
        "Sırriye",
        "Tagangül",
        "Talibe",
        "Tan",
        "Tangül",
        "Tanses",
        "Tanyu",
        "Tasvir",
        "Tayyibe",
        "Taçnur",
        "Teknaz",
        "Temime",
        "Tercan",
        "Teybet",
        "Ticen",
        "Tomurcuk",
        "Tule",
        "Turcein",
        "Tutkucan",
        "Tuğçe",
        "Tülin",
        "Türcan",
        "Türknur",
        "Tüzenur",
        "Ufukay",
        "Ummahani",
        "Umuşan",
        "Uyanser",
        "Uğur",
        "Vacibe",
        "Varlık",
        "Vecide",
        "Vefia",
        "Verde",
        "Vezrife",
        "Vildane",
        "Yahşi",
        "Yalın",
        "Yasemen",
        "Yazgül",
        "Yaşar",
        "Yekbun",
        "Yepelek",
        "Yeşil",
        "Yosma",
        "Yurdaser",
        "Yurtseven",
        "Yücel",
        "Yıldız",
        "Zahfer",
        "Zaliha",
        "Zebirce",
        "Zehranur",
        "Zelha",
        "Zemzem",
        "Zerafet",
        "Zeride",
        "Zevlüde",
        "Zeyno",
        "Zilfa",
        "Zinnure",
        "Zubeyde",
        "Zöhrehan",
        "Züheyla",
        "Zülbiye",
        "Zülfüye",
        "Zümre",
        "Âlemşah",
        "Çalım",
        "Çağlar",
        "Çevregül",
        "Çilga",
        "Çisem",
        "Çolpan",
        "Ömriye",
        "Öncel",
        "Örfiye",
        "Övün",
        "Özay",
        "Özbilge",
        "Özdeş",
        "Özge",
        "Özgün",
        "Özlem",
        "Özpetek",
        "Özyurt",
        "Üge",
        "Ülke",
        "Ülküm",
        "Ümmahan",
        "Ümmühan",
        "Ümray",
        "Ünal",
        "Ünsever",
        "Ürper",
        "Üçgül",
        "İde",
        "İhsan",
        "İklim",
        "İldeş",
        "İlkbahar",
        "İlklima",
        "İlper",
        "İmge",
        "İmrihan",
        "İncifir",
        "İnsaf",
        "İrfan",
        "İslime",
        "İsra",
        "İzel",
        "İçimbike",
        "Şadıman",
        "Şahdiye",
        "Şahinder",
        "Şahnuray",
        "Şahıgül",
        "Şamiha",
        "Şayan",
        "Şazime",
        "Şefiye",
        "Şehreban",
        "Şehza",
        "Şelâle",
        "Şemsinisa",
        "Şendoğan",
        "Şennur",
        "Şeref",
        "Şerman",
        "Şevketfeza",
        "Şeyda",
        "Şilan",
        "Şirivan",
        "Şöhret",
        "Şüküfe",
    )

    first_names_male = (
        "Abdiş",
        "Abdulbekir",
        "Abdulgazi",
        "Abdulkadir",
        "Abdulmenaf",
        "Abdulsemet",
        "Abdurrahman",
        "Abdülahat",
        "Abdülcemal",
        "Abdülhadi",
        "Abdülkerim",
        "Abdülsamed",
        "Abdürreşit",
        "Abid",
        "Abuzar",
        "Acar",
        "Aclan",
        "Adak",
        "Adasal",
        "Adlan",
        "Adıgün",
        "Afer",
        "Ahat",
        "Ahsen",
        "Akalan",
        "Akar",
        "Akatay",
        "Akbaş",
        "Akboğa",
        "Akcivan",
        "Akdora",
        "Akdurmuş",
        "Akgöl",
        "Akif",
        "Akkerman",
        "Akmaner",
        "Aksay",
        "Aksöğüt",
        "Aktemür",
        "Akver",
        "Akçabay",
        "Akçasu",
        "Aköz",
        "Akınal",
        "Alaaddin",
        "Alaeddin",
        "Alanalp",
        "Alattin",
        "Alcan",
        "Alexandru",
        "Aliabbas",
        "Aliihsan",
        "Aliseydi",
        "Alkor",
        "Almus",
        "Alparslan",
        "Alpcan",
        "Alpin",
        "Alpsü",
        "Alsoy",
        "Altoğan",
        "Altuğ",
        "Altınkaya",
        "Altınışın",
        "Amaç",
        "Andiç",
        "Annak",
        "Apaydın",
        "Aran",
        "Arcan",
        "Argu",
        "Arifcan",
        "Arkut",
        "Arpağ",
        "Artan",
        "Aru",
        "Arıel",
        "Arıkol",
        "Arısoy",
        "Asalet",
        "Aslanhan",
        "Asım",
        "Atagün",
        "Atalay",
        "Atasagun",
        "Atatöre",
        "Atgun",
        "Atilhan",
        "Atnan",
        "Atılgan",
        "Avşin",
        "Ayaydın",
        "Aybora",
        "Aydinç",
        "Aydınbey",
        "Aygutalp",
        "Aykutalp",
        "Aypar",
        "Aysoy",
        "Aytek",
        "Aytuna",
        "Ayvas",
        "Ayşan",
        "Azettin",
        "Açıkel",
        "Ağakişi",
        "Ağmur",
        "Aşir",
        "Baba",
        "Bahaddin",
        "Bahittin",
        "Baki",
        "Balatekin",
        "Bali",
        "Baltaş",
        "Barak",
        "Bariş",
        "Barsen",
        "Barışcan",
        "Basım",
        "Baturay",
        "Batırhan",
        "Baydu",
        "Baykan",
        "Bayman",
        "Bayruhan",
        "Baytal",
        "Bayzettin",
        "Bağdaş",
        "Başay",
        "Başhan",
        "Başok",
        "Bedi",
        "Bedri",
        "Behrem",
        "Bekbay",
        "Bektaşi",
        "Bellisan",
        "Bengibay",
        "Benol",
        "Beren",
        "Berkal",
        "Berki",
        "Berksay",
        "Berran",
        "Besin",
        "Beyda",
        "Beyler",
        "Beyzade",
        "Bican",
        "Bilender",
        "Bilgen",
        "Bilgütay",
        "Biltaş",
        "Binbaşar",
        "Binışık",
        "Birgit",
        "Birsen",
        "Bişar",
        "Borahan",
        "Borataş",
        "Boynak",
        "Bozbağ",
        "Bozerk",
        "Boztaş",
        "Boğatimur",
        "Buhari",
        "Bulunç",
        "Burakhan",
        "Burç",
        "Buyrukhan",
        "Börteçin",
        "Büget",
        "Bünyamün",
        "Cabir",
        "Canal",
        "Canberk",
        "Candeniz",
        "Cangür",
        "Cannur",
        "Cansin",
        "Cantez",
        "Cavit",
        "Cebesoy",
        "Celilay",
        "Cemalettin",
        "Cenan",
        "Cercis",
        "Cevheri",
        "Cezayir",
        "Cihandide",
        "Cindoruk",
        "Coşkun",
        "Cuman",
        "Cüneyit",
        "Dalan",
        "Dalkılıç",
        "Danış",
        "Dayar",
        "Dağistan",
        "Delil",
        "Demirbüken",
        "Demiriz",
        "Demirok",
        "Demiryürek",
        "Denizalp",
        "Denkel",
        "Derkay",
        "Deviner",
        "Değmeer",
        "Diken",
        "Dilder",
        "Dincer",
        "Dinçkol",
        "Dinçsü",
        "Dirican",
        "Dirlik",
        "Dolun",
        "Dorukhan",
        "Doğanalp",
        "Doğanşah",
        "Doğuhan",
        "Duracan",
        "Durdali",
        "Durmuşali",
        "Duruk",
        "Duruöz",
        "Dölensoy",
        "Dündaralp",
        "Eba",
        "Ebuakil",
        "Ecemiş",
        "Edgübay",
        "Efe",
        "Eflâtun",
        "Efser",
        "Ekber",
        "Ekmel",
        "Elhan",
        "Elnur",
        "Elöve",
        "Emin",
        "Emirşan",
        "Emrullah",
        "Enes",
        "Enginiz",
        "Ensari",
        "Eral",
        "Eraycan",
        "Erbil",
        "Ercihan",
        "Erdemer",
        "Erdibay",
        "Erdogan",
        "Erdursun",
        "Erenalp",
        "Erensoy",
        "Ergener",
        "Erginel",
        "Ergönül",
        "Ergün",
        "Erik",
        "Erinçer",
        "Erkan",
        "Erkinel",
        "Erksoy",
        "Erkılıç",
        "Ermutlu",
        "Eroğul",
        "Ersel",
        "Erseç",
        "Ertan",
        "Erten",
        "Ertuncay",
        "Ertün",
        "Eryıldız",
        "Eröz",
        "Erşat",
        "Esenbay",
        "Esentürk",
        "Eskinalp",
        "Evcimen",
        "Evrimer",
        "Eyyüp",
        "Ezgütekin",
        "Eşref",
        "Fahrullah",
        "Fami",
        "Fatih",
        "Fazul",
        "Fehim",
        "Fenni",
        "Ferat",
        "Feremez",
        "Ferihan",
        "Fersan",
        "Ferzi",
        "Fetullah",
        "Feyruz",
        "Feza",
        "Filit",
        "Fuzuli",
        "Galip",
        "Gazel",
        "Gencaslan",
        "Gençay",
        "Geray",
        "Ginyas",
        "Giz",
        "Gökay",
        "Gökbudun",
        "Göken",
        "Göknur",
        "Göksev",
        "Gökten",
        "Gökçebalan",
        "Gökçil",
        "Gönen",
        "Görgünay",
        "Görklü",
        "Gözel",
        "Gücal",
        "Gülağa",
        "Gülel",
        "Güleğen",
        "Gülşahin",
        "Gümüştekin",
        "Günaydin",
        "Günden",
        "Gündüzalp",
        "Güneri",
        "Güngördü",
        "Günkurt",
        "Günser",
        "Günver",
        "Günşen",
        "Gürarda",
        "Gürelcem",
        "Gürsal",
        "Güçal",
        "Güçlüer",
        "Güçyeter",
        "Haciali",
        "Hakikat",
        "Halidun",
        "Haluk",
        "Hami",
        "Hanedan",
        "Hariz",
        "Hasbek",
        "Hatem",
        "Hayali",
        "Hayret",
        "Hazrat",
        "Hekmet",
        "Heyvetullah",
        "Hidir",
        "Hindal",
        "Hiçsönmez",
        "Hudavent",
        "Hunalp",
        "Huzuri",
        "Hükümdar",
        "Hürdoğan",
        "Hüryaşar",
        "Hüsmen",
        "Hıfzullah",
        "Idık",
        "Ilgı",
        "Ismık",
        "Işıkay",
        "Işıman",
        "Jankat",
        "Kader",
        "Kahir",
        "Kalgay",
        "Kamar",
        "Kanak",
        "Kanpulat",
        "Kapagan",
        "Karabaş",
        "Karaca",
        "Karaer",
        "Karakucak",
        "Karanbay",
        "Karataş",
        "Karcan",
        "Karlukhan",
        "Kasim",
        "Kavurt",
        "Kayagün",
        "Kaygusuz",
        "Kayrabay",
        "Kayıt",
        "Kaşif",
        "Kelâmi",
        "Kenter",
        "Kerman",
        "Kete",
        "Kibar",
        "Kiramettin",
        "Kiyasi",
        "Kocabaş",
        "Koldan",
        "Konguralp",
        "Kopan",
        "Koray",
        "Korkmazalp",
        "Korugan",
        "Kotuz",
        "Koçak",
        "Koçkan",
        "Koşukhan",
        "Kuddusi",
        "Kutay",
        "Kâmil",
        "Köker",
        "Köktaş",
        "Kösemen",
        "Kürşad",
        "Kılıçbay",
        "Kınel",
        "Kırat",
        "Kırgız",
        "Kıvılcım",
        "Kızıl",
        "Kızıltunç",
        "Ledün",
        "Lutfi",
        "Lütfi",
        "Mahir",
        "Mahsun",
        "Maksur",
        "Mansurali",
        "Masar",
        "Mazlum",
        "Mecit",
        "Mefarettin",
        "Mehmed",
        "Mehmetzahir",
        "Melihcan",
        "Memili",
        "Mengi",
        "Mengüç",
        "Merdi",
        "Mertel",
        "Merzuk",
        "Mestur",
        "Metinkaya",
        "Mevlüt",
        "Meşhur",
        "Mihin",
        "Milay",
        "Mirbadin",
        "Mishat",
        "Monis",
        "Mucahit",
        "Muhammet",
        "Muhip",
        "Muhyettin",
        "Muktedir",
        "Muratcan",
        "Musafet",
        "Mutasım",
        "Mutluhan",
        "Muvaffak",
        "Möhsim",
        "Mücellib",
        "Müfit",
        "Mükramin",
        "Mülâyim",
        "Münif",
        "Mürit",
        "Müslum",
        "Müzekker",
        "Nabil",
        "Nafii",
        "Nakip",
        "Nas",
        "Nasuf",
        "Nayil",
        "Nazlim",
        "Nebih",
        "Necdat",
        "Necmettin",
        "Nehip",
        "Nerim",
        "Nesip",
        "Nevsal",
        "Nezihi",
        "Nihai",
        "Niyazi",
        "Noman",
        "Nural",
        "Nurcan",
        "Nuretdin",
        "Nurkan",
        "Nurullah",
        "Nuyan",
        "N˜zamett˜n",
        "Odkanlı",
        "Oganer",
        "Okanay",
        "Okbay",
        "Okgüçlü",
        "Okseven",
        "Oktüremiş",
        "Okyalaz",
        "Olca",
        "Oldağ",
        "Oliver",
        "Omaca",
        "Onat",
        "Ongay",
        "Onuker",
        "Onurcan",
        "Onursu",
        "Oranlı",
        "Orgün",
        "Ortak",
        "Oruç",
        "Otay",
        "Oymak",
        "Ozansü",
        "Oğulbaş",
        "Oğurata",
        "Oğuzman",
        "Paker",
        "Pehlil",
        "Pirahmet",
        "Rabih",
        "Rafih",
        "Rahmet",
        "Ramadan",
        "Rasul",
        "Razı",
        "Recepali",
        "Refik",
        "Remazan",
        "Resulcan",
        "Rezzak",
        "Risalet",
        "Rohat",
        "Ruhsat",
        "Rüknettin",
        "Rüşen",
        "Saba",
        "Sabih",
        "Sadat",
        "Sadittin",
        "Safet",
        "Sahir",
        "Sakip",
        "Salami",
        "Salkın",
        "Salurbay",
        "Sami",
        "Samurtay",
        "Sancak",
        "Sançar",
        "Sargın",
        "Sarpkın",
        "Sarıcabay",
        "Satrettin",
        "Savak",
        "Savni",
        "Saydam",
        "Sayin",
        "Sayrak",
        "Sayın",
        "Sağcan",
        "Sağıt",
        "Sebattin",
        "Seda",
        "Seha",
        "Selaheddin",
        "Selatin",
        "Seler",
        "Selvi",
        "Selâtin",
        "Semender",
        "Sencar",
        "Seracettin",
        "Serda",
        "Serezli",
        "Serhatmehmet",
        "Serol",
        "Server",
        "Sevdi",
        "Sevindik",
        "Seydo",
        "Seyfullah",
        "Seyithan",
        "Sezal",
        "Sezginbaş",
        "Seçme",
        "Sidki",
        "Siper",
        "Sittik",
        "Sonad",
        "Songurkan",
        "Soydaner",
        "Soykut",
        "Soyselçuk",
        "Suat",
        "Sudi",
        "Sulhi",
        "Sunel",
        "Suphi",
        "Sökmen",
        "Sözer",
        "Sücaettin",
        "Süha",
        "Sümeyye",
        "Süvari",
        "Sıla",
        "Sıylıhan",
        "Taciddin",
        "Tahir",
        "Talayer",
        "Tali",
        "Tamaydın",
        "Tanak",
        "Tanbay",
        "Tandoğdu",
        "Tanhan",
        "Tanpınar",
        "Tansev",
        "Tansığ",
        "Tanyolaç",
        "Tanır",
        "Tarancı",
        "Tartış",
        "Tatu",
        "Tayaydın",
        "Taygan",
        "Taylak",
        "Tayyip",
        "Taşar",
        "Taşkan",
        "Teber",
        "Tecimer",
        "Tekbay",
        "Tekecan",
        "Tekiner",
        "Teksoy",
        "Telim",
        "Temirhan",
        "Temizkal",
        "Temuçin",
        "Tenvir",
        "Terlan",
        "Tevs",
        "Tezcan",
        "Tezol",
        "Timurtaş",
        "Tiğin",
        "Toker",
        "Toktuğ",
        "Toköz",
        "Tolonbay",
        "Tonguç",
        "Topuz",
        "Torhan",
        "Toy",
        "Toğan",
        "Tulun",
        "Tunahan",
        "Tunguç",
        "Tunçboğa",
        "Tunçkılıç",
        "Turabi",
        "Turgut",
        "Tutkun",
        "Tuyuğ",
        "Tuğcan",
        "Tuğrulhan",
        "Tuğtaş",
        "Törel",
        "Tükelalp",
        "Tümer",
        "Tümkurt",
        "Türabi",
        "Türkalp",
        "Türkmen",
        "Tüzeer",
        "Tınal",
        "Ufukay",
        "Ulakbey",
        "Ulu",
        "Uludağ",
        "Uluman",
        "Ulutay",
        "Uluğbey",
        "Umman",
        "Umutcan",
        "Uraltay",
        "Urhan",
        "Us",
        "Ushan",
        "Utkucan",
        "Uygun",
        "Uzbay",
        "Uzsoy",
        "Uçan",
        "Uçbeyi",
        "Uğan",
        "Uğurkan",
        "Uğurtan",
        "Vafir",
        "Vahittin",
        "Vargın",
        "Vaysal",
        "Vedat",
        "Veis",
        "Velitdin",
        "Verim",
        "Vezat",
        "Vâlâ",
        "Yadigar",
        "Yahşikan",
        "Yalazabay",
        "Yalgın",
        "Yaltırak",
        "Yalın",
        "Yamin",
        "Yankı",
        "Yargı",
        "Yasan",
        "Yavuz",
        "Yayak",
        "Yazganalp",
        "Yağın",
        "Yağızkurt",
        "Yaşattin",
        "Yekda",
        "Yelesen",
        "Yeneral",
        "Yertan",
        "Yetişal",
        "Yigit",
        "Yilmaz",
        "Yolal",
        "Yoruç",
        "Yunt",
        "Yurdanur",
        "Yurtgüven",
        "Yurttaş",
        "Yönetmen",
        "Yücelen",
        "Yümun",
        "Yıldır",
        "Yılma",
        "Zahid",
        "Zamir",
        "Zekayi",
        "Zennun",
        "Zeynelabidin",
        "Zihni",
        "Ziyaettin",
        "Zoral",
        "Züfer",
        "Zülgarni",
        "Âdem",
        "Çakar",
        "Çakırca",
        "Çaltı",
        "Çamok",
        "Çapkan",
        "Çavuldur",
        "Çağa",
        "Çağdan",
        "Çağlasın",
        "Çağveren",
        "Çelem",
        "Çelikkan",
        "Çelikyürek",
        "Çerçi",
        "Çetinsu",
        "Çeviköz",
        "Çinerk",
        "Çokan",
        "Çopur",
        "Çoğay",
        "Çıdal",
        "Çıvgın",
        "Öge",
        "Ökkaş",
        "Öktürk",
        "Ömür",
        "Öncel",
        "Önel",
        "Öngen",
        "Önsal",
        "Örik",
        "Öryürek",
        "Över",
        "Özakan",
        "Özalpsan",
        "Özaslan",
        "Özbay",
        "Özbilek",
        "Özdal",
        "Özdil",
        "Özdoğdu",
        "Özel",
        "Özerdinç",
        "Özertem",
        "Özger",
        "Özgür",
        "Özinal",
        "Özkent",
        "Özkutlu",
        "Özlü",
        "Özokçu",
        "Özpınar",
        "Özsözlü",
        "Öztek",
        "Öztürk",
        "Özçam",
        "Özüdoğru",
        "Öğet",
        "Übeydullah",
        "Ülfet",
        "Ülküdeş",
        "Ümmet",
        "Ünek",
        "Ünlen",
        "Ünsever",
        "Ünübol",
        "Ürfettin",
        "Üsame",
        "Üstün",
        "Üzer",
        "Ğanim",
        "İbrahim",
        "İdiris",
        "İkiz",
        "İlalmış",
        "İlbek",
        "İldem",
        "İlgi",
        "İlim",
        "İlkim",
        "İlmafer",
        "İlsu",
        "İlteriş",
        "İmam",
        "İmren",
        "İnançlı",
        "İntihap",
        "İsak",
        "İsmet",
        "İvecen",
        "İyiyürek",
        "İzgü",
        "İşcan",
        "Şabettin",
        "Şafii",
        "Şahat",
        "Şahinbey",
        "Şahmettin",
        "Şali",
        "Şanlı",
        "Şavki",
        "Şefi",
        "Şehamet",
        "Şekim",
        "Şemsettin",
        "Şendoğan",
        "Şenkal",
        "Şerafeddin",
        "Şevket",
        "Şide",
        "Şinasi",
        "Şuayp",
        "Şükri",
    )

    first_names = first_names_male + first_names_female

    last_names = (
        "Yılmaz",
        "Yıldırım",
        "Türk",
        "Yorulmaz",
        "Erdoğan",
        "Çorlu",
        "Sakarya",
        "Demir",
        "Yaman",
        "Manço",
        "Aksu",
        "Akçay",
        "Akar",
        "Bilir",
        "Bilgin",
        "Yüksel",
        "Eraslan",
        "Aslan",
        "Arslan",
        "Hançer",
        "Hayrioğlu",
        "Şama",
        "Ergül",
        "Arsoy",
        "Kısakürek",
        "Gülen",
        "Seven",
        "Şafak",
        "Dumanlı",
        "Ertaş",
        "Güçlü",
        "Soylu",
        "Zorlu",
        "Fırat",
        "Duran",
        "Durmuş",
        "Durdu",
        "Zengin",
        "Tevetoğlu",
        "Mansız",
        "Şener",
        "Şensoy",
        "Ülker",
        "Tarhan",
        "Sezer",
        "Demirel",
        "Gül",
        "Korutürk",
        "İnönü",
        "Öcalan",
        "Çetin",
        "Sezgin",
        "Alemdar",
        "Karadeniz",
        "Akdeniz",
        "Bilge",
        "Akgündüz",
        "Akçay",
        "Çamurcuoğlu",
        "İhsanoğlu",
        "Akça",
    )

    prefixes_female = ("Bayan", "Dr.", "Uz.", "Öğr.", "Çev.", "Okt.", "Öğr.", "Öğr.", "Arş. Gör.", "Yrd. Doç.", "Dr.", "Doç.", "Prof.", "Av.")
    prefixes_male = ("Bay", "Dr.", "Uz.", "Öğr.", "Çev.", "Okt.", "Öğr.", "Öğr.", "Arş. Gör.", "Yrd. Doç.", "Dr.", "Doç.", "Prof.", "Av.")

    prefixes = prefixes_female + prefixes_male