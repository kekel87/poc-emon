<?php

namespace App\Entity;

use ApiPlatform\Metadata\ApiResource;
use ApiPlatform\Metadata\Get;
use ApiPlatform\Metadata\GetCollection;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity]
#[ApiResource(operations: [
    new Get(),
    new GetCollection(),
])]
class Pokemon
{
    #[ORM\Id, ORM\Column, ORM\GeneratedValue]
    public ?int $id = null;

    #[ORM\Column(length: 255, nullable: false)]
    #[Assert\NotBlank()]
    public string $name = '';

    public function getId(): ?int
    {
        return $this->id;
    }
}
