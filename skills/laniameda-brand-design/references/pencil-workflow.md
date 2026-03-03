# Pencil MCP Workflow — Complete Reference

## Tool Overview

Pencil is an MCP-based visual design tool for `.pen` files. Files are encrypted — ONLY access via Pencil MCP tools, never with Read/Grep.

### Available Tools

| Tool | Purpose |
|------|---------|
| `get_editor_state` | Start here — get active file, selection, context |
| `open_document` | Open existing `.pen` or create new (`"new"`) |
| `get_guidelines` | Design rules by topic (landing-page, design-system, etc.) |
| `get_style_guide_tags` | Available style inspiration tags |
| `get_style_guide` | Visual style guide from tags |
| `batch_get` | Read nodes by pattern or ID |
| `batch_design` | Execute insert/copy/update/replace/move/delete operations |
| `get_screenshot` | Visual verification of any node |
| `snapshot_layout` | Check computed layout rectangles |
| `get_variables` | Read design variables |
| `set_variables` | Set/update design variables |
| `find_empty_space_on_canvas` | Find space for new frames |
| `search_all_unique_properties` | Audit colors/fonts across node trees |
| `replace_all_matching_properties` | Bulk property replacement |

---

## Startup Sequence

```
1. get_editor_state(include_schema: true)
2. get_guidelines(topic: "landing-page")
3. get_style_guide_tags() → get_style_guide(tags: [...])
4. set_variables() — register color palette
5. Build reusable components
6. Build screens section by section
7. get_screenshot() after each section for verification
```

---

## batch_design Operation Syntax

Operations use a JavaScript-like syntax. Each line is ONE operation with an optional binding.

### Insert (I)
```javascript
// Insert a node into a parent
myNode=I("parentId", { type: "frame", layout: "vertical", gap: 16 })

// Insert text
title=I(myNode, { type: "text", content: "Hello", fontSize: 48, fontWeight: "800" })

// Insert component instance (ref)
card=I(container, { type: "ref", ref: "componentId", width: "fill_container" })
```

### Update (U)
```javascript
// Update properties of existing node
U("nodeId", { fill: "#fffaf5", padding: 32 })

// Update descendant inside component instance
U("instanceId/descendantId", { content: "New text" })

// Chain with binding
U(myCard+"/titleText", { content: "Updated Title" })
```

### Copy (C)
```javascript
// Copy a node to a new parent
copy=C("sourceId", "parentId", { width: "fill_container" })

// Copy with descendant overrides (MUST use descendants, NOT separate U calls)
card2=C("cardId", container, {
  descendants: {
    "titleId": { content: "Card 2 Title" },
    "descId": { content: "Card 2 description" }
  }
})
```

### Replace (R)
```javascript
// Replace a node inside an instance with a new node
newNode=R("instanceId/slotId", { type: "text", content: "Replaced" })
```

### Delete (D)
```javascript
D("nodeId")
```

### Move (M)
```javascript
// Move node to new parent, optionally at specific index
M("nodeId", "newParentId", 0)
```

### Generate Image (G)
```javascript
// Apply image to a frame (there is no "image" node type)
heroImg=I("parent", { type: "frame", width: 400, height: 300 })
G(heroImg, "ai", "modern workspace")
G("existingFrameId", "stock", "laptop coding")
```

---

## Component Architecture

### Creating Reusable Components

Set `reusable: true` on the root frame:

```javascript
comp=I(document, {
  type: "frame",
  name: "My Component",
  reusable: true,
  layout: "vertical",
  width: 300,
  height: "fit_content",
  fill: "#fffaf5"
})
// Add children
title=I(comp, { type: "text", id: "title", content: "Default Title" })
body=I(comp, { type: "frame", id: "body", placeholder: true })
```

### Using Component Instances

Insert as a `ref`:

```javascript
instance=I(container, { type: "ref", ref: "componentId", width: "fill_container" })
```

### Customizing Instances

Override descendant properties via Update:

```javascript
instance=I(container, { type: "ref", ref: "componentId" })
U(instance+"/title", { content: "Custom Title" })
U(instance+"/body", { fill: "#f7ede2" })
```

---

## Layout Patterns

### Vertical Stack
```javascript
stack=I(parent, {
  type: "frame",
  layout: "vertical",
  gap: 24,
  padding: 32,
  width: "fill_container",
  height: "fit_content"
})
```

### Horizontal Row
```javascript
row=I(parent, {
  type: "frame",
  layout: "horizontal",
  gap: 16,
  alignItems: "center",
  width: "fill_container"
})
```

### Grid (2-column)
```javascript
grid=I(parent, {
  type: "frame",
  layout: "horizontal",
  gap: 16,
  wrap: true,
  width: "fill_container"
})
// Each child at ~half width
item1=I(grid, { type: "frame", width: 580, height: "fit_content" })
item2=I(grid, { type: "frame", width: 580, height: "fit_content" })
```

