# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{prefix}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{first_name_female}}-{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}} {{prefix}} {{last_name}}',
    )

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{prefix}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{first_name_male}}-{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}} {{prefix}} {{last_name}}',
    )

    formats = formats_male + formats_female

    first_names_male = (
        'Adrien',
        'Aimé',
        'Alain',
        'Alexandre',
        'Alfred',
        'Alphonse',
        'André',
        'Antoine',
        'Arthur',
        'Auguste',
        'Augustin',
        'Benjamin',
        'Benoît',
        'Bernard',
        'Bertrand',
        'Charles',
        'Christophe',
        'Daniel',
        'David',
        'Denis',
        'Édouard',
        'Émile',
        'Emmanuel',
        'Éric',
        'Étienne',
        'Eugène',
        'François',
        'Franck',
        'Frédéric',
        'Gabriel',
        'Georges',
        'Gérard',
        'Gilbert',
        'Gilles',
        'Grégoire',
        'Guillaume',
        'Guy',
        'William',
        'Henri',
        'Honoré',
        'Hugues',
        'Isaac',
        'Jacques',
        'Jean',
        'Jérôme',
        'Joseph',
        'Jules',
        'Julien',
        'Laurent',
        'Léon',
        'Louis',
        'Luc',
        'Lucas',
        'Marc',
        'Marcel',
        'Martin',
        'Matthieu',
        'Maurice',
        'Michel',
        'Nicolas',
        'Noël',
        'Olivier',
        'Patrick',
        'Paul',
        'Philippe',
        'Pierre',
        'Raymond',
        'Rémy',
        'René',
        'Richard',
        'Robert',
        'Roger',
        'Roland',
        'Sébastien',
        'Stéphane',
        'Théodore',
        'Théophile',
        'Thibaut',
        'Thibault',
        'Thierry',
        'Thomas',
        'Timothée',
        'Tristan',
        'Victor',
        'Vincent',
        'Xavier',
        'Yves',
        'Zacharie')

    first_names_female = (
        'Adélaïde',
        'Adèle',
        'Adrienne',
        'Agathe',
        'Agnès',
        'Aimée',
        'Alexandrie',
        'Alix',
        'Alexandria',
        'Alex',
        'Alice',
        'Amélie',
        'Anaïs',
        'Anastasie',
        'Andrée',
        'Anne',
        'Anouk',
        'Antoinette',
        'Arnaude',
        'Astrid',
        'Audrey',
        'Aurélie',
        'Aurore',
        'Bernadette',
        'Brigitte',
        'Capucine',
        'Caroline',
        'Catherine',
        'Cécile',
        'Céline',
        'Célina',
        'Chantal',
        'Charlotte',
        'Christelle',
        'Christiane',
        'Christine',
        'Claire',
        'Claudine',
        'Clémence',
        'Colette',
        'Constance',
        'Corinne',
        'Danielle',
        'Denise',
        'Diane',
        'Dorothée',
        'Édith',
        'Éléonore',
        'Élisabeth',
        'Élise',
        'Élodie',
        'Émilie',
        'Emmanuelle',
        'Françoise',
        'Frédérique',
        'Gabrielle',
        'Geneviève',
        'Hélène',
        'Henriette',
        'Hortense',
        'Inès',
        'Isabelle',
        'Jacqueline',
        'Jeanne',
        'Jeannine',
        'Joséphine',
        'Josette',
        'Julie',
        'Juliette',
        'Laetitia',
        'Laure',
        'Laurence',
        'Lorraine',
        'Louise',
        'Luce',
        'Lucie',
        'Lucy',
        'Madeleine',
        'Manon',
        'Marcelle',
        'Margaux',
        'Margaud',
        'Margot',
        'Marguerite',
        'Margot',
        'Margaret',
        'Maggie',
        'daisy',
        'Marianne',
        'Marie',
        'Marine',
        'Marthe',
        'Martine',
        'Maryse',
        'Mathilde',
        'Michèle',
        'Michelle',
        'Michelle',
        'Monique',
        'Nathalie',
        'Nath',
        'Nathalie',
        'Nicole',
        'Noémi',
        'Océane',
        'Odette',
        'Olivie',
        'Patricia',
        'Paulette',
        'Pauline',
        'Pénélope',
        'Philippine',
        'Renée',
        'Sabine',
        'Simone',
        'Sophie',
        'Stéphanie',
        'Susanne',
        'Suzanne',
        'Susan',
        'Suzanne',
        'Sylvie',
        'Thérèse',
        'Valentine',
        'Valérie',
        'Véronique',
        'Victoire',
        'Virginie',
        'Zoé',
        'Camille',
        'Claude',
        'Dominique')

    first_names = first_names_male + first_names_female

    last_names = (
        'Dostie',
        'Louineaux',
        'Gladu',
        'Bonenfant',
        'Chnadonnet',
        'Lacroix',
        'Allain',
        'Jetté',
        'Vadnais',
        'Rouleau',
        'Chauvet',
        'Durand',
        'Sarrazin',
        'Labbé',
        'Pelland',
        'Ouellet',
        'Narcisse',
        'Lécuyer',
        'Lavoie',
        'Patry',
        'Rousseau',
        'Lapierre',
        'Savoie',
        'Marquis',
        'Bourgouin',
        'Cailot',
        'Jodoin',
        'Fugère',
        'David',
        'Racicot',
        'Ferland',
        'Corbeil',
        'Gagnon',
        'Berthiaume',
        'Proulx',
        'Leblanc',
        'Sanschagrin',
        'Chassé',
        'Busque',
        'Gaillard',
        'Boivin',
        'Nadeau',
        'Aubé',
        'Brousseau',
        'LHeureux',
        'Ricard',
        'Pelchat',
        'Bordeaux',
        'Mailly',
        'Compagnon',
        'Sauriol',
        'Doucet',
        'Guernon',
        'Leroux',
        'Plouffe',
        'Laforge',
        'Bienvenue',
        'Lacombe',
        'Laberge',
        'Lanteigne',
        'LeBatelier',
        'Therriault',
        'Simard',
        'Plourde',
        'Ruest',
        'Lepage',
        'Goulet',
        'Paiement',
        'Adler',
        'Favreau',
        'Mireault',
        'Sylvain',
        'Beaulac',
        'Guertin',
        'Trudeau',
        'Chartré',
        'Dagenais',
        'Auger',
        'Duplessis',
        'Laframboise',
        'Daigle',
        'Roy',
        'Bérard',
        'Gamache',
        'Paimboeuf',
        'Barrette',
        'Carignan',
        'Cyr',
        'Dastous',
        'Talon',
        'Giroux',
        'Gaillou',
        'Cantin',
        'Longpré',
        'Levasseur',
        'Cousteau',
        'Marchesseault',
        'Bolduc',
        'Bellemare',
        'Patenaude',
        'Deserres',
        'Guérette',
        'Bureau',
        'Gabriaux',
        'Bonneville',
        'Lamarre',
        'Lesage',
        'Meunier',
        'Beaudry',
        'Panetier',
        'Abril',
        'Laliberté',
        'Grenier',
        'Laprise',
        'Théberge',
        'Salois',
        'Beaudouin',
        'St-Jacques',
        'Picard',
        'Mercier',
        'Brian',
        'Coudert',
        'Chouinard',
        'Dubé',
        'Brisette',
        'Gousse',
        'Lebrun',
        'Varieur',
        'Labelle',
        'Duperré',
        'Grondin',
        'Lapointe',
        'Massé',
        'Chastain',
        'Ratté',
        'Lacharité',
        'Charest',
        'Royer',
        'Paradis',
        'Barteaux',
        'Norbert',
        'Parenteau',
        'Chrétien',
        'Sorel',
        'Quenneville',
        'Casgrain',
        'Faure',
        'Bourgeois',
        'Laramée',
        'Houde',
        'Tremblay',
        'Arpin',
        'LAngelier',
        'Renaud',
        'Saindon',
        'Leclair',
        'Martineau',
        'Bourget',
        'Neufville',
        'Raymond',
        'Allard',
        'Gendron',
        'Lapresse',
        'Dennis',
        'Charrette',
        'Marcil',
        'Laboissonnière',
        'Course',
        'Courtois',
        'Patel',
        'Bellefeuille',
        'Gauthier',
        'Bois',
        'Bonami',
        'Baron',
        'Busson',
        'Morin',
        'Blanc',
        'Bisaillon',
        'Thibault',
        'Bergeron',
        'deChateaub',
        'Garcia',
        'Jacques',
        'Thivierge',
        'Boisclair',
        'Champagne',
        'Hétu',
        'Lajeunesse',
        'Bernard',
        'Monty',
        'Durepos',
        'Lussier',
        'Généreux',
        'Givry',
        'Courcelle',
        'Rocher',
        'Robitaille',
        'Bazinet',
        'Morel',
        'Voisine',
        'Pinneau',
        'Tardif',
        'Noël',
        'Tisserand',
        'Jalbert',
        'Poulin',
        'Quessy',
        'Roux',
        'Duplanty',
        'Tétrault',
        'Jobin',
        'Chalifour',
        'Séguin',
        'Galarneau',
        'Bérubé',
        'Chicoine',
        'Despins',
        'Guibord',
        'Gaulin',
        'Tanguay',
        'Gagné',
        'Thériault',
        'Sirois',
        'Chenard',
        'Boulanger',
        'Turcotte',
        'Larivière',
        'Édouard',
        'Benjamin',
        'Clavet',
        'Lampron',
        'Gadbois',
        'Auclair',
        'Sciverit',
        'Cadieux',
        'Souplet',
        'Vallée',
        'Lamour',
        'Lereau',
        'Riel',
        'Collin',
        'Étoile',
        'Poissonnier',
        'Vernadeau',
        'Devoe',
        'Boucher',
        'Bordeleau',
        'Batard',
        'Bourque',
        'DAubigné',
        'Fouquet',
        'Descoteaux',
        'Lemaître',
        'Dupuis',
        'Lamothe',
        'Rochon',
        'Caouette',
        'Chauvin',
        'Charpie',
        'Jodion',
        'Douffet',
        'Bouvier',
        'Goguen',
        'Boulé',
        'Asselin',
        'Labossière',
        'Beauchamps',
        'Fontaine',
        'Gour',
        'Grandpré',
        'Lachance',
        'Rochefort',
        'Croteau',
        'Mazuret',
        'Moquin',
        'Fortier',
        'Baril',
        'Laforest',
        'Artois',
        'Dupont',
        'Fongemie',
        'Crête',
        'Brousse',
        'Deschamps',
        'Phaneuf',
        'Morneau',
        'Blais',
        'Brisebois',
        'Cuillerier',
        'Cormier',
        'Gamelin',
        'Joly',
        'deLaunay',
        'Grimard',
        'Caron',
        'Lambert',
        'Duranseau',
        'Simon',
        'LHiver',
        'Belisle',
        'Dumoulin',
        'Authier',
        'Lizotte',
        'Leduc',
        'Paquin',
        'Marleau',
        'Doiron',
        'Dumont',
        'Charpentier',
        'Moreau',
        'Denis',
        'Drouin',
        'deBrisay',
        'DeGrasse',
        'Charlebois',
        'Soucy',
        'Grivois',
        'Petit',
        'Foucault',
        'Ayot',
        'Beauchemin',
        'Laurent',
        'Laisné',
        'Dandonneau',
        'Thibodeau',
        'Dufour',
        'Piedalue',
        'Garnier',
        'Boutot',
        'Charette',
        'Arnoux',
        'Arsenault',
        'Fournier',
        'Fecteau',
        'Caya',
        'Begin',
        'Jolicoeur',
        'Hervieux',
        'Quirion',
        'Guay',
        'Marcheterre',
        'Camus',
        'Bélair',
        'Arcouet',
        'Aubin',
        'Lafrenière',
        'Loiseau',
        'Chaussée',
        'Dubeau',
        'Rodrigue',
        'Beausoleil',
        'Brault',
        'Chandonnet',
        'Hervé',
        'Rocheleau',
        'Verreau',
        'Vaillancourt',
        'Bisson',
        'Alexandre',
        'Mainville',
        'Bouchard',
        'Grandbois',
        'Sansouci',
        'Forest',
        'Lamare',
        'Couturier',
        'Pichette',
        'Dupéré',
        'Veilleux',
        'Pellerin',
        'Metivier',
        'Aucoin',
        'Gaudreau',
        'Bernier',
        'Plante',
        'Lafontaine',
        'Langlais',
        'Beaujolie',
        'Lépicier',
        'Berthelette',
        'DuTrieux',
        'Paulet',
        'Lebel',
        'Guimond',
        'Desilets',
        'DeLaVergne',
        'Mailloux',
        'Coupart',
        'Huard',
        'Ducharme',
        'Plaisance',
        'Trottier',
        'Huppé',
        'Gosselin',
        'Racine',
        'Faucher',
        'Latourelle',
        'Deblois',
        'Houle',
        'Desrosiers',
        'Binet',
        'Bussière',
        'Lamy',
        'Turgeon',
        'Lagacé',
        'Maheu',
        'Echeverri',
        'Briard',
        'Pirouet',
        'Tachel',
        'Mousseau',
        'Vadeboncoeur',
        'Clavette',
        'Legault',
        'Courtemanche',
        'Lafond',
        'Daviau',
        'Marier',
        'Gingras',
        'Devost',
        'Gilbert',
        'DesMeaux',
        'Bizier',
        'Archambault',
        'Margand',
        'LaCaille',
        'Paquet',
        'Viens',
        'Babin',
        'Veronneau',
        'Meilleur',
        'Davignon',
        'Parmentier',
        'Pelletier',
        'Béland',
        'Tougas',
        'Benoit',
        'Marseau',
        'Labrosse',
        'Bourassa',
        'Cloutier',
        'Méthot',
        'Grignon',
        'Covillon',
        'Bourgeau',
        'Lanoie',
        'Henrichon',
        'Bilodeau',
        'Petrie',
        'Richard',
        'Lauzier',
        'Charbonneau',
        'Chaloux',
        'Desforges',
        'Robert',
        'Chartier',
        'Parrot',
        'Truchon',
        'Duhamel',
        'Landry',
        'Robillard',
        'Couet',
        'Barrière',
        'Ruel',
        'Côté',
        'Martel',
        'Sabourin',
        'Lang',
        'Duval',
        'Rhéaume',
        'Guédry',
        'Goddu',
        'Jardine',
        'Monjeau',
        'Pitre',
        'Dubois',
        'Desnoyers',
        'Ménard',
        'Bonsaint',
        'Blondlot',
        'Allaire',
        'Desnoyer',
        'Berger',
        'Sacré',
        'Carrière',
        'Routhier',
        'Austin',
        'Deniger',
        'Lagueux',
        'Gregoire',
        'Bonnet',
        'Rouze',
        'Mothé',
        'Cinq-Mars',
        'Mouet',
        'Deslauriers',
        'Moïse',
        'Roussel',
        'Desaulniers',
        'Chatigny',
        'Pomerleau',
        'Montminy',
        'Beaudoin',
        'Achin',
        'Trépanier',
        'Lanctot',
        'Duffet',
        'Ailleboust',
        'Bler',
        'Gervais',
        'Flamand',
        'Beaulieu',
        'Beauchamp',
        'Dupuy',
        'Déziel',
        'Masson',
        'Louis',
        'Daoust',
        'Fremont',
        'Desjardins',
        'Leclerc',
        'Léveillé',
        'Pépin',
        'Mailhot',
        'Vertefeuille',
        'Audibert',
        'Richer',
        'Garreau',
        'LaGarde',
        'Leroy',
        'Bousquet',
        'Paré',
        'DAvis',
        'Quinn',
        'Bédard',
        'Martin',
        'Desroches',
        'Poirier',
        'Fresne',
        'Marceau',
        'Deschênes',
        'Ruais',
        'Migneault',
        'Beaupré',
        'Sauvé',
        'Lavallée',
        'Desruisseaux',
        'Charlesbois',
        'Gougeon',
        'Langlois',
        'Perillard',
        'Chalut',
        'Bossé',
        'Paquette',
        'DuLin',
        'Saurel',
        'Cressac',
        'Brunelle',
        'Duclos',
        'Lemelin',
        'Savard',
        'Brodeur',
        'Rivard',
        'Brochu',
        'Marcoux',
        'Cotuand',
        'Lefèbvre',
        'Girard',
        'Lacasse',
        'Parizeau',
        'Pariseau',
        'Saucier',
        'Lalonde',
        'Villeneuve',
        'Perrault',
        'Corbin',
        'Lejeune',
        'Berie',
        'Harquin',
        'Hughes',
        'Goudreau',
        'Fluet',
        'Boncoeur',
        'Brunault',
        'Quiron',
        'Lessard',
        'Laderoute',
        'Majory',
        'Auberjonois',
        'Couture',
        'Dionne',
        'LaGrande',
        'Demers',
        'Giguère',
        'Cartier',
        'Gauvin',
        'Therrien',
        'Huot',
        'Mercure',
        'René',
        'Michaud',
        'Lachapelle',
        'Loiselle',
        'Émond',
        'St-Jean',
        'Rancourt',
        'Doyon',
        'Bazin',
        'Barjavel',
        'Franchet',
        'Vachon',
        'Monrency',
        'Avare',
        'Coulombe',
        'Audet',
        'Potvin',
        'Fortin',
        'Perreault',
        'Brasseur',
        'Parent',
        'Clément',
        'St-Pierre',
        'Laux',
        'Larocque',
        'Lespérance',
        'Vincent',
        'Rivière',
        'Boileau',
        'Lemieux',
        'Blanchard',
        'DeLaRonde',
        'Michel',
        'Labrie',
        'Beauchesne',
        'Gareau',
        'Létourneau',
        'Senneville',
        'Bériault',
        'Faubert',
        'Marois',
        'Salmons',
        'Melanson',
        'Garceau',
        'Angélil',
        'Pouchard',
        'Riquier',
        'Pouliotte',
        'Tessier',
        'Frappier',
        'Dodier',
        'Labrecque',
        'Chabot',
        'Beaulé',
        'Jomphe',
        'Lazure',
        'Breton',
        'Reault',
        'Aupry',
        'Caisse',
        'Josseaume',
        'Vaillancour',
        'Chesnay',
        'Bourdette',
        'Lamontagne',
        'Bondy',
        'Lagrange',
        'Cliche',
        'Lévesque',
        'Boisvert',
        'Labonté',
        'Querry',
        'Godin',
        'Francoeur',
        'Bélanger',
        'Sicard',
        'Rossignol',
        'CinqMars',
        'Miron',
        'Lamoureux',
        'Croquetaigne',
        'Chevrette',
        'Lajoie',
        'Bertrand',
        'Mathieu',
        'Fréchette',
        'Primeau',
        'Charron',
        'Tollmache',
        'Pinette',
        'Hébert',
        'Guilmette',
        'Dufresne',
        'Sevier',
        'Poisson',
        'Daigneault',
        'Hachée',
        'Provencher',
        'Barrientos',
        'Thomas',
        'Lefebvre',
        'Martinez',
        'DaSilva',
        'Lefevre',
        'Boyer',
        'Lopez',
        'Andre',
        'Francois',
        'Muller',
        'Guerin',
        'Legrand',
        'Sanchez',
        'Chevalier',
        'Perez',
        'Clement',
        'Fernandez',
        'Robin',
        'Pereira',
        'Perrin',
        'Henry',
        'Gautier',
        'Nicolas',
        'Marie',
        'Noel',
        'Ferreira',
        'Lemaire',
        'Riviere',
        'Marchand',
        'Rodriguez',
        'Payet',
        'Lucas',
        'DosSantos',
        'Rodrigues',
        'Gerard',
        'Fernandes',
        'Brunet',
        'Meyer',
        'Barbier',
        'Renard',
        'Goncalves',
        'Brun',
        'Giraud',
        'Roger',
        'Schmitt',
        'Colin',
        'Arnaud',
        'Vidal',
        'Gonzalez',
        'Lemoine',
        'Roche',
        'Aubert',
        'Olivier',
        'Leclercq',
        'Pierre',
        'Philippe',
        'Martins',
        'Guillaume',
        'Lecomte',
        'Fabre',
        'Carpentier',
        'Vasseur',
        'Hubert',
        'Jean',
        'Dumas',
        'Rolland',
        'Rey',
        'Huet',
        'Gomez',
        'Guillot',
        'Moulin',
        'Hoarau',
        'Menard',
        'Fleury',
        'Adam',
        'Bertin',
        'Charles',
        'Aubry',
        'DaCosta',
        'Maillard',
        'Paris',
        'Lopes',
        'Guyot',
        'Carre',
        'Jacquet',
        'Renault',
        'Herve',
        'Klein',
        'Cousin',
        'Collet',
        'Leger',
        'Ribeiro',
        'Hernandez',
        'Bailly',
        'Schneider',
        'LeGall',
        'Ruiz',
        'Gomes',
        'Prevost',
        'Julien',
        'Germain',
        'Millet',
        'Remy',
        'Daniel',
        'Marques',
        'Maillot',
        'LeGoff',
        'Barre',
        'Perrot',
        'Leveque',
        'Marty',
        'Benard',
        'Monnier',
        'Hamon',
        'Alves',
        'Etienne',
        'Marchal',
        'Poulain',
        'Lemaitre',
        'Guichard',
        'Besson',
        'Mallet',
        'Hoareau',
        'Gillet',
        'Weber',
        'Jacob',
        'Chevallier',
        'Perrier',
        'Carlier',
        'Marechal',
        'Antoine',
        'Lebon',
        'Cordier',
        'Bouchet',
        'Pasquier',
        'Legros',
        'Delattre',
        'Humbert',
        'DeOliveira',
        'Briand',
        'Launay',
        'Perret',
        'Gay',
        'Nguyen',
        'Navarro',
        'Besnard',
        'Pichon',
        'Hebert',
        'Cohen',
        'Pons',
        'Lebreton',
        'Sauvage',
        'DeSousa',
        'Pineau',
        'Albert',
        'Pinto',
        'Barthelemy',
        'Turpin',
        'Bigot',
        'Lelievre',
        'Georges',
        'Reynaud',
        'Ollivier',
        'Voisin',
        'Guillet',
        'Vallee',
        'Coulon',
        'Marin',
        'Teixeira',
        'Costa',
        'Mahe',
        'Didier',
        'Charrier',
        'Gaudin',
        'Bodin',
        'Guillou',
        'Gros',
        'Blanchet',
        'Buisson',
        'Blondel',
        'Paul',
        'Dijoux',
        'Barbe',
        'Hardy',
        'Laine',
        'Evrard',
        'Laporte',
        'Rossi',
        'Joubert',
        'Regnier',
        'Tanguy',
        'Gimenez',
        'Devaux',
        'Morvan',
        'Levy',
        'Dias',
        'Lenoir',
        'Berthelot',
        'Pascal',
        'Vaillant',
        'Guilbert',
        'Moreno',
        'Colas',
        'Masse',
        'Baudry',
        'Bruneau',
        'Verdier',
        'Delorme',
        'Blin',
        'Guillon',
        'Mary',
        'Coste',
        'Pruvost',
        'Maury',
        'Valentin',
        'Godard',
        'Joseph',
        'Brunel',
        'Marion',
        'Texier',
        'Seguin',
        'Raynaud',
        'Bourdon',
        'Bonneau',
        'Maurice',
        'Legendre',
        'Ferrand',
        'Toussaint',
        'Techer',
        'Lombard',
        'Lefort',
        'Diaz',
        'Riou',
        'Clerc',
        'Weiss',
        'Imbert',
        'Jourdan',
        'Delahaye',
        'Gilles',
        'Guibert',
        'Begue',
        'Descamps',
        'Delmas',
        'Peltier',
        'Dupre',
        'Laroche',
        'Leconte',
        'Maillet',
        'Labbe',
        'Potier',
        'Normand',
        'Pottier',
        'Torres',
        'Blot',
        'Jacquot',
        'Lemonnier',
        'Bonnin',
        'Boutin',
        'Fischer',
        'Munoz',
        'Neveu',
        'Mendes',
        'Delannoy',
        'Wagner',
        'Mace',
        'Ramos',
        'Pages',
        'Petitjean',
        'Chauveau',
        'Foucher',
        'Peron',
        'Guyon',
        'Gallet',
        'Rousset',
        'Traore',
        'Vallet',
        'Letellier',
        'Bouvet',
        'Hamel',
        'Chretien',
        'Faivre',
        'Boulay',
        'Thierry',
        'Samson',
        'Ledoux',
        'Salmon',
        'Lecoq',
        'Pires',
        'Leleu',
        'Becker',
        'Diallo',
        'Merle',
        'Valette')

    prefixes = ('de', 'de la', 'Le', 'du')
