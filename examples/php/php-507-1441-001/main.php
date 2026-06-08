<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class HelloController extends AbstractController
{
    #[Route('/hello/{name}', name: 'app_hello', requirements: ['name' => '[a-zA-Z]+'], defaults: ['name' => 'World'])]
    public function hello(string $name): Response
    {
        return $this->render('hello/hello.html.twig', [
            'name' => $name,
        ]);
    }

    #[Route('/api/hello', name: 'api_hello', methods: ['GET'])]
    public function apiHello(): Response
    {
        return $this->json(['message' => 'Hello from Symfony API']);
    }
}
