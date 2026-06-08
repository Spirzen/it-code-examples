class UserController extends Controller
{
    public function show($id)
    {
        $user = User::findOrFail($id);
        return view('user.profile', compact('user'));
    }

    public function update(Request $request, $id)
    {
        $user = User::findOrFail($id);
        $user->update($request->validated());
        return redirect()->route('user.show', $id);
    }
}
