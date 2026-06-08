$loop = React\EventLoop\Factory::create();
$server = new React\Http\Server(function (Psr\Http\Message\ServerRequestInterface $request) {
    return new React\Http\Message\Response(
        200,
        ['Content-Type' => 'text/plain'],
        "Привет из ReactPHP!\n"
    );
});

$socket = new React\Socket\Server('0.0.0.0:8080', $loop);
$server->listen($socket);

echo "Сервер запущен на http://127.0.0.1:8080\n";
$loop->run();
