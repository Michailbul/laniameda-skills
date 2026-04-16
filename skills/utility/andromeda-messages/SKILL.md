---
name: andromeda-messages
description: >
  Add, update, delete, or list nodes in the Andromeda Galaxy app.
  Also lock/unlock galaxies programmatically.

  Use when Michael asks to add a message/thought/record to any galaxy (Dreams, Life,
  Soulmate, Family, Antidreams), or to list/edit/delete nodes, unlock a galaxy, or check
  galaxy status.

  Keywords: add to andromeda, save to galaxy, add to dreams, add to жизнь,
  unlock your life, разблокируй семью, delete node, update node.
---

# Andromeda Messages

Full CRUD API for the Andromeda galaxy app plus galaxy lock/unlock control.

## Base URL

Use the deployed app base URL for the current environment.

- Current production: `https://andromeda.laniameda.space`
- Legacy redirect source: `https://www.mishabuloichyk.com`
- Local standalone repo example: `http://localhost:3331`

## Auth

`Authorization: Bearer <ADMIN_TOKEN>`

Use the repo's configured `ADMIN_TOKEN`.

---

## Galaxy Name Aliases

The `galaxy` field accepts any of these:

| Send this | Resolves to |
| --- | --- |
| `"Your Dreams"` / `"dreams"` / `"мечты"` | `sagittarius` |
| `"Your Soulmate"` / `"soulmate"` / `"partner"` / `"laniakea"` / `"партнёр"` | `wormhole` |
| `"Your Family"` / `"family"` / `"семья"` | `carina` |
| `"Your Life"` / `"life"` / `"жизнь"` | `andromeda` |
| `"Your Antidreams"` / `"antidreams"` / `"антимечты"` | `kepler` |
| Raw IDs (`sagittarius`, `wormhole`, etc.) | also work |

Always confirm with the canonical display name, not the internal ID.

---

## Production Safety Rules

These rules are mandatory. The Andromeda backend is live production data.

1. Never write with raw galaxy IDs (`kepler`, `andromeda`, etc.) unless Michael explicitly asks for raw-ID debugging. Use canonical display names in API requests.
2. Always resolve and state the target before mutating: `Your Life → andromeda`, `Your Antidreams → kepler`, etc.
3. Before any create, update, delete, lock, unlock, import, or cleanup, run a read check for the target galaxy and note its current node count.
4. After any mutation, re-read the target galaxy and confirm the new count or changed node.
5. For high-risk operations, also check `Your Antidreams` after the mutation. It should stay empty unless the user explicitly requested an antidream entry.
6. Never use `spaceGraph:seedGalaxy`, bulk imports, `clearGalaxy`, direct Convex mutations, or scripts against production unless Michael explicitly approves the exact galaxy and action in the current conversation.
7. Any bulk operation must first create a timestamped backup of affected nodes and edges.

### Antidreams Hard Guard

`Your Antidreams` is `kepler`. Treat it as protected.

- Do not infer `Your Antidreams` from vague phrasing.
- Do not use `kepler` for life, dreams, family, partner/soulmate, or positive aspiration content.
- Only write to `Your Antidreams` when the user explicitly says `Your Antidreams`, `antidreams`, or `антимечты`.
- If the content reads like a dream, relationship goal, family goal, life goal, or positive aspiration, stop and ask before writing to `Your Antidreams`.
- If nodes appear in `Your Antidreams` unexpectedly, immediately stop, back up `kepler` nodes and edges, report counts, and ask before moving or deleting unless Michael directly asks to clear them.

---

## Node Routes (`/api/andromeda`)

### POST — Create a node

```bash
curl -s -X POST "$BASE_URL/api/andromeda" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"galaxy":"Your Life","title":"Short title","content":"Full message text","nodeType":"STATION"}'
```

### GET — List nodes in a galaxy

```bash
curl -s "$BASE_URL/api/andromeda?galaxy=Your+Life" \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

### PATCH — Update a node

```bash
curl -s -X PATCH "$BASE_URL/api/andromeda" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nodeId":"<id>","title":"New title","content":"New content"}'
```

### DELETE — Delete a node

```bash
curl -s -X DELETE "$BASE_URL/api/andromeda?nodeId=<id>" \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

---

## Galaxy Lock Routes (`/api/andromeda/galaxy`)

### GET — List all galaxy lock states

```bash
curl -s "$BASE_URL/api/andromeda/galaxy" \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

### POST — Lock or unlock a galaxy

```bash
curl -s -X POST "$BASE_URL/api/andromeda/galaxy" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"galaxy":"Your Life","locked":false}'
```

Set `locked: false` to unlock, `locked: true` to lock.

---

## nodeType Options

- `STATION` — main message node
- `RELAY` — connecting or transition node
- `SENSOR` — observation or detail node

---

## Workflow Examples

`Add to Your Dreams: title "Morning Light", content "..."`
Use `POST /api/andromeda`, then confirm the canonical galaxy name.

`Unlock Your Life`
Use `POST /api/andromeda/galaxy` with `{"galaxy":"Your Life","locked":false}`.

`List all nodes in Your Family`
Use `GET /api/andromeda?galaxy=Your+Family`.

`Delete the node with id X`
Use `DELETE /api/andromeda?nodeId=X`.

`Update title of node X to "..."`  
Use `PATCH /api/andromeda` with `{ nodeId, title }`.

---

## Notes

- Changes are live immediately through Convex
- Galaxy lock state lives in the `galaxySettings` table
- Admin UI route: `/admin/andromeda`
