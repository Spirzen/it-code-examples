abstract class Handler
{
    protected $next;

    public function setNext(Handler $next)
    {
        $this->next = $next;
        return $next;
    }

    public function handle($request)
    {
        if ($this->next) {
            return $this->next->handle($request);
        }
        return $request;
    }
}

class AuthHandler extends Handler
{
    public function handle($request)
    {
        if (!$request->user()) {
            return response('Unauthorized', 401);
        }
        return parent::handle($request);
    }
}
