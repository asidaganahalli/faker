from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{prefix}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
    )

    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{prefix}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{first_name_female}}-{{first_name_female}} {{last_name}}',
    )

    formats = formats_male + formats_female

    first_names_male = (
        'Afonso', 'Alexandre', 'Álvaro', 'André', 'Ângelo', 'António', 'Artur',
        'Benjamim', 'Bernardo', 'Brian', 'Bruno', 'Bryan', 'Carlos',
        'Cláudio', 'Cristiano', 'César', 'Daniel', 'David', 'Denis',
        'Diego', 'Dinis', 'Diogo', 'Duarte', 'Edgar', 'Eduardo', 'Emanuel',
        'Enzo', 'Fernando', 'Filipe', 'Francisco', 'Frederico', 'Fábio',
        'Gabriel', 'Gaspar', 'Gil', 'Gonçalo', 'Guilherme', 'Gustavo',
        'Henrique', 'Hugo', 'Igor', 'Isaac', 'Ismael', 'Ivan', 'Ivo', 'Jaime',
        'Joaquim', 'Joel', 'Jorge', 'José', 'João', 'Kevin', 'Kévim',
        'Leandro', 'Leonardo', 'Lisandro', 'Lourenço', 'Luca', 'Lucas',
        'Luís', 'Manuel', 'Marco', 'Marcos', 'Martim', 'Mateus',
        'Matias', 'Mauro', 'Micael', 'Miguel', 'Márcio', 'Mário',
        'Nelson', 'Noa', 'Noah', 'Nuno', 'Paulo', 'Pedro', 'Rafael',
        'Renato', 'Ricardo', 'Rodrigo', 'Rui', 'Rúben', 'Salvador',
        'Samuel', 'Sandro', 'Santiago', 'Sebastião', 'Simão', 'Sérgio', 'Tiago',
        'Tomás', 'Tomé', 'Valentim', 'Vasco', 'Vicente', 'Vítor', 'William',
        'Wilson', 'Xavier',
    )

    first_names_female = (
        'Adriana', 'Alexandra', 'Alice', 'Alícia', 'Amélia', 'Ana', 'Andreia',
        'Ângela', 'Anita', 'Ariana', 'Beatriz', 'Benedita', 'Bianca', 'Bruna',
        'Bárbara', 'Caetana', 'Camila', 'Carlota', 'Carminho', 'Carolina',
        'Catarina', 'Clara', 'Constança', 'Daniela', 'Diana', 'Débora', 'Eduarda',
        'Ema', 'Emma', 'Emília', 'Erica', 'Érica', 'Erika', 'Eva', 'Fabiana',
        'Filipa', 'Flor', 'Francisca', 'Gabriela', 'Helena', 'Iara', 'Inês',
        'Irina', 'Íris', 'Isabel', 'Isabela', 'Joana', 'Juliana', 'Jéssica',
        'Júlia', 'Kelly', 'Kyara', 'Lara', 'Larissa', 'Laura', 'Leonor', 'Letícia',
        'Lia', 'Lorena', 'Luana', 'Luciana', 'Luna', 'Luísa', 'Lúcia', 'Madalena',
        'Mafalda', 'Mara', 'Margarida', 'Maria', 'Mariana', 'Marta', 'Matilde',
        'Melissa', 'Mia', 'Miriam', 'Mélanie', 'Naiara', 'Nair', 'Nicole', 'Nádia',
        'Núria', 'Patrícia', 'Petra', 'Pilar', 'Rafaela', 'Raquel', 'Renata',
        'Rita', 'Salomé', 'Sara', 'Sofia', 'Soraia', 'Tatiana', 'Teresa',
        'Valentina', 'Vera', 'Victória', 'Violeta', 'Vitória', 'Yara', 'Yasmin',
    )

    first_names = first_names_male + first_names_female

    last_names = (
        'Abreu', 'Almeida', 'Alves', 'Amaral', 'Amorim', 'Andrade', 'Anjos',
        'Antunes', 'Araújo', 'Assunção', 'Azevedo', 'Baptista', 'Barbosa',
        'Barros', 'Batista', 'Borges', 'Branco', 'Brito', 'Campos', 'Cardoso',
        'Carneiro', 'Carvalho', 'Castro', 'Coelho', 'Correia', 'Costa', 'Cruz',
        'Cunha', 'Domingues', 'Esteves', 'Faria', 'Fernandes', 'Ferreira',
        'Figueiredo', 'Fonseca', 'Freitas', 'Garcia', 'Gaspar', 'Gomes',
        'Gonçalves', 'Guerreiro', 'Henriques', 'Jesus', 'Leal', 'Leite', 'Lima',
        'Lopes', 'Loureiro', 'Lourenço', 'Macedo', 'Machado', 'Magalhães',
        'Maia', 'Marques', 'Martins', 'Matias', 'Matos', 'Melo', 'Mendes',
        'Miranda', 'Monteiro', 'Morais', 'Moreira', 'Mota', 'Moura',
        'Nascimento', 'Neto', 'Neves', 'Nogueira', 'Nunes', 'Oliveira',
        'Pacheco', 'Paiva', 'Pereira', 'Pinheiro', 'Pinho', 'Pinto', 'Pires',
        'Ramos', 'Reis', 'Ribeiro', 'Rocha', 'Rodrigues', 'Santos', 'Silva',
        'Simões', 'Soares', 'Sousa', 'Sá', 'Tavares', 'Teixeira', 'Torres',
        'Valente', 'Vaz', 'Vicente', 'Vieira',
    )

    prefixes = ('de', 'da', 'do')

    def prefix(self) -> str:
        return self.random_element(self.prefixes)
