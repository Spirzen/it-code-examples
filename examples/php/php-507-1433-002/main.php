<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Resources\NoteResource;
use App\Models\Note;
use Illuminate\Http\Request;

class NoteController extends Controller
{
    public function index()
    {
        return NoteResource::collection(Note::latest()->get());
    }

    public function store(Request $request)
    {
        $data = $request->validate(['text' => 'required|string|max:2000']);
        $note = Note::create($data);
        return new NoteResource($note);
    }

    public function destroy(Note $note)
    {
        $note->delete();
        return response()->noContent();
    }
}
