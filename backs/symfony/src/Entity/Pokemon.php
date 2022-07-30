<?php
 
namespace App\Entity;
 
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;
use ApiPlatform\Core\Annotation\ApiResource;
 
#[ORM\Entity]
#[ORM\HasLifecycleCallbacks()]
#[ORM\Table(name: "pokemon")]
#[ApiResource(
    collectionOperations: ['get'],
    itemOperations: ['get'],
)]
class Pokemon
{
    #[ORM\Id, ORM\Column, ORM\GeneratedValue]
    public ?int $id = null;
 
    #[ORM\Column(length: 255)]
    #[Assert\NotBlank()]
    public string $name;
 
    /******** METHODS ********/
  
    public function __toString()
    {
        return $this->name;
    }
}