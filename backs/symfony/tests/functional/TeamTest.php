<?php

namespace App\Tests\Functional;

use ApiPlatform\Symfony\Bundle\Test\ApiTestCase;
use App\Entity\Team;

class TeamTest extends ApiTestCase
{
    public function testCreateBook(): void
    {
        $response = static::createClient()->request('POST', '/api/teams', ['json' => [
          'name' => 'Team de Sacha',
          'owner' => 'Sacha',
          'pokemon1' => '/api/pokemons/25',
        ]]);

        $this->assertResponseStatusCodeSame(201);
        $this->assertResponseHeaderSame('content-type', 'application/ld+json; charset=utf-8');
        $this->assertJsonContains([
          '@context' => '/api/contexts/Team',
          '@type' => 'Team',
          'id' => 1,
          'name' => 'Team de Sacha',
          'owner' => 'Sacha',
          'pokemon1' => '/api/pokemons/25',
        ]);
        $this->assertMatchesRegularExpression('~^/api/teams/\d+$~', $response->toArray()['@id']);
        $this->assertMatchesResourceItemJsonSchema(Team::class);
    }

    public function testGetCollectionJsonLd(): void
    {
        $response = static::createClient()->request('GET', '/api/teams', [
          'headers' => [
            'accept' => 'application/ld+json',
          ],
        ]);

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/ld+json; charset=utf-8');

        $this->assertJsonContains([
          '@context' => '/api/contexts/Team',
          '@id' => '/api/teams',
          '@type' => 'hydra:Collection',
          'hydra:totalItems' => 1,
        ]);
        $this->assertCount(1, $response->toArray()['hydra:member']);
        $this->assertMatchesResourceCollectionJsonSchema(Team::class);
    }

    public function testGetJsonLd(): void
    {
        static::createClient()->request('GET', '/api/teams/1', [
          'headers' => [
            'accept' => 'application/ld+json',
          ],
        ]);

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/ld+json; charset=utf-8');

        $this->assertJsonContains([
          '@context' => '/api/contexts/Team',
          '@type' => 'Team',
          'id' => 1,
          'name' => 'Team de Sacha',
          'owner' => 'Sacha',
          'pokemon1' => '/api/pokemons/25',
        ]);
        $this->assertMatchesResourceItemJsonSchema(Team::class);
    }

    public function testGetJson(): void
    {
        static::createClient()->request('GET', '/api/teams/1', [
          'headers' => [
            'accept' => 'application/json',
          ],
        ]);

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/json; charset=utf-8');

        $this->assertJsonContains([
          'id' => 1,
          'name' => 'Team de Sacha',
          'owner' => 'Sacha',
          'pokemon1' => '/api/pokemons/25',
        ]);
        $this->assertMatchesResourceItemJsonSchema(Team::class);
    }

    public function testPutJson(): void
    {
        static::createClient()->request('PUT', '/api/teams/1', ['json' => [
          'name' => 'Team de Regis',
          'owner' => 'Regis',
          'pokemon1' => '/api/pokemons/133',
        ]]);

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/ld+json; charset=utf-8');

        $this->assertJsonContains([
          '@context' => '/api/contexts/Team',
          '@type' => 'Team',
          'id' => 1,
          'name' => 'Team de Regis',
          'owner' => 'Regis',
          'pokemon1' => '/api/pokemons/133',
        ]);
        $this->assertMatchesResourceItemJsonSchema(Team::class);
    }

    public function testPatchJson(): void
    {
        static::createClient()->request(
            'PATCH',
            '/api/teams/1',
            [
              'json' => [
                'owner' => 'Regis Chen',
                'pokemon2' => '/api/pokemons/4',
              ],
              'headers' => [
                'content-type' => 'application/merge-patch+json',
              ],
            ],
        );

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/ld+json; charset=utf-8');

        $this->assertJsonContains([
          '@context' => '/api/contexts/Team',
          '@type' => 'Team',
          'id' => 1,
          'name' => 'Team de Regis',
          'owner' => 'Regis Chen',
          'pokemon1' => '/api/pokemons/133',
          'pokemon2' => '/api/pokemons/4',
        ]);
        $this->assertMatchesResourceItemJsonSchema(Team::class);
    }

    public function testDelete(): void
    {
        static::createClient()->request('DELETE', '/api/teams/1');
        $this->assertResponseStatusCodeSame(204);
        $this->assertNull(
            static::getContainer()->get('doctrine')->getRepository(Team::class)->findOneBy(['id' => '1'])
        );
    }
}
