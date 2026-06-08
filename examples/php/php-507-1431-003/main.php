<?php

namespace App\Http\Controllers;

use App\Models\Counter;
use Illuminate\Http\Request;

class CounterController extends Controller
{
    /**
     * Отображение начальной страницы
     */
    public function index()
    {
        // Получаем последний созданный счетчик или создаем новый
        $counter = Counter::latest()->first();
        
        if (!$counter) {
            $counter = Counter::create(['value' => 0]);
        }

        return view('counter.index', compact('counter'));
    }

    /**
     * Увеличение значения счетчика
     */
    public function increment(Request $request)
    {
        $counter = Counter::latest()->first();
        
        if ($counter) {
            $counter->increment('value');
        } else {
            $counter = Counter::create(['value' => 1]);
        }

        return redirect()->route('counter.index')
            ->with('success', 'Значение увеличено');
    }

    /**
     * Уменьшение значения счетчика
     */
    public function decrement(Request $request)
    {
        $counter = Counter::latest()->first();
        
        if ($counter && $counter->value > 0) {
            $counter->decrement('value');
        }

        return redirect()->route('counter.index')
            ->with('success', 'Значение уменьшено');
    }

    /**
     * Сброс счетчика
     */
    public function reset(Request $request)
    {
        $counter = Counter::latest()->first();
        
        if ($counter) {
            $counter->update(['value' => 0]);
        }

        return redirect()->route('counter.index')
            ->with('success', 'Счетчик сброшен');
    }
}
