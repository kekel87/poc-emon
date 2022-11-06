<?php

namespace App\Entity;

use ApiPlatform\Metadata\ApiResource;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity]
#[ApiResource]
class Team
{
    #[ORM\Id, ORM\Column, ORM\GeneratedValue]
    private ?int $id = null;

    #[ORM\Column]
    #[Assert\NotNull]
    #[Assert\NotBlank]
    public string $name;

    #[ORM\Column]
    #[Assert\NotNull]
    #[Assert\NotBlank]
    public string $owner;

    #[ORM\ManyToOne]
    #[Assert\NotBlank]
    #[Assert\NotNull]
    public Pokemon $pokemon1;

    #[ORM\ManyToOne]
    public ?Pokemon $pokemon2;

    #[ORM\ManyToOne]
    public ?Pokemon $pokemon3;

    #[ORM\ManyToOne]
    public ?Pokemon $pokemon4;

    #[ORM\ManyToOne]
    public ?Pokemon $pokemon5;

    #[ORM\ManyToOne]
    public ?Pokemon $pokemon6;

    public function getId(): ?int
    {
        return $this->id;
    }
}
