<?php

namespace Tests;

use PHPUnit\Framework\TestCase;
use App\Services\UserService;

class UserServiceTest extends TestCase
{
    public function testUserCreation(): void
    {
        $service = new UserService();
        $user = $service->create('Ivan', 'Petrov');
        
        $this->assertEquals('Ivan Petrov', $user->getFullName());
        $this->assertNotNull($user->getId());
    }
}
