void hashmap_grow(HashMap *map)
{
    HashMap fresh = {0};
    fresh.capacity = map->capacity * 2;
    fresh.buckets = calloc(fresh.capacity, sizeof *fresh.buckets);

    for (size_t i = 0; i < map->capacity; i++) {
        for (Entry *e = map->buckets[i]; e != NULL; ) {
            Entry *next = e->next;
            hashmap_insert(&fresh, e->key, e->value); /* rehash */
            e = next;
        }
    }

    hashmap_destroy(map);
    *map = fresh;
}
