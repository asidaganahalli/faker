# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{prefix}} {{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{prefix}} {{first_name}} {{last_name}}',
    )
    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}} {{suffix_male}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}} {{suffix_male}}',
    )

    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}} {{suffix_female}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}} {{suffix_female}}',
    )

    formats = formats_male + formats_female

    # source: https://www.data.gv.at/katalog/dataset/87fc82a0-0042-49c8-b6f9-2602cd3dc17a
    first_names_male = (
        'Aaron', 'Adam', 'Adrian', 'Adriano', 'Alan', 'Aleksander',
        'Alex', 'Alexandar', 'Alexander', 'Andreas', 'Andrej', 'Angelo', 'Anton',
        'Antonio', 'Antonius', 'Arda', 'Armin', 'Aron', 'Arthur', 'Aurelio', 'Axel',
        'Bastian', 'Ben', 'Benedict', 'Benedikt', 'Beni', 'Benjamin', 'Bernhard', 'Boris',
        'Bruno', 'Calvin', 'Carl', 'Carlo', 'Chris', 'Christian', 'Christoph',
        'Christopher', 'Clemens', 'Constantin', 'Cornelius', 'Cristiano', 'Damian', 'Daniel',
        'Danilo', 'Dario', 'Darius', 'Darko', 'David', 'Dennis', 'Dominik',
        'Eduard', 'Elias', 'Elyas', 'Emanuel', 'Emil', 'Emilian', 'Emmanuel', 'Eric',
        'Erik', 'Erwin', 'Fabian', 'Fabio', 'Felix', 'Ferdinand', 'Fernando', 'Filip',
        'Finn', 'Florentin', 'Florian', 'Florin', 'Franz', 'Frederik', 'Fridolin',
        'Friedrich', 'Gabriel', 'Georg', 'Gregor', 'Gustav', 'Heinrich', 'Henri',
        'Henrik', 'Henry', 'Hubert', 'Hugo', 'Igor', 'Ilias', 'Isa', 'Ismail', 'Jacob',
        'Jakob', 'James', 'Jamie', 'Jan', 'Jannik', 'Jannis', 'Jasper', 'Joel', 'Johann',
        'Johannes', 'John', 'Jonas', 'Jonathan', 'Josef', 'Joseph', 'Joshua', 'Julian',
        'Julius', 'Justin', 'Justus', 'Kai', 'Karim', 'Karl', 'Kevin', 'Kilian', 'Konrad',
        'Konstantin', 'Kristian', 'Lars', 'Laurenz', 'Laurin', 'Lean', 'Leander', 'Lennard',
        'Lennart', 'Leo', 'Leon', 'Leonard', 'Leonardo', 'Leonhard', 'Leopold', 'Levi',
        'Liam', 'Lino', 'Linus', 'Lionel', 'Lorenz', 'Lorenzo', 'Louis', 'Luca', 'Lucas',
        'Luis', 'Luka', 'Lukas', 'Maksim', 'Manuel', 'Marc', 'Marcel', 'Marco', 'Marcus',
        'Mario', 'Marius', 'Mark', 'Marko', 'Markus', 'Martin', 'Marvin', 
        'Mateo', 'Matheo', 'Mathias', 'Matteo', 'Matthias', 'Maurice', 'Max',
        'Maximilian', 'Merlin', 'Mert', 'Michael', 'Mika', 'Mike', 'Milan', 'Milo', 'Moritz',
        'Natan', 'Nathan', 'Nicholas', 'Nick', 'Nico', 'Nicolai', 'Nicolas', 'Niklas',
        'Niko', 'Nikola', 'Nikolai', 'Nikolas', 'Nikolaus', 'Nils', 'Nino', 'Noah',
        'Noel', 'Oliver', 'Oscar', 'Oskar', 'Pascal', 'Patrick', 'Patrik', 'Paul',
        'Peter', 'Philip', 'Philipp', 'Phillip', 'Raffael', 'Ralph', 'Raphael',
        'Rene', 'Ricardo', 'Richard', 'Robert', 'Robin', 'Roman', 'Ruben', 'Sam',
        'Samuel', 'Sandro', 'Sascha', 'Sebastian', 'Severin', 'Simon', 'Stefan', 'Stephan',
        'Steven', 'Sven', 'Teodor', 'Theo', 'Theodor', 'Thomas', 'Tim', 'Timo', 'Timon',
        'Tobias', 'Tom', 'Tristan', 'Valentin', 'Valentino', 'Victor', 'Viktor',
        'Vincent', 'Vito', 'William', 'Xavier'
    )

    # source: https://www.data.gv.at/katalog/dataset/87fc82a0-0042-49c8-b6f9-2602cd3dc17a
    first_names_female = (
        'Adelina', 'Adriana', 'Ajna', 'Alara', 'Aleksandra', 'Alena', 'Alexa', 'Alexandra',
        'Alexia', 'Alice', 'Alma', 'Amanda', 'Amelia', 'Amelie', 'Anabella', 'Anastasia',
        'Andjela', 'Andjelina', 'Andrea', 'Angela', 'Angelika',
        'Angelina', 'Anika', 'Anita', 'Anja', 'Anna', 'Anna-Lena', 'Anna-Maria', 'Annabell',
        'Annabella', 'Annabelle', 'Annalena', 'Anne', 'Annika', 'Antonella', 'Antonia',
        'Ariana', 'Ariane', 'Aurelia', 'Aurora', 'Ava', 'Aylin', 'Barbara', 'Beatrice',
        'Bernadette', 'Berra', 'Bianca', 'Carina', 'Carla', 'Carlotta', 'Carolina',
        'Caroline', 'Catharina', 'Cecilia', 'Charlotte', 'Christina', 'Christine', 'Claire', 
        'Clara', 'Clarissa', 'Claudia', 'Constanze', 'Cristina', 'Dana', 'Daniela', 'Denise',
        'Diana', 'Dilara', 'Domenica', 'Dora', 'Eda', 'Edda', 'Ela', 'Elena', 'Eleonora',
        'Elina', 'Elisa', 'Elisabeth', 'Ella', 'Ellie', 'Elma', 'Elona', 'Elsa', 'Elvira',
        'Emanuela', 'Emely', 'Emilia', 'Emilie', 'Emilija', 'Emma', 'Erina', 'Estelle',
        'Esther', 'Eva', 'Evelyn', 'Felicitas', 'Fiona', 'Florentina', 'Francesca', 'Franziska',
        'Frida', 'Gabriela', 'Gloria', 'Hanna', 'Hannah', 'Heidi', 'Helena', 'Helene', 'Ina',
        'Ines', 'Irina', 'Iris', 'Irma', 'Isabel', 'Isabell', 'Isabella',
        'Isabelle', 'Jana', 'Janine', 'Jasmina', 'Jasmine', 'Jennifer', 'Jessica',
        'Johanna', 'Josefine', 'Jovana', 'Julia', 'Juliana', 'Juliane',
        'Julijana', 'Juna', 'Kalina', 'Karina', 'Karla', 'Karolina', 'Karoline',
        'Katarina', 'Katharina', 'Katja', 'Kerstin', 'Klara', 'Kristina',
        'Kyra', 'Laetitia', 'Laila', 'Lana', 'Lara', 'Lara-Sophie', 'Larissa', 'Laura',
        'Laureen', 'Lea', 'Lea-Sophie', 'Leah', 'Leandra', 'Lena', 'Leni', 'Leona', 'Leoni',
        'Leonie', 'Leonora', 'Leontina', 'Leticia', 'Leyla', 'Lia', 'Lilia', 'Lilian',
        'Liliana', 'Liliane', 'Lilli', 'Lilly', 'Lily', 'Lina', 'Linda', 'Linnea', 'Lisa',
        'Lisa-Marie', 'Lola', 'Lora', 'Lorena', 'Lotta', 'Lotte', 'Louisa',
        'Louise', 'Luana', 'Lucia', 'Lucie', 'Luisa', 'Luise', 'Luna', 'Lydia',
        'Madeleine', 'Magdalena', 'Maida', 'Maja', 'Malena', 'Manuela', 'Mara', 'Maria',
        'Mariam', 'Mariana', 'Marie', 'Marie-Louise', 'Marie-Sophie', 'Mariella',
        'Marijana', 'Marina', 'Marissa', 'Marlene', 'Marta', 'Martha', 'Martina', 'Maryam',
        'Mathilda', 'Matilda', 'Maya', 'Melanie', 'Melek', 'Melina', 'Melisa', 'Melissa',
        'Mia', 'Michaela', 'Michelle', 'Mila', 'Milica', 'Mina', 'Mira', 'Miriam',
        'Mona', 'Nadia', 'Nadin', 'Nadine', 'Nadja', 'Naomi', 'Natalia', 'Natalie',
        'Natascha', 'Nathalie', 'Nela', 'Nele', 'Nelly', 'Nicola', 'Nicole', 'Nika',
        'Nikita', 'Nikola', 'Nikolina', 'Nina', 'Nisa', 'Nora', 'Norah', 'Olivia',
        'Patricia', 'Paula', 'Paulina', 'Pauline', 'Petra', 'Philippa', 'Pia', 'Rachel',
        'Raffaela', 'Rana', 'Rayana', 'Rebecca', 'Rita', 'Romy', 'Ronja', 'Ronya', 'Rosa',
        'Rosalie', 'Ruth', 'Sabine', 'Sabrina', 'Sahra', 'Salma',
        'Sandra', 'Sara', 'Sarah', 'Selena', 'Selin', 'Selina', 'Selma', 'Sena', 'Siena',
        'Sigrid', 'Sofia', 'Sofie', 'Sofija', 'Sonja', 'Sophia', 'Sophie', 'Sophie-Marie',
        'Soraya', 'Stefanie', 'Stella', 'Stephanie', 'Tamara', 'Tanja',
        'Tea', 'Theodora', 'Theresa', 'Therese', 'Tiffany', 'Tina',
        'Valentina', 'Vanessa', 'Vera', 'Verena', 'Veronika', 'Victoria',
        'Viktoria', 'Viola', 'Violetta', 'Vivian',
        'Yasmina', 'Ylvie', 'Yvonne', 'Zara', 'Zoe', 'Zoey',
    )

    first_names = first_names_male + first_names_female

    # about 1000 of the most popular Austrian surnames
    # https://de.wiktionary.org/wiki/Verzeichnis:Deutsch/Namen/die_h%C3%A4ufigsten_Nachnamen_%C3%96sterreichs
    last_names = (
        'Achleitner', 'Ackerl', 'Adam', 'Adler', 'Aichholzer', 'Aichinger',
        'Aigner', 'Albrecht', 'Altmann', 'Amann', 'Amon', 'Anderl', 'Angerer', 'Arnold',
        'Artner', 'Aschauer', 'Auer', 'Augustin', 'Auinger', 'Bacher', 'Bachinger',
        'Bachler', 'Bachmann', 'Bader', 'Baier', 'Baldauf', 'Barth', 'Bartl', 'Bauer',
        'Baumann', 'Baumgartner', 'Bayer', 'Beck', 'Becker', 'Beer', 'Berchtold', 'Berger',
        'Bergmann', 'Berner', 'Bernhard', 'Berthold', 'Bichler', 'Biedermann', 'Binder',
        'Bischof', 'Bitschnau', 'Bittner', 'Blauensteiner', 'Blum', 'Blümel', 'Bock',
        'Bodner', 'Bogner', 'Brandl', 'Brandner', 'Brandstetter', 'Brandstätter',
        'Brandtner', 'Braun', 'Brenner', 'Breuer', 'Bruckner', 'Brugger', 'Brunner', 'Bräuer',
        'Buchberger', 'Buchegger', 'Bucher', 'Buchinger', 'Buchner', 'Burger', 'Burgstaller',
        'Burtscher', 'Bäck', 'Böck', 'Böhler', 'Böhm', 'Bösch', 'Bürger', 'Dallinger',
        'Dangl', 'Danner', 'Danninger', 'Decker', 'Dengg', 'Denk', 'Deutschmann', 'Dietl',
        'Dietrich', 'Dirnberger', 'Dittrich', 'Dobler', 'Doppler', 'Dorfer', 'Dorn',
        'Dorner', 'Draxler', 'Dünser', 'Eberhard', 'Eberharter', 'Eberl', 'Ebner', 'Ecker',
        'Eder', 'Edlinger', 'Egger', 'Eibl', 'Eichberger', 'Eichhorn', 'Eichinger',
        'Eisl', 'Eisner', 'Eller', 'Ender', 'Engel', 'Engl', 'Enzinger', 'Erber',
        'Erhart', 'Erlacher', 'Erler', 'Ernst', 'Ertl', 'Fabian', 'Falkner', 'Fankhauser',
        'Farkas', 'Fasching', 'Fehringer', 'Feichtenschlager', 'Feichter', 'Feichtinger',
        'Feichtner', 'Feigl', 'Felber', 'Felder', 'Fellinger', 'Fellner', 'Fercher', 'Ferstl',
        'Fichtinger', 'Fiedler', 'Fink', 'Fischer', 'Fitz', 'Fleck', 'Fleischhacker',
        'Fleischmann', 'Foidl', 'Forster', 'Forstner', 'Frank', 'Franz', 'Freitag',
        'Freudenthaler', 'Frey', 'Frick', 'Friedl', 'Friedrich', 'Frisch', 'Fritsch', 'Fritz',
        'Froschauer', 'Fröhlich', 'Fröschl', 'Frühwirth', 'Fuchs', 'Fuhrmann', 'Füreder',
        'Fürst', 'Gabriel', 'Gahleitner', 'Galler', 'Gamsjäger', 'Gangl', 'Gartner',
        'Gasser', 'Gassner', 'Gattringer', 'Geier', 'Geiger', 'Geisler', 'Geyer', 'Gindl',
        'Glaser', 'Glatz', 'Glück', 'Gmeiner', 'Gollner', 'Gosch', 'Grabher', 'Grabner',
        'Graf', 'Grasser', 'Grassl', 'Gratz', 'Gratzer', 'Gratzl', 'Greiner', 'Griesser',
        'Grill', 'Gritsch', 'Gross', 'Groß', 'Gruber', 'Grundner', 'Grünberger', 'Grüner',
        'Grünwald', 'Gschaider', 'Gschwandtner', 'Gstrein', 'Guggenberger', 'Gutmann',
        'Gärtner', 'Göschl', 'Götz', 'Günther', 'Haas', 'Haberl', 'Hacker', 'Hackl',
        'Haderer', 'Hafner', 'Hagen', 'Hager', 'Hahn', 'Haid', 'Haiden', 'Haider',
        'Haidinger', 'Haindl', 'Hainzl', 'Haller', 'Hammer', 'Hammerer', 'Hammerl', 'Handl',
        'Handler', 'Haring', 'Harrer', 'Hartl', 'Hartmann', 'Haslauer', 'Haslinger',
        'Hattinger', 'Hauer', 'Haumer', 'Hausberger', 'Hauser', 'Hebenstreit', 'Hechenberger',
        'Heger', 'Heigl', 'Heim', 'Heindl', 'Heinrich', 'Heinz', 'Heinzl', 'Heiss',
        'Heissenberger', 'Held', 'Hell', 'Heller', 'Helm', 'Hemetsberger', 'Herbst', 'Hermann',
        'Herrmann', 'Herzog', 'Himmelbauer', 'Hinterberger', 'Hinteregger', 'Hinterleitner',
        'Hirsch', 'Hirschmann', 'Hochleitner', 'Hochreiter', 'Hofbauer', 'Hofer',
        'Hoffmann', 'Hofinger', 'Hofmann', 'Hofmeister', 'Hofstetter', 'Hofstätter', 'Holl',
        'Hollaus', 'Holler', 'Holzer', 'Holzinger', 'Holzknecht', 'Holzmann', 'Horak',
        'Horn', 'Hosp', 'Huber', 'Hubmann', 'Huemer', 'Hufnagl', 'Humer', 'Hummel',
        'Hummer', 'Huter', 'Hutter', 'Hutterer', 'Hämmerle', 'Häusler', 'Hödl', 'Höfer',
        'Höfler', 'Höglinger', 'Höller', 'Hölzl', 'Hörl', 'Hörmann', 'Hübner', 'Hütter',
        'Jahn', 'Jandl', 'Janisch', 'Jank', 'Jauk', 'Jenewein', 'Jost', 'Jovanovic',
        'Juen', 'Jung', 'Jungwirth', 'Jäger', 'Jöbstl', 'Kager', 'Kahr', 'Kain',
        'Kaindl', 'Kainz', 'Kaiser', 'Kalcher', 'Kaltenbrunner', 'Kaltenböck',
        'Kaltenegger', 'Kammerer', 'Kapeller', 'Kappel', 'Kargl', 'Karl', 'Karner', 'Karrer',
        'Kaspar', 'Kasper', 'Kastner', 'Kaufmann', 'Keller', 'Kellner', 'Keplinger',
        'Kern', 'Kerschbaum', 'Kerschbaumer', 'Kessler', 'Kirchmair', 'Kirchner',
        'Kirschner', 'Kiss', 'Kitzler', 'Klammer', 'Klaus', 'Klausner', 'Klein', 'Klement',
        'Klinger', 'Klingler', 'Klocker', 'Kloiber', 'Klotz', 'Klug', 'Knapp', 'Knaus',
        'Knoll', 'Kober', 'Koch', 'Kocher', 'Kofler', 'Kogler', 'Kohl', 'Kohler', 'Kolar',
        'Kolb', 'Koller', 'Kollmann', 'Kolm', 'Konrad', 'Kopf', 'Kopp', 'Koppensteiner',
        'Kraft', 'Krainer', 'Krainz', 'Kral', 'Krall', 'Kramer', 'Krammer', 'Kratzer',
        'Kraus', 'Kraxner', 'Kreidl', 'Kreiner', 'Kremser', 'Krenn', 'Kreuzer', 'Kriegl',
        'Kronberger', 'Kronsteiner', 'Krug', 'Kröll', 'Kucera', 'Kugler', 'Kuhn', 'Kummer',
        'Kunz', 'Kurz', 'Kurzmann', 'Käfer', 'Köberl', 'Köck', 'Köhler', 'Kölbl', 'Köll',
        'König', 'Kössler', 'Lackner', 'Ladner', 'Lagler', 'Laimer', 'Lammer', 'Lampert',
        'Lampl', 'Lamprecht', 'Landl', 'Lang', 'Langer', 'Larcher', 'Lassnig', 'Leber',
        'Lechner', 'Lederer', 'Leeb', 'Lehner', 'Leibetseder', 'Leitgeb', 'Leithner',
        'Leitner', 'Lengauer', 'Lenz', 'Leonhartsberger', 'Leopold', 'Lerch', 'Lercher',
        'Lettner', 'Leutgeb', 'Lichtenegger', 'Linder', 'Lindinger', 'Lindner', 'Lindorfer',
        'Lintner', 'Lipp', 'List', 'Loibl', 'Loidl', 'Lorenz', 'Ludwig', 'Luger',
        'Luttenberger', 'Lutz', 'Löffler', 'Macher', 'Mader', 'Maier', 'Maierhofer', 'Mair',
        'Mairhofer', 'Mandl', 'Mann', 'Margreiter', 'Maringer', 'Mark', 'Markl', 'Marte',
        'Martin', 'Marx', 'Mathis', 'Maurer', 'Mayer', 'Mayerhofer', 'Mayr', 'Mayrhofer',
        'Meier', 'Meindl', 'Meister', 'Meixner', 'Messner', 'Metzler', 'Meusburger',
        'Meyer', 'Mitter', 'Mitteregger', 'Mitterer', 'Mitterlehner', 'Mittermayr',
        'Mohr', 'Moosbrugger', 'Moritz', 'Moser', 'Muhr', 'Mörth', 'Mühlbacher',
        'Mühlberger', 'Mühlböck', 'Müller', 'Müllner', 'Nagel', 'Nagele', 'Nagl', 'Nemeth',
        'Neubacher', 'Neubauer', 'Neugebauer', 'Neuhauser', 'Neuhold', 'Neulinger', 'Neumann',
        'Neumayer', 'Neumayr', 'Neumeister', 'Neumüller', 'Neuner', 'Neureiter', 'Neuwirth',
        'Niederl', 'Nowak', 'Nussbaumer', 'Nußbaumer', 'Nöbauer', 'Oberhauser', 'Oberhofer',
        'Oberleitner', 'Obermayr', 'Obermüller', 'Oberndorfer', 'Ofner', 'Ortner', 'Ostermann',
        'Oswald', 'Ott', 'Pacher', 'Pachler', 'Paier', 'Pammer', 'Parzer', 'Pauer', 'Paul',
        'Paulitsch', 'Payer', 'Peer', 'Peham', 'Pendl', 'Penz', 'Perner', 'Pertl',
        'Pesendorfer', 'Peter', 'Petz', 'Pfeffer', 'Pfeifer', 'Pfeiffer', 'Pfister', 'Pfleger',
        'Philipp', 'Pichler', 'Pieber', 'Pilz', 'Pinter', 'Pircher', 'Pirker', 'Plank',
        'Plattner', 'Platzer', 'Pock', 'Pohl', 'Pointner', 'Pokorny', 'Pollak', 'Polzer',
        'Posch', 'Postl', 'Prager', 'Prantl', 'Praxmarer', 'Prem', 'Prenner', 'Prinz',
        'Probst', 'Prohaska', 'Pröll', 'Pucher', 'Puchner', 'Puntigam', 'Punz', 'Putz',
        'Pöll', 'Pölzl', 'Pöschl', 'Pühringer', 'Raab', 'Rabitsch', 'Rabl', 'Radl',
        'Rainer', 'Ramsauer', 'Rath', 'Rauch', 'Rausch', 'Rauscher', 'Rauter',
        'Rechberger', 'Redl', 'Reich', 'Reichel', 'Reicher', 'Reichl', 'Reichmann', 'Reif',
        'Reinbacher', 'Reindl', 'Reiner', 'Reinisch', 'Reinprecht', 'Reinthaler', 'Reischl',
        'Reisinger', 'Reisner', 'Reitbauer', 'Reiter', 'Reiterer', 'Reithofer', 'Reitinger',
        'Renner', 'Resch', 'Rettenbacher', 'Richter', 'Rieder', 'Riedl', 'Riedler',
        'Riedmann', 'Rieger', 'Riegler', 'Riener', 'Riepl', 'Rieser', 'Ringhofer', 'Rinner',
        'Ritter', 'Rohrer', 'Rohrmoser', 'Rosenberger', 'Rosner', 'Rossmann', 'Roth',
        'Rottensteiner', 'Rotter', 'Rudolf', 'Rupp', 'Röck', 'Rössler', 'Sagmeister', 'Sailer',
        'Salcher', 'Salzer', 'Salzmann', 'Sammer', 'Santner', 'Sattler', 'Sauer',
        'Schachinger', 'Schachner', 'Schaffer', 'Schalk', 'Schaller', 'Schandl', 'Schantl',
        'Scharf', 'Scharinger', 'Schartner', 'Schatz', 'Schatzl', 'Schauer', 'Scheer',
        'Scheiber', 'Scheidl', 'Schenk', 'Scherer', 'Scherr', 'Scherz', 'Scherzer',
        'Scheucher', 'Schiefer', 'Schiestl', 'Schilcher', 'Schiller', 'Schimpl', 'Schinagl',
        'Schindler', 'Schinnerl', 'Schlager', 'Schlosser', 'Schlögl', 'Schmid', 'Schmidinger',
        'Schmidl', 'Schmidt', 'Schmied', 'Schmuck', 'Schmölzer', 'Schnabl', 'Schneeberger',
        'Schneider', 'Schober', 'Scholz', 'Schramm', 'Schrammel', 'Schranz', 'Schreiber',
        'Schreiner', 'Schrempf', 'Schrenk', 'Schrittwieser', 'Schröder', 'Schubert', 'Schuh',
        'Schuler', 'Schuller', 'Schulz', 'Schuster', 'Schwab', 'Schwaiger', 'Schwaighofer',
        'Schwarz', 'Schwarzinger', 'Schwarzl', 'Schweiger', 'Schweighofer', 'Schweitzer',
        'Schwendinger', 'Schäfer', 'Schöberl', 'Schöffmann', 'Schöller', 'Schön', 'Schönauer',
        'Schönberger', 'Schöpf', 'Schüller', 'Schütz', 'Seebacher', 'Seidl', 'Seifert',
        'Seiler', 'Seiser', 'Seitz', 'Seiwald', 'Sieber', 'Sieberer', 'Siegl', 'Sigl',
        'Siller', 'Simic', 'Simon', 'Singer', 'Sommer', 'Sonnleitner', 'Sorger', 'Sperl',
        'Spiegl', 'Spindler', 'Spitzer', 'Spreitzer', 'Springer', 'Stadlbauer', 'Stadler',
        'Stangl', 'Stark', 'Staudacher', 'Staudinger', 'Stecher', 'Stefan', 'Steger',
        'Steidl', 'Steiger', 'Steinacher', 'Steinbacher', 'Steinbauer', 'Steinberger',
        'Steinböck', 'Steindl', 'Steiner', 'Steininger', 'Steinkellner', 'Steinlechner',
        'Steinwender', 'Stelzer', 'Stelzl', 'Stern', 'Steurer', 'Stiegler', 'Stifter', 'Stock',
        'Stocker', 'Stockhammer', 'Stockinger', 'Stoiber', 'Stolz', 'Strasser', 'Strauss',
        'Strauß', 'Streicher', 'Strobl', 'Strohmaier', 'Strohmayer', 'Strohmeier',
        'Stummer', 'Sturm', 'Stöckl', 'Stöger', 'Stückler', 'Stütz', 'Sulzer', 'Suppan',
        'Taferner', 'Tanzer', 'Tauber', 'Taucher', 'Teufl', 'Thaler', 'Thalhammer',
        'Thaller', 'Thurner', 'Tiefenbacher', 'Tischler', 'Toth', 'Trattner', 'Trauner',
        'Traxler', 'Trimmel', 'Trinkl', 'Trummer', 'Uhl', 'Ullmann', 'Ulrich', 'Unger',
        'Unterberger', 'Unterweger', 'Urban', 'Varga', 'Veit', 'Vogel', 'Vogl', 'Vogler',
        'Vogt', 'Wachter', 'Wagner', 'Walch', 'Walcher', 'Walder', 'Waldner', 'Wallner',
        'Walser', 'Walter', 'Waltl', 'Wandl', 'Weber', 'Wechselberger', 'Wegscheider',
        'Weidinger', 'Weigl', 'Weinberger', 'Weiser', 'Weiss', 'Weissenböck', 'Weiß',
        'Wenger', 'Weninger', 'Wenzl', 'Werner', 'Widhalm', 'Widmann', 'Wiedner',
        'Wieland', 'Wiener', 'Wiesbauer', 'Wieser', 'Wiesinger', 'Wiesner', 'Wild',
        'Wilfinger', 'Wilhelm', 'Wimmer', 'Windhager', 'Windisch', 'Winkler', 'Winter',
        'Wirth', 'Wittmann', 'Wohlmuth', 'Wolf', 'Wurm', 'Wurzer', 'Wurzinger',
        'Wögerbauer', 'Wöhrer', 'Yilmaz', 'Zach', 'Zangerl', 'Zauner', 'Zechmeister',
        'Zechner', 'Zehetner', 'Zeiler', 'Zeilinger', 'Zeiner', 'Zeller', 'Zenz', 'Zettl',
        'Ziegler', 'Zimmermann', 'Zotter', 'Zöchling', 'Zöhrer',
    )

    prefixes_male = (
        'Herr', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )
    prefixes_female = (
        'Frau', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )

    prefixes_male = (
        'Herr', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )
    prefixes_female = (
        'Frau', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )

    prefixes = ('Dr.', 'Mag.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.')
