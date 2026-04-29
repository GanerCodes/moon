// ChatGPT

/* 
  #include <stdalign.h>
  #define AVEC_HDR_SIZE ((sizeof(avec_hdr) + alignof(max_align_t)-1) & ~(alignof(max_align_t)-1))
  #define AVEC_HDR(v) ((avec_hdr *)((char *)(v) - AVEC_HDR_SIZE))
  avec_hdr *h = arena_alloc(Ѧ, AVEC_HDR_SIZE + elem_size * cap);
  return (void *)((char*)h + AVEC_HDR_SIZE);
*/

#include <string.h>
#include <stdint.h>
#include <stdlib.h>

#define ARENA_BLOCK_SIZE 4096

/* ========= Arena ========= */
typedef struct ArenaBlock {
  struct ArenaBlock *next;
  size_t used, cap;
  char data[];
} ArenaBlock;
typedef struct { ArenaBlock *head; } Arena;

void arena_init(Arena *Ѧ) { Ѧ->head = NULL; }

static inline void *arena_alloc(Arena *Ѧ, size_t sz) {
  sz = (sz+7) & ~7;
  ArenaBlock *b = Ѧ->head;
  if(!b || b->used + sz > b->cap) {
    size_t cap = sz > ARENA_BLOCK_SIZE ? sz : ARENA_BLOCK_SIZE;
    b = (ArenaBlock *)malloc(sizeof(ArenaBlock) + cap);
    b->next = Ѧ->head;
    b->used = 0;
    b->cap = cap;
    Ѧ->head = b; }
  void *ptr = b->data + b->used;
  b->used += sz;
  return ptr; }

void arena_free_all(Arena *Ѧ) {
  ArenaBlock *b = Ѧ->head;
  while(b) { ArenaBlock *n = b->next;
             free(b);
             b = n; }
  Ѧ->head = NULL; }

/* ========= Vector ========= */

/*
Layout (compatible with "pointer is array"):
[ header ][ elements... ]

User sees: T*
Header is just before it.
*/

typedef struct { uint32_t cap; uint32_t len; } avec_hdr;

#define AVEC_HDR(v) ((avec_hdr *)((char *)(v) - sizeof(avec_hdr)))

/* Create */
static inline void *_avec_create(Arena *Ѧ, size_t elem_size) {
  avec_hdr *h = (avec_hdr *)arena_alloc(Ѧ, sizeof(avec_hdr) + 4*elem_size);
  h->cap = 4;
  h->len = 0;
  return (void *)(h + 1); }

/* Size */
#define vector_size(v) ((v) ? AVEC_HDR(v)->len : 0)

/* Grow */
static inline void *_avec_grow(Arena *Ѧ, void *v, size_t elem_size) {
  avec_hdr *h = AVEC_HDR(v);
  uint32_t new_cap = h->cap * 2;
  
  avec_hdr *nh = (avec_hdr *)arena_alloc(Ѧ, sizeof(avec_hdr) + elem_size * new_cap);
  nh->cap = new_cap;
  nh->len = h->len;
  
  memcpy(nh + 1, v, elem_size * h->len);
  return (void *)(nh + 1); }

/* Push (returns pointer to new element) */
static inline void *_avec_add_dst(Arena *Ѧ, void **vptr, size_t elem_size) {
  void *v = *vptr;
  if(!v) {
    v = _avec_create(Ѧ, elem_size);
    *vptr = v; }

  avec_hdr *h = AVEC_HDR(v);

  if(h->len >= h->cap) {
    v = _avec_grow(Ѧ, v, elem_size);
    *vptr = v;
    h = AVEC_HDR(v); }

  void *slot = (char *)v + elem_size * h->len;
  h->len++;
  return slot; }
#define vector_add_dst(Ѧ, vptr) _avec_add_dst(Ѧ, (void **)(vptr), sizeof(**(vptr)))

/* Pop */
#define vector_pop(v) do { if((v) && AVEC_HDR(v)->len) AVEC_HDR(v)->len--; } while(0)

/* Free (noop for arena) */
#define vector_free(v) ((void)0)