### Full-width Section
```javascript
section=I(parent, {
  type: "frame",
  layout: "vertical",
  gap: 24,
  padding: [80, 64, 80, 64],  // top, right, bottom, left
  width: "fill_container",
  height: "fit_content",
  fill: "#fffaf5"
})
```

---

## Text Styling in Pencil

### Hero Headline (Inter 800)
```javascript
headline=I(section, {
  type: "text",
  content: "Your agents are only as good as their context.",
  fontSize: 56,
  fontWeight: "800",
  fontFamily: "Inter",
  fill: "#201710",
  letterSpacing: -0.04,
  lineHeight: 1.1,
  width: 700
})
```

### Section Label (Monospace)
```javascript
label=I(section, {
  type: "text",
  content: "// features",
  fontSize: 11,
  fontFamily: "JetBrains Mono",
  fontWeight: "500",
  fill: "#ff7a64",
  letterSpacing: 0.12,
  textTransform: "uppercase"
})
```

### Body Text
```javascript
body=I(section, {
  type: "text",
  content: "Description text here...",
  fontSize: 16,
  fontFamily: "Inter",
  fontWeight: "400",
  fill: "#4c3a2d",
  lineHeight: 1.6,
  width: "fill_container"
})
```

### Display Serif (Italic)
```javascript
display=I(section, {
  type: "text",
  content: "Everything you need.",
  fontSize: 88,
  fontFamily: "Playfair Display",
  fontWeight: "700",
  fontStyle: "italic",
  fill: "#201710",
  lineHeight: 1.0
})
```

---

## Bulk Operations

### Audit Colors
```javascript
search_all_unique_properties({
  parents: ["frameId"],
  properties: ["fillColor", "textColor", "strokeColor"]
})
```

### Bulk Replace Colors (Dark → Light Rework)
```javascript
replace_all_matching_properties({
  parents: ["frameId"],
  properties: {
    fillColor: [
      { from: "#0f0f0f", to: "#fffaf5" },
      { from: "#1a1a1a", to: "#fff4ea" },
      { from: "#18181b", to: "#f7ede2" }
    ],
    textColor: [
      { from: "#ffffff", to: "#201710" },
      { from: "#e0e0e0", to: "#4c3a2d" },
      { from: "#a0a0a0", to: "#7d6755" }
    ]
  }
})
```

**CRITICAL**: After bulk color replacement, manually fix:
1. Terminal window interiors → back to `#0f0f0f` / `#1a1a1a`
2. Traffic light dots → `#ff5f56`, `#ffbd2e`, `#27c93f`
3. Terminal syntax text → coral, green, white
4. Coral badge text → back to `#ffffff`
5. Any element that should remain dark as a contrast focal point

---

## Screenshot Verification Checklist

After taking a screenshot with `get_screenshot`, verify:

- [ ] Background uses paper/surface colors (no pure white)
- [ ] Text hierarchy is clear (ink → secondary → tertiary → ghost)
- [ ] Coral appears sparingly (CTAs, labels, accents only)
- [ ] Monospace labels are uppercase with tracking
- [ ] Terminals have dark interiors with colored syntax
- [ ] Shadows are warm-toned (ink base), not gray
- [ ] Brutalist elements have zero radius
- [ ] Soft elements have 20px radius
- [ ] Spacing feels generous and editorial
- [ ] No visual glitches, overlapping text, or clipped content

---

## Design Variables Setup

Register the palette as Pencil variables at project start:

```javascript
set_variables({
  variables: {
    "paper": { type: "color", value: "#fffaf5" },
    "surface-1": { type: "color", value: "#fff4ea" },
    "surface-2": { type: "color", value: "#f7ede2" },
    "surface-3": { type: "color", value: "#efe2d4" },
    "ink": { type: "color", value: "#201710" },
    "text-secondary": { type: "color", value: "#4c3a2d" },
    "text-tertiary": { type: "color", value: "#7d6755" },
    "text-ghost": { type: "color", value: "#ab9381" },
    "coral": { type: "color", value: "#ff7a64" },
    "coral-hover": { type: "color", value: "#ff917d" },
    "inverse-bg": { type: "color", value: "#18181b" },
    "inverse-text": { type: "color", value: "#fafafa" }
  }
})
```

---

## Performance Tips

- **Max 25 operations per batch_design call** — split large sections across calls
- **Build components first** — reuse saves operations later
- **Use fill_container width** for responsive-like behavior
- **Take screenshots periodically** — catching errors early saves rework
- **Use bindings** for parent references within the same batch
- **Don't U() descendants of C() nodes** — use `descendants` property in Copy instead
