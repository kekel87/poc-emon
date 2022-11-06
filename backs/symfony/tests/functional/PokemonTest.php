<?php

namespace App\Tests\Functional;

use ApiPlatform\Symfony\Bundle\Test\ApiTestCase;
use App\Entity\Pokemon;

class PokemonTest extends ApiTestCase
{
    public function testGetCollectionJsonLd(): void
    {
        $response = static::createClient()->request('GET', '/api/pokemons', [
          'headers' => [
            'accept' => 'application/ld+json',
          ],
        ]);

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/ld+json; charset=utf-8');

        $this->assertJsonContains([
          '@context' => '/api/contexts/Pokemon',
          '@id' => '/api/pokemons',
          '@type' => 'hydra:Collection',
          'hydra:totalItems' => 905,
          'hydra:view' => [
            '@id' => '/api/pokemons?page=1',
            '@type' => 'hydra:PartialCollectionView',
            'hydra:first' => '/api/pokemons?page=1',
            'hydra:last' => '/api/pokemons?page=31',
            'hydra:next' => '/api/pokemons?page=2',
          ],
        ]);
        $this->assertCount(30, $response->toArray()['hydra:member']);

        // Enum is not properly supported for now
        // $this->assertMatchesResourceCollectionJsonSchema(Pokemon::class);
    }

    public function testGetCollectionJson(): void
    {
        $response = static::createClient()->request('GET', '/api/pokemons', [
          'headers' => ['accept' => 'application/json'],
        ]);

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/json; charset=utf-8');

        $this->assertJsonContains([
          [
            'id' => 1,
            'name' => 'bulbasaur',
            'type1' => 'grass',
            'type2' => 'poison',
          ],
        ]);

        $this->assertCount(30, $response->toArray());

        // Enum is not properly supported for now
        // $this->assertMatchesResourceCollectionJsonSchema(Pokemon::class);
    }

    public function testGetJson(): void
    {
        static::createClient()->request('GET', '/api/pokemons/1', [
          'headers' => ['accept' => 'application/json'],
        ]);

        $this->assertResponseIsSuccessful();
        $this->assertResponseHeaderSame('content-type', 'application/json; charset=utf-8');

        $this->assertJsonContains([
          'id' => 1,
          'name' => 'bulbasaur',
          'type1' => 'grass',
          'type2' => 'poison',
        ]);

        // Enum is not properly supported for now
        // $this->assertMatchesResourceItemJsonSchema(Pokemon::class);
    }
}
