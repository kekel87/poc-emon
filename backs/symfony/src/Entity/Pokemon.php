<?php
 
namespace App\Entity;
 
use Doctrine\ORM\Mapping as ORM;
use Doctrine\Common\Collections\ArrayCollection;
use Symfony\Component\Validator\Constraints as Assert;
use ApiPlatform\Core\Annotation\ApiResource;
 
/**
 * @ORM\Entity
 * @ORM\HasLifecycleCallbacks()
 * @ORM\Table(name="pokemon")
 * @ApiResource()
 */
class Pokemon
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     * @ORM\Column(type="integer")
     */
    private ?int $id = null;
 
    /**
     * @ORM\Column(length=255)
     * @Assert\NotBlank()
     */
    public string $name;
  
 
    /******** METHODS ********/
 
    public function getId()
    {
        return $this->id;
    }
 
    public function __toString()
    {
        return $this->name;
    }
}