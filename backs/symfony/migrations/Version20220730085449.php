<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use App\Entity\Pokemon;
use App\Enum\Type;
use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;
use Symfony\Component\DependencyInjection\ContainerAwareInterface;
use Symfony\Component\DependencyInjection\ContainerAwareTrait;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20220730085449 extends AbstractMigration implements ContainerAwareInterface
{
    use ContainerAwareTrait;

    public function getDescription(): string
    {
        return 'Initial db migration with seed data';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TABLE pokemon (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR(255) NOT NULL, type1 VARCHAR(255) NOT NULL, type2 VARCHAR(255) DEFAULT NULL)');
        $this->addSql('CREATE TABLE team (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, pokemon1_id INTEGER DEFAULT NULL, pokemon2_id INTEGER DEFAULT NULL, pokemon3_id INTEGER DEFAULT NULL, pokemon4_id INTEGER DEFAULT NULL, pokemon5_id INTEGER DEFAULT NULL, pokemon6_id INTEGER DEFAULT NULL, name VARCHAR(255) NOT NULL, owner VARCHAR(255) NOT NULL, CONSTRAINT FK_C4E0A61F1722D724 FOREIGN KEY (pokemon1_id) REFERENCES pokemon (id) NOT DEFERRABLE INITIALLY IMMEDIATE, CONSTRAINT FK_C4E0A61F59778CA FOREIGN KEY (pokemon2_id) REFERENCES pokemon (id) NOT DEFERRABLE INITIALLY IMMEDIATE, CONSTRAINT FK_C4E0A61FBD2B1FAF FOREIGN KEY (pokemon3_id) REFERENCES pokemon (id) NOT DEFERRABLE INITIALLY IMMEDIATE, CONSTRAINT FK_C4E0A61F20FC2716 FOREIGN KEY (pokemon4_id) REFERENCES pokemon (id) NOT DEFERRABLE INITIALLY IMMEDIATE, CONSTRAINT FK_C4E0A61F98404073 FOREIGN KEY (pokemon5_id) REFERENCES pokemon (id) NOT DEFERRABLE INITIALLY IMMEDIATE, CONSTRAINT FK_C4E0A61F8AF5EF9D FOREIGN KEY (pokemon6_id) REFERENCES pokemon (id) NOT DEFERRABLE INITIALLY IMMEDIATE)');
        $this->addSql('CREATE INDEX IDX_C4E0A61F1722D724 ON team (pokemon1_id)');
        $this->addSql('CREATE INDEX IDX_C4E0A61F59778CA ON team (pokemon2_id)');
        $this->addSql('CREATE INDEX IDX_C4E0A61FBD2B1FAF ON team (pokemon3_id)');
        $this->addSql('CREATE INDEX IDX_C4E0A61F20FC2716 ON team (pokemon4_id)');
        $this->addSql('CREATE INDEX IDX_C4E0A61F98404073 ON team (pokemon5_id)');
        $this->addSql('CREATE INDEX IDX_C4E0A61F8AF5EF9D ON team (pokemon6_id)');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('DROP TABLE pokemon');
        $this->addSql('DROP TABLE team');
    }

    /**
     * Seed initial data.
     */
    public function postUp(Schema $schema): void
    {
        $url = 'https://beta.pokeapi.co/graphql/v1beta';
        $query = 'query {
        pokemon_v2_pokemon(where: {is_default: {_eq: true}}) {
            species_id: pokemon_species_id
            name
            types: pokemon_v2_pokemontypes {
            pokemon_v2_type {
                name
            }
            }
        }
        }';

        $context = stream_context_create([
            'http' => [
                'method' => 'POST',
                'header' => ['Content-Type: application/json'],
                'content' => json_encode(['query' => $query]),
            ],
        ]);
        $result = file_get_contents($url, false, $context);
        $pokemons = json_decode($result)->data->pokemon_v2_pokemon;

        // https://stackoverflow.com/a/25960400
        $em = $this->container->get('doctrine.orm.entity_manager');
        $batchSize = 50;

        for ($i = 0, $c = count($pokemons); $i < $c; ++$i) {
            $pkm = $pokemons[$i];
            $types = $pokemons[$i]->types;

            $pkm = new Pokemon();
            $pkm->id = $pokemons[$i]->species_id;
            $pkm->name = $pokemons[$i]->name;
            $pkm->type1 = Type::from($types[0]->pokemon_v2_type->name);
            $pkm->type2 = isset($types[1]) ? Type::from($types[1]->pokemon_v2_type->name) : null;
            $em->persist($pkm);

            if (($i % $batchSize) === 0) {
                $em->flush();
                $em->clear();
            }
        }
        $em->flush();
        $em->clear();
    }
}
