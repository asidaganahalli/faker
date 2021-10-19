from .. import Provider as AddressProvider


class Provider(AddressProvider):

    street_prefixes = ('Av', 'Avenida', 'R.', 'Rua', 'Travessa', 'Largo', 'Alameda', 'Praça')

    city_formats = ('{{city_name}}',)
    street_name_formats = (
        '{{street_prefix}} {{last_name}}',
        '{{street_prefix}} {{first_name}} {{last_name}}',
        '{{street_prefix}} de {{last_name}}',
        '{{street_prefix}} {{place_name}}',
    )

    street_address_formats = (
        '{{street_name}}, {{building_number}}',
    )

    address_formats = (
        "{{street_address}}\n{{postcode}} {{city}}",
    )

    building_number_formats = ('S/N', '%', '%#', '%#', '%#', '%##')

    postcode_formats = ('####-###',)

    cities = (
        'Abrantes', 'Agualva-Cacém', 'Albufeira', 'Alcobaça', 'Alcácer do Sal',
        'Almada', 'Almeirim', 'Alverca do Ribatejo', 'Amadora', 'Amarante',
        'Amora', 'Anadia', 'Angra do Heroísmo', 'Aveiro', 'Barcelos',
        'Barreiro', 'Beja', 'Braga', 'Bragança', 'Caldas da Rainha', 'Caniço',
        'Cantanhede', 'Cartaxo', 'Castelo Branco', 'Chaves', 'Coimbra',
        'Costa da Caparica', 'Covilhã', 'Câmara de Lobos', 'Elvas',
        'Entroncamento', 'Ermesinde', 'Esmoriz', 'Espinho', 'Esposende',
        'Estarreja', 'Estremoz', 'Fafe', 'Faro', 'Felgueiras',
        'Figueira da Foz', 'Fiães', 'Freamunde', 'Funchal', 'Fundão', 'Fátima',
        'Gafanha da Nazaré', 'Gandra', 'Gondomar', 'Gouveia', 'Guarda',
        'Guimarães', 'Horta', 'Lagoa', 'Lagos', 'Lamego', 'Leiria', 'Lisboa',
        'Lixa', 'Loulé', 'Loures', 'Lourosa', 'Macedo de Cavaleiros', 'Maia',
        'Mangualde', 'Marco de Canaveses', 'Marinha Grande', 'Matosinhos',
        'Mealhada', 'Miranda do Douro', 'Mirandela', 'Montemor-o-Novo',
        'Montijo', 'Moura', 'Mêda', 'Odivelas', 'Olhão', 'Oliveira de Azeméis',
        'Oliveira do Bairro', 'Oliveira do Hospital', 'Ourém', 'Ovar',
        'Paredes', 'Paços de Ferreira', 'Penafiel', 'Peniche', 'Peso da Régua',
        'Pinhel', 'Pombal', 'Ponta Delgada', 'Ponte de Sor', 'Portalegre',
        'Portimão', 'Porto', 'Porto Santo', 'Praia da Vitória',
        'Póvoa de Santa Iria', 'Póvoa de Varzim', 'Quarteira', 'Queluz',
        'Rebordosa', 'Reguengos de Monsaraz', 'Ribeira Grande', 'Rio Maior',
        'Rio Tinto', 'Sabugal', 'Sacavém', 'Santa Comba Dão', 'Santa Cruz',
        'Santa Maria da Feira', 'Santana', 'Santarém', 'Santiago do Cacém',
        'Santo Tirso', 'Seia', 'Seixal', 'Serpa', 'Setúbal', 'Silves', 'Sines',
        'Sintra', 'São João da Madeira', 'São Mamede de Infesta',
        'São Salvador de Lordelo', 'Tarouca', 'Tavira', 'Tomar', 'Tondela',
        'Torres Novas', 'Torres Vedras', 'Trancoso', 'Trofa', 'Valbom',
        'Vale de Cambra', 'Valongo', 'Valpaços', 'Vendas Novas',
        'Viana do Castelo', 'Vila Franca de Xira', 'Vila Nova de Famalicão',
        'Vila Nova de Foz Côa', 'Vila Nova de Gaia', 'Vila Nova de Santo André',
        'Vila Real', 'Vila Real de Santo António', 'Vila do Conde', 'Viseu',
        'Vizela', 'Évora', 'Ílhavo',
    )

    countries = (
        'Afeganistão', 'África do Sul', 'Akrotiri', 'Albânia', 'Alemanha',
        'Andorra', 'Angola', 'Anguila', 'Antárctida', 'Antígua e Barbuda',
        'Antilhas Neerlandesas', 'Arábia Saudita', 'Arctic Ocean', 'Argélia',
        'Argentina', 'Arménia', 'Aruba', 'Ashmore and Cartier Islands',
        'Atlantic Ocean', 'Austrália', 'Áustria', 'Azerbaijão', 'Baamas',
        'Bangladeche', 'Barbados', 'Barém', 'Bélgica', 'Belize', 'Benim',
        'Bermudas', 'Bielorrússia', 'Birmânia', 'Bolívia',
        'Bósnia e Herzegovina', 'Botsuana', 'Brasil', 'Brunei', 'Bulgária',
        'Burquina Faso', 'Burúndi', 'Butão', 'Cabo Verde', 'Camarões',
        'Camboja', 'Canadá', 'Catar', 'Cazaquistão', 'Chade', 'Chile', 'China',
        'Chipre', 'Clipperton Island', 'Colômbia', 'Comores',
        'Congo-Brazzaville', 'Congo-Kinshasa', 'Coral Sea Islands',
        'Coreia do Norte', 'Coreia do Sul', 'Costa do Marfim', 'Costa Rica',
        'Croácia', 'Cuba', 'Dhekelia', 'Dinamarca', 'Domínica', 'Egipto',
        'Emiratos Árabes Unidos', 'Equador', 'Eritreia', 'Eslováquia',
        'Eslovénia', 'Espanha', 'Estados Unidos', 'Estónia', 'Etiópia', 'Faroé',
        'Fiji', 'Filipinas', 'Finlândia', 'França', 'Gabão', 'Gâmbia', 'Gana',
        'Gaza Strip', 'Geórgia', 'Geórgia do Sul e Sandwich do Sul',
        'Gibraltar', 'Granada', 'Grécia', 'Gronelândia', 'Guame', 'Guatemala',
        'Guernsey', 'Guiana', 'Guiné', 'Guiné Equatorial', 'Guiné-Bissau',
        'Haiti', 'Honduras', 'Hong Kong', 'Hungria', 'Iémen', 'Ilha Bouvet',
        'Ilha do Natal', 'Ilha Norfolk', 'Ilhas Caimão', 'Ilhas Cook',
        'Ilhas dos Cocos', 'Ilhas Falkland', 'Ilhas Heard e McDonald',
        'Ilhas Marshall', 'Ilhas Salomão', 'Ilhas Turcas e Caicos',
        'Ilhas Virgens Americanas', 'Ilhas Virgens Britânicas', 'Índia',
        'Indian Ocean', 'Indonésia', 'Irão', 'Iraque', 'Irlanda', 'Islândia',
        'Israel', 'Itália', 'Jamaica', 'Jan Mayen', 'Japão', 'Jersey', 'Jibuti',
        'Jordânia', 'Kuwait', 'Laos', 'Lesoto', 'Letónia', 'Líbano', 'Libéria',
        'Líbia', 'Listenstaine', 'Lituânia', 'Luxemburgo', 'Macau', 'Macedónia',
        'Madagáscar', 'Malásia', 'Malávi', 'Maldivas', 'Mali', 'Malta',
        'Man, Isle of', 'Marianas do Norte', 'Marrocos', 'Maurícia',
        'Mauritânia', 'Mayotte', 'México', 'Micronésia', 'Moçambique',
        'Moldávia', 'Mónaco', 'Mongólia', 'Monserrate', 'Montenegro', 'Mundo',
        'Namíbia', 'Nauru', 'Navassa Island', 'Nepal', 'Nicarágua', 'Níger',
        'Nigéria', 'Niue', 'Noruega', 'Nova Caledónia', 'Nova Zelândia', 'Omã',
        'Pacific Ocean', 'Países Baixos', 'Palau', 'Panamá', 'Papua-Nova Guiné',
        'Paquistão', 'Paracel Islands', 'Paraguai', 'Peru', 'Pitcairn',
        'Polinésia Francesa', 'Polónia', 'Porto Rico', 'Portugal', 'Quénia',
        'Quirguizistão', 'Quiribáti', 'Reino Unido',
        'República Centro-Africana', 'República Checa', 'República Dominicana',
        'Roménia', 'Ruanda', 'Rússia', 'Salvador', 'Samoa', 'Samoa Americana',
        'Santa Helena', 'Santa Lúcia', 'São Cristóvão e Neves', 'São Marinho',
        'São Pedro e Miquelon', 'São Tomé e Príncipe',
        'São Vicente e Granadinas', 'Sara Ocidental', 'Seicheles', 'Senegal',
        'Serra Leoa', 'Sérvia', 'Singapura', 'Síria', 'Somália',
        'Southern Ocean', 'Spratly Islands', 'Sri Lanca', 'Suazilândia',
        'Sudão', 'Suécia', 'Suíça', 'Suriname', 'Svalbard e Jan Mayen',
        'Tailândia', 'Taiwan', 'Tajiquistão', 'Tanzânia',
        'Território Britânico do Oceano Índico',
        'Territórios Austrais Franceses', 'Timor Leste', 'Togo', 'Tokelau',
        'Tonga', 'Trindade e Tobago', 'Tunísia', 'Turquemenistão', 'Turquia',
        'Tuvalu', 'Ucrânia', 'Uganda', 'União Europeia', 'Uruguai',
        'Usbequistão', 'Vanuatu', 'Vaticano', 'Venezuela', 'Vietname',
        'Wake Island', 'Wallis e Futuna', 'West Bank', 'Zâmbia', 'Zimbabué',
    )

    # From https://pt.wikipedia.org/wiki/Distritos_de_Portugal
    distritos = (
        'Aveiro', 'Beja', 'Braga', 'Bragança', 'Castelo Branco', 'Coimbra',
        'Évora', 'Faro', 'Guarda', 'Leiria', 'Lisboa', 'Portalegre', 'Porto',
        'Santarém', 'Setúbal', 'Viana do Castelo', 'Vila Real', 'Viseu',
    )

    # From https://pt.wikipedia.org/wiki/Lista_de_concelhos_por_NUTS,_distritos_e_ilhas
    concelhos = (
        "Águeda", "Aguiar da Beira", "Alandroal", "Albergaria-a-Velha", "Albufeira",
        "Alcácer do Sal", "Alcanena", "Alcobaça", "Alcochete", "Alcoutim", "Alenquer",
        "Alfândega da Fé", "Alijó", "Aljezur", "Aljustrel", "Almada", "Almeida", "Almeirim",
        "Almodôvar", "Alpiarça", "Alter do Chão", "Alvaiázere", "Alvito", "Amadora",
        "Amarante", "Amares", "Anadia", "Angra do Heroísmo", "Ansião",
        "Arcos de Valdevez", "Arganil", "Armamar", "Arouca", "Arraiolos",
        "Arronches", "Arruda dos Vinhos", "Aveiro", "Avis", "Azambuja",
        "Baião", "Barcelos", "Barrancos", "Barreiro", "Batalha", "Beja",
        "Belmonte", "Benavente", "Bombarral", "Borba", "Boticas", "Braga",
        "Bragança", "Cabeceiras de Basto", "Cadaval", "Caldas da Rainha",
        "Calheta (R.A.A.)", "Calheta (R.A.M.)", "Câmara de Lobos", "Caminha",
        "Campo Maior", "Cantanhede", "Carrazeda de Ansiães", "Carregal do Sal",
        "Cartaxo", "Cascais", "Castanheira de Pêra", "Castelo Branco",
        "Castelo de Paiva", "Castelo de Vide", "Castro Daire", "Castro Marim",
        "Castro Verde", "Celorico da Beira", "Celorico de Basto", "Chamusca",
        "Chaves", "Cinfães", "Coimbra", "Condeixa-a-Nova", "Constância",
        "Coruche", "Corvo", "Covilhã", "Crato", "Cuba", "Elvas",
        "Entroncamento", "Espinho", "Esposende", "Estarreja", "Estremoz",
        "Évora", "Fafe", "Faro", "Felgueiras", "Ferreira do Alentejo",
        "Ferreira do Zêzere", "Figueira da Foz", "Figueira de Castelo Rodrigo",
        "Figueiró dos Vinhos", "Fornos de Algodres", "Freixo de Espada à Cinta",
        "Fronteira", "Funchal", "Fundão", "Gavião", "Góis", "Golegã", "Gondomar",
        "Gouveia", "Grândola", "Guarda", "Guimarães", "Horta", "Idanha-a-Nova",
        "Ílhavo", "Lagoa", "Lagoa (R.A.A)", "Lagos", "Lajes das Flores",
        "Lajes do Pico", "Lamego", "Leiria", "Lisboa", "Loulé", "Loures",
        "Lourinhã", "Lousã", "Lousada", "Mação", "Macedo de Cavaleiros",
        "Machico", "Madalena", "Mafra", "Maia", "Mangualde", "Manteigas",
        "Marco de Canaveses", "Marinha Grande", "Marvão", "Matosinhos",
        "Mealhada", "Meda", "Melgaço", "Mértola", "Mesão Frio", "Mira",
        "Miranda do Corvo", "Miranda do Douro", "Mirandela", "Mogadouro",
        "Moimenta da Beira", "Moita", "Monção", "Monchique", "Mondim de Basto",
        "Monforte", "Montalegre", "Montemor-o-Novo", "Montemor-o-Velho", "Montijo",
        "Mora", "Mortágua", "Moura", "Mourão", "Murça", "Murtosa", "Nazaré",
        "Nelas", "Nisa", "Nordeste", "Óbidos", "Odemira", "Odivelas", "Oeiras",
        "Oleiros", "Olhão", "Oliveira de Azeméis", "Oliveira de Frades",
        "Oliveira do Bairro", "Oliveira do Hospital", "Ourém", "Ourique", "Ovar",
        "Paços de Ferreira", "Palmela", "Pampilhosa da Serra", "Paredes",
        "Paredes de Coura", "Pedrógão Grande", "Penacova", "Penafiel",
        "Penalva do Castelo", "Penamacor", "Penedono", "Penela", "Peniche",
        "Peso da Régua", "Pinhel", "Pombal", "Ponta Delgada", "Ponta do Sol",
        "Ponte da Barca", "Ponte de Lima", "Ponte de Sor", "Portalegre", "Portel",
        "Portimão", "Porto", "Porto de Mós", "Porto Moniz", "Porto Santo",
        "Povoação", "Póvoa de Lanhoso", "Póvoa de Varzim", "Proença-a-Nova",
        "Redondo", "Reguengos de Monsaraz", "Resende", "Ribeira Brava",
        "Ribeira de Pena", "Ribeira Grande", "Rio Maior", "Sabrosa",
        "Sabugal", "Salvaterra de Magos", "Santa Comba Dão", "Santa Cruz",
        "Santa Cruz da Graciosa", "Santa Cruz das Flores", "Santa Maria da Feira",
        "Santa Marta de Penaguião", "Santana", "Santarém", "Santiago do Cacém",
        "Santo Tirso", "São Brás de Alportel", "São João da Madeira",
        "São João da Pesqueira", "São Pedro do Sul", "São Roque do Pico",
        "São Vicente", "Sardoal", "Sátão", "Seia", "Seixal", "Sernancelhe",
        "Serpa", "Sertã", "Sesimbra", "Setúbal", "Sever do Vouga", "Silves",
        "Sines", "Sintra", "Sobral de Monte Agraço", "Soure", "Sousel",
        "Tábua", "Tabuaço", "Tarouca", "Tavira", "Terras de Bouro",
        "Tomar", "Tondela", "Torre de Moncorvo", "Torres Novas",
        "Torres Vedras", "Trancoso", "Trofa", "Vagos", "Vale de Cambra",
        "Valença", "Valongo", "Valpaços", "Velas", "Vendas Novas",
        "Viana do Alentejo", "Viana do Castelo", "Vidigueira",
        "Vieira do Minho", "Vila da Praia da Vitória", "Vila de Rei",
        "Vila do Bispo", "Vila do Conde", "Vila do Porto", "Vila Flor",
        "Vila Franca de Xira", "Vila Franca do Campo", "Vila Nova da Barquinha",
        "Vila Nova de Cerveira", "Vila Nova de Famalicão", "Vila Nova de Foz Côa",
        "Vila Nova de Gaia", "Vila Nova de Paiva", "Vila Nova de Poiares",
        "Vila Pouca de Aguiar", "Vila Real", "Vila Real de Santo António",
        "Vila Velha de Ródão", "Vila Verde", "Vila Viçosa", "Vimioso",
        "Vinhais", "Viseu", "Vizela", "Vouzela",
    )

    # From https://pt.wikipedia.org/wiki/Lista_de_freguesias_de_Portugal
    freguesias = [
        "Abrantes", "Águeda", "Aguiar da Beira", "Alandroal",
        "Albergaria-a-Velha", "Albufeira", "Alcácer do Sal", "Alcanena",
        "Alcobaça", "Alcochete", "Alcoutim", "Alenquer", "Alfândega da Fé",
        "Alijó", "Aljezur", "Aljustrel", "Almada", "Almeida", "Almeirim",
        "Almodôvar", "Alpiarça", "Alter do Chão", "Alvaiázere", "Alvito",
        "Amadora", "Amarante", "Amares", "Anadia", "Angra do Heroísmo",
        "Ansião", "Arcos de Valdevez", "Arganil", "Armamar", "Arouca",
        "Arraiolos", "Arronches", "Arruda dos Vinhos", "Aveiro", "Avis",
        "Azambuja", "Baião", "Barcelos", "Barrancos", "Barreiro", "Batalha",
        "Beja", "Belmonte", "Benavente", "Bombarral", "Borba", "Boticas",
        "Braga", "Bragança", "Cabeceiras de Basto", "Cadaval",
        "Caldas da Rainha", "Calheta (Açores)", "Calheta (Madeira)",
        "Câmara de Lobos", "Caminha", "Campo Maior", "Cantanhede",
        "Carrazeda de Ansiães", "Carregal do Sal", "Cartaxo", "Cascais",
        "Castanheira de Pêra", "Castelo Branco", "Castelo de Paiva",
        "Castelo de Vide", "Castro Daire", "Castro Marim", "Castro Verde",
        "Celorico da Beira", "Celorico de Basto", "Chamusca", "Chaves",
        "Cinfães", "Coimbra", "Condeixa-a-Nova", "Constância", "Coruche",
        "Corvo", "Covilhã", "Crato", "Cuba", "Elvas", "Entroncamento",
        "Espinho", "Esposende", "Estarreja", "Estremoz", "Évora", "Fafe",
        "Faro", "Felgueiras", "Ferreira do Alentejo", "Ferreira do Zêzere",
        "Figueira da Foz", "Figueira de Castelo Rodrigo",
        "Figueiró dos Vinhos", "Fornos de Algodres",
        "Freixo de Espada à Cinta", "Fronteira", "Funchal", "Fundão", "Gavião",
        "Góis", "Golegã", "Gondomar", "Gouveia", "Grândola", "Guarda",
        "Guimarães", "Horta", "Idanha-a-Nova", "Ílhavo", "Lagoa",
        "Lagoa (Açores)", "Lagos", "Lajes das Flores", "Lajes do Pico",
        "Lamego", "Leiria", "Lisboa", "Loulé", "Loures", "Lourinhã", "Lousã",
        "Lousada", "Mação", "Macedo de Cavaleiros", "Machico", "Madalena",
        "Mafra", "Maia", "Mangualde", "Manteigas", "Marco de Canaveses",
        "Marinha Grande", "Marvão", "Matosinhos", "Mealhada", "Mêda",
        "Melgaço", "Mértola", "Mesão Frio", "Mira", "Miranda do Corvo",
        "Miranda do Douro", "Mirandela", "Mogadouro", "Moimenta da Beira",
        "Moita", "Monção", "Monchique", "Mondim de Basto", "Monforte",
        "Montalegre", "Montemor-o-Novo", "Montemor-o-Velho", "Montijo",
        "Mora", "Mortágua", "Moura", "Mourão", "Murça", "Murtosa", "Nazaré",
        "Nelas", "Nisa", "Nordeste", "Óbidos", "Odemira", "Odivelas",
        "Oeiras", "Oleiros", "Olhão", "Oliveira de Azeméis",
        "Oliveira de Frades", "Oliveira do Bairro", "Oliveira do Hospital",
        "Ourém", "Ourique", "Ovar", "Paços de Ferreira", "Palmela",
        "Pampilhosa da Serra", "Paredes", "Paredes de Coura", "Pedrógão Grande",
        "Penacova", "Penafiel", "Penalva do Castelo", "Penamacor", "Penedono",
        "Penela", "Peniche", "Peso da Régua", "Pinhel", "Pombal",
        "Ponta Delgada", "Ponta do Sol", "Ponte da Barca", "Ponte de Lima",
        "Ponte de Sor", "Portalegre", "Portel", "Portimão", "Porto",
        "Porto de Mós", "Porto Moniz", "Porto Santo", "Póvoa de Lanhoso",
        "Póvoa de Varzim", "Povoação", "Praia da Vitória", "Proença-a-Nova",
        "Redondo", "Reguengos de Monsaraz", "Resende", "Ribeira Brava",
        "Ribeira de Pena", "Ribeira Grande", "Rio Maior", "Sabrosa", "Sabugal",
        "Salvaterra de Magos", "Santa Comba Dão", "Santa Cruz",
        "Santa Cruz da Graciosa", "Santa Cruz das Flores",
        "Santa Maria da Feira", "Santa Marta de Penaguião", "Santana",
        "Santarém", "Santiago do Cacém", "Santo Tirso", "São Brás de Alportel",
        "São João da Madeira", "São João da Pesqueira", "São Pedro do Sul",
        "São Roque do Pico", "São Vicente (Madeira)", "Sardoal", "Sátão",
        "Seia", "Seixal", "Sernancelhe", "Serpa", "Sertã", "Sesimbra",
        "Setúbal", "Sever do Vouga", "Silves", "Sines", "Sintra",
        "Sobral de Monte Agraço", "Soure", "Sousel", "Tábua", "Tabuaço",
        "Tarouca", "Tavira", "Terras de Bouro", "Tomar", "Tondela",
        "Torre de Moncorvo", "Torres Novas", "Torres Vedras", "Trancoso",
        "Trofa", "Vagos", "Vale de Cambra", "Valença", "Valongo", "Valpaços",
        "Velas", "Vendas Novas", "Viana do Alentejo", "Viana do Castelo",
        "Vidigueira", "Vieira do Minho", "Vila de Rei", "Vila do Bispo",
        "Vila do Conde", "Vila do Porto", "Vila Flor", "Vila Franca de Xira",
        "Vila Franca do Campo", "Vila Nova da Barquinha",
        "Vila Nova de Cerveira", "Vila Nova de Famalicão",
        "Vila Nova de Foz Côa", "Vila Nova de Gaia", "Vila Nova de Paiva",
        "Vila Nova de Poiares", "Vila Pouca de Aguiar", "Vila Real",
        "Vila Real de Santo António", "Vila Velha de Ródão", "Vila Verde",
        "Vila Viçosa", "Vimioso", "Vinhais", "Viseu", "Vizela", "Vouzela",
    ]

    # from https://pt.wikipedia.org/wiki/Lista_de_arruamentos_de_Lisboa
    # and https://pt.wikipedia.org/wiki/Lista_de_arruamentos_do_Porto
    places = (
        "da Igreja", "António Sérgio", "Cardeal Cerejeira", "Coronel Marques Júnior", "da Encarnação",
        "da Música", "da Quinta de Santo António", "da Universidade", "das Comunidades Portuguesas",
        "das Linhas de Torres", "de Santo António dos Capuchos", "do Beato", "Dom Afonso Henriques",
        "dos Oceanos", "dos Pinheiros", "Edgar Cardoso", "Mahatma Gandhi",
        "Manuel Ricardo Espírito Santo", "Padre Álvaro Proença", "Roentgen", "da Boavista",
        "da Cova da Moura", "das Conchas", "de Caselas", "de São Francisco",
        "do Carvalhão", "do Longo", "do Penalva", "do Varejão",
        "dos Moinhos", "da Conceição", "das Portas do Mar", "de Jesus",
        "do Evaristo", "do Rosário", "Escuro", "Grande de Cima",
        "Areeiro", "Campolide", "Madrid", "Paris (Nascente)",
        "Paris (Poente)", "Roma", "Sabugosa", "Novo (à Travessa das Águas Boas)",
        "da Ponte da Lama", "da Praia da Galé", "do Duro", "dos Ferreiros",
        "das Rolas", "da Lingueta", "das Naus", "do Olival",
        "do Sodré", "dos Argonautas", "Português", "da Figueira",
        "de Santo Estêvão", "de São Lourenço", "de São Miguel", "do Tijolo",
        "dos Olivais", "da Feiteira", "da Rainha", "da Raposa",
        "das Andorinhas", "das Cegonhas", "das Gaivotas ao Parque das Nações", "de Baixo da Penha",
        "de Palma de Cima", "do Alto do Varejão", "do Arboreto", "dos Estorninhos",
        "dos Flamingos", "dos Melros", "dos Pardais", "dos Pinheiros ao Parque das Nações",
        "dos Rouxinóis", "Velho do Outeiro", "das Amoreiras", "das Cebolas",
        "de Santa Clara", "dos Mártires da Pátria", "Grande", "Pequeno",
        "de Campolide", "da Graça", "de Colares", "Norte do Bairro da Encarnação",
        "Sul do Bairro da Encarnação", "da Torrinha", "do Castelo", "de Santa Helena",
        "da Sé", "das Bolas", "das Chagas", "José António Marques",
        "do Monte", "Gerais", "D. Carlos I ao Parque das Nações", "Adão Barata",
        "Alfredo Keil", "Alice Cruz", "Amália Rodrigues", "Amélia Carvalheira",
        "Amnistia Internacional", "Augusto Monjardino", "Bento Martins", "das Nações",
        "Ducla Soares", "Eduardo Prado Coelho", "Elisa Baptista de Sousa Pedroso", "Fernanda de Castro",
        "Fernando Pessa", "Ferreira de Mira", "Garcia de Orta ao Parque das Nações", "Irmã Lúcia",
        "Jorge Luis Borges", "Luís Ferreira", "Maria da Luz Ponces de Carvalho", "Maria de Lourdes Sá Teixeira",
        "Maria José Moura", "Mário Ruivo", "Mário Soares", "9 de Abril",
        "Prof. António de Sousa Franco", "Prof. Francisco Caldeira Cabral", "Pulido Garcia", "Tristão da Silva",
        "Ribeirinhos", "Sophia de Mello Breyner Andresen", "do Mirante", "do Alto de São João",
        "General Afonso Botelho", "Eduardo VII de Inglaterra", "Silva Porto", "Artur Agostinho",
        "da Ilha dos Amores", "da Nau Catrineta", "da Vila Expo", "das Âncoras",
        "das Fragatas", "das Garças", "das Gáveas ao Parque das Nações", "das Musas",
        "das Tágides", "de Neptuno", "de Ulisses", "do Adamastor",
        "do Amazonas", "do Báltico", "do Campo da Bola", "do Cantábrico",
        "do Levante", "do Parque", "do Ródano", "do Sapal",
        "do Tejo", "do Trancão", "dos Aventureiros", "dos Cruzados",
        "dos Fenícios", "dos Heróis do Mar", "dos Jacarandás", "dos Mastros",
        "dos Navegadores", "João Jayme Faria Affonso", "Júlio Verne", "Afonso de Albuquerque",
        "da Cruz", "da Galega", "das Canas", "das Galeotas ao Parque das Nações",
        "das Pirogas", "de Dom Fradique", "do Carrasco", "do Peneireiro",
        "do Pimenta", "do Pinzaleiro", "do Seabra", "do Sequeiro",
        "do Sextante", "do Tronco", "dos Escaleres", "do Borratém",
        "do Mar", "Adolfo Ayala", "Cuf", "da Quinta de São João Baptista",
        "da Quinta do Guarda-Mor", "da Rua Duque de Palmela", "das Torres do Restelo", "do Chinquilho",
        "Fernando Valle", "Maestro Ivo Cruz", "Prof. António José Saraiva", "Professor Gonçalves Ferreira",
        "Professor José Conde", "Teófilo Ferreira", "das Necessidades", "do Mercado",
        "dos Anjos", "do Conde de Óbidos", "de Palma", "Almirante Pinheiro de Azevedo",
        "António Dias Lourenço", "Coronel Vítor Alves", "da Expo 98", "das Olaias",
        "das Oliveiras", "de Pina Manique", "dos Vice-reis", "Matilde Bensaúde",
        "Nelson Mandela", "Pupilos do Exército", "República Argentina", "República da Colômbia",
        "Visconde de Alvalade", "do Barcal", "do Calhau", "de São Vicente",
        "das Ondas", "dos Corvos", "Feia", "Arquitecto Carlos Ramos",
        "das Antas", "das Fontainhas", "de 25 de Abril", "de Aquilino Ribeiro",
        "de Basílio Teles", "de Cartes", "de Cláudio Carneiro", "de Eça de Queirós",
        "de Manuel d'Arriaga", "do Dr. António Macedo", "do Dr. Fernando de Azeredo Antas", "do Prof. Hernâni Monteiro",
        "do Prof. Ruy Luís Gomes", "dos Capitães de Abril", "25 de Abril", "da Associação Empresarial de Portugal",
        "da França", "de Camilo", "de D. Afonso Henriques", "de D. Carlos I",
        "de D. João II", "de Fernão de Magalhães", "de Fontes Pereira de Melo", "de Gustavo Eiffel",
        "de Montevideu", "de Nun'Álvares Pereira", "de Paiva Couceiro", "de Rodrigues de Freitas",
        "de Sidónio Pais", "de Vasco da Gama", "de Vímara Peres", "do Bessa",
        "do Brasil (Porto)", "do Conselho da Europa", "do Dr. Antunes Guimarães", "do Marechal Gomes da Costa",
        "dos Aliados", "dos Combatentes da Grande Guerra", "Flor da Rosa", "José Domingues dos Santos",
        "da Agra do Amial", "da Fonte da Moura", "da Pasteleira", "da Rainha D. Leonor",
        "de Costa Cabral", "de Francos", "de Manuel Cardoso Agrelos", "de Pio XII",
        "de Ramalde", "de São João de Deus", "de São Roque da Lameira", "de São Vicente de Paulo",
        "de Santo Eugénio", "do Aleixo", "do Bom Sucesso", "do Carvalhido",
        "do Cerco do Porto", "do Dr. Nuno Pinheiro Torres", "do Falcão", "do Lagarteiro",
        "do Leal", "do Outeiro", "do Regado", "do Viso",
        "Herculano", "Central", "da Bela Vista", "da Beneditina",
        "da Senhora da Luz", "de Bonjóia", "de Carreiras", "de Passos Manuel",
        "de S. João da Foz", "de S. Macário", "de S. Marçal", "do Arrabalde",
        "do Campo", "do Campo Alegre", "do Machado", "do Meiral",
        "do Paço", "do Pedregulho", "do Preto", "de Baixo",
        "de Cima", "da Alfândega", "da Estiva", "da Ribeira",
        "das Pedras", "do Bicalho", "dos Guindais", "da Arrábida",
        "da Boa Viagem", "da Póvoa", "da Ranha", "das Carquejeiras",
        "das Laranjeiras", "das Virtudes", "de Chaves de Oliveira", "de D. Pedro Pitões",
        "de Godim", "de João do Carmo", "de Maceda", "de Marques Marinho",
        "de Monchique", "de Nova Sintra", "de São Pedro", "de Serrúbia",
        "de Sobre-o-Douro", "de Vandoma", "do Calvário", "do Carregal",
        "do Forno Velho", "do Monte da Lapa", "do Monte de S. João", "do Ouro",
        "do Rego Lameiro", "dos Ingleses", "da Fonte de Cima", "das Congostas",
        "da Asprela", "de Vinte e Quatro de Agosto", "do Rou", "de Antero de Quental",
        "de Estêvão Vasconcelos", "de Viterbo de Campos", "do Dr. Manuel Laranjeira",
        "Carolina Michaelis de Vasconcelos", "da Vitória", "das Sereias", "das Verdades", "de S. Francisco de Borja",
        "do Adro", "do Barredo", "do Caminho Novo", "do Cidral de Baixo",
        "do Cidral de Cima", "do Codeçal", "do Colégio", "do Monte Cativo",
        "do Monte dos Judeus", "do Pinheiro", "do Recanto", "do Roleto",
        "dos Armazéns", "do Molhe", "da Circunvalação", "de Gondomar",
        "Nacional 108", "Nacional 209", "de Moradias Populares do Eng.º Machado Vaz",
        "de Moradais Populares do Carriçal", "de Antero de Figueiredo", "de Arnaldo Gama", "de Belém",
        "de Carrilho Videira", "de Guedes de Oliveira", "de João Chagas", "de Marques de Oliveira", "de Teófilo Braga",
        "do Moreda", "do Passeio Alegre", "Machado de Asis", "Severo Portela",
        "da Foz", "do Bolhão", "dos Bacalhoeiros", "da Luz",
        "do Seminário", "S. Bartolomeu", "de S. Lázaro", "das Escadas do Monte dos Judeus",
        "das Japoneiras", "de S. Salvador", "do Bonjardim", "de Luiz I",
        "de Maria Pia", "do Freixo", "do Carvão", "da Banda de Ramalde",
        "da Cidade da Praia", "das Mimosas", "de Adelino Amaro da Costa", "de Augusto Gomes",
        "de Bernarda Ferreira Lacerda", "de Eduardo Soares", "de Francisco Borges", "de Irene de Castro",
        "de João Augusto Ribeiro", "de José Régio", "de José Serra", "de Luís António Verney",
        "de Públia Hortênsia", "de Ribeiro Sanches", "de S. Mamede", "do Dr. Jaime Cortesão",
        "do Maestro Afonso Valentim", "do Maestro Resende Dias", "do Mestre de Aviz", "do Prof. Egas Moniz",
        "Egito Gonçalves", "Ernesto Veiga de Oliveira", "João Glama", "José Luís Nunes",
        "Manuel Gonçalves Moreira", "Artur Cupertino de Miranda", "Associação Empresarial de Portugal",
        "Manuel Pinto de Azevedo Júnior", "Goelas de Pau", "de Cintura Interna", "do Almirante Gago Coutinho",
        "do Castelo do Queijo", "Futebol Clube do Porto", "Panorâmica", "Panorâmica Edgar Cardoso",
        "de Gonçalo Cristóvão", "do Cais das Pedras", "da Aldeia", "da Baleia", "da Bouça",
        "da Carvalhosa", "da Companhia", "da Ilha do Ferro", "da Pedreira", "da Senhora da Lapa", "das Andrezas",
        "de Grijó", "de Lamas", "de S. Brás", "de Santana", "do Anjo", "do Anjo da Guarda",
        "do Buraco", "do José da Mestra", "do Monte da Pena", "do Picoto", "do Sobreirinho",
    )

    def street_prefix(self) -> str:
        """
        :example 'Rua'
        """
        return self.random_element(self.street_prefixes)

    def city_name(self) -> str:
        """
        :example 'Amora'
        """
        return self.random_element(self.cities)

    def administrative_unit(self) -> str:
        """
        :example 'Bragança'
        """
        return self.random_element(self.distritos)

    distrito = administrative_unit

    def concelho(self) -> str:
        """
        :example 'Tondela'
        """
        return self.random_element(self.concelhos)

    def freguesia(self) -> str:
        """
        :example 'Miranda do Douro'
        """
        return self.random_element(self.freguesias)

    def place_name(self) -> str:
        """
        :example "do Pombal"
        """
        return self.random_element(self.places)
