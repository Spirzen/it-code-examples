<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('counters', function (Blueprint $table) {
            $table->id(); // Автоинкрементный первичный ключ
            $table->integer('value')->default(0); // Целочисленное поле со значением по умолчанию 0
            $table->timestamps(); // Поля created_at и updated_at
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('counters');
    }
};
