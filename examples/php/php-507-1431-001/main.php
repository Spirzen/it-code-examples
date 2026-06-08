<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Counter extends Model
{
    // Имя таблицы в базе данных (по умолчанию используется множественное число от имени класса)
    protected $table = 'counters';

    // Поля, которые можно заполнять массово
    protected $fillable = ['value'];

    // Поля, которые нужно скрыть при сериализации (опционально)
    protected $hidden = [];
}
