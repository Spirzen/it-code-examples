<?php

namespace App\Livewire;

use App\Models\Task;
use Livewire\Component;

class TaskSearch extends Component
{
    public string $query = '';

    public function render()
    {
        $tasks = Task::query()
            ->when($this->query, fn ($q) => $q->where('title', 'like', '%'.$this->query.'%'))
            ->orderByDesc('id')
            ->limit(20)
            ->get();

        return view('livewire.task-search', compact('tasks'));
    }
}
