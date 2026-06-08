$kernel->middleware([
    \Illuminate\Foundation\Http\Middleware\CheckForMaintenanceMode::class,
]);

$kernel->middlewareGroups([
    'web' => [
        \App\Http\Middleware\EncryptCookies::class,
        \Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse::class,
    ],
    'api' => [
        'throttle:60,1',
        \Illuminate\Routing\Middleware\SubstituteBindings::class,
    ],
]);
