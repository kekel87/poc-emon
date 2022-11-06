<?php

namespace App\Entity;

use ApiPlatform\Metadata\ApiResource;
use ApiPlatform\Metadata\Get;
use ApiPlatform\Metadata\GetCollection;
use App\Enum\Type;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity]
#[ApiResource(
    operations: [
        new Get(uriTemplate: '/pokemons/{id}'),
        new GetCollection(uriTemplate: '/pokemons'),
    ]
)]
class Pokemon
{
    #[ORM\Id, ORM\Column, ORM\GeneratedValue]
    public ?int $id = null;

    #[ORM\Column(length: 255)]
    #[Assert\NotNull]
    #[Assert\NotBlank]
    public string $name;

    #[ORM\Column(type: 'string', enumType: Type::class)]
    #[Assert\NotNull]
    #[Assert\NotBlank]
    public Type $type1;

    #[ORM\Column(type: 'string', enumType: Type::class, nullable: true)]
    public ?Type $type2 = null;

    public function getId(): ?int
    {
        return $this->id;
    }
}
