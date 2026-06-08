#include <stdio.h>
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"

int main() {
    // Создание новой среды выполнения
    lua_State *L = luaL_newstate();
    
    // Загрузка стандартных библиотек
    luaL_openlibs(L);
    
    // Получение ссылки на функцию print из глобальной таблицы
    lua_getglobal(L, "print");
    
    // Помещение числа 42 в стек
    lua_pushnumber(L, 42);
    
    // Вызов функции print с одним аргументом и ожиданием нуля результатов
    // Первый аргумент - сама функция print, второй - число 42
    if (lua_pcall(L, 1, 0, 0) != LUA_OK) {
        fprintf(stderr, "Ошибка выполнения скрипта: %s\n", lua_tostring(L, -1));
        lua_close(L);
        return 1;
    }
    
    // Закрытие среды выполнения
    lua_close(L);
    return 0;
}
