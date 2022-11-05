<?php

$finder = (new PhpCsFixer\Finder())
    ->exclude('var')
    ->exclude('public/bundles')
    ->exclude('vendor')
    ->in(__DIR__);

return (new PhpCsFixer\Config())
    ->setRules([
        '@Symfony' => true,
    ])
    ->setFinder($finder);
