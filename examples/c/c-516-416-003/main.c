#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

typedef struct {
    uint32_t magic;   /* например 0x31415926 */
    uint16_t version; /* 1 */
    uint32_t count;
} Header;

bool write_header(FILE *f, const Header *h)
{
    if (fwrite(&h->magic, sizeof h->magic, 1, f) != 1)
        return false;
    if (fwrite(&h->version, sizeof h->version, 1, f) != 1)
        return false;
    if (fwrite(&h->count, sizeof h->count, 1, f) != 1)
        return false;
    return true;
}
