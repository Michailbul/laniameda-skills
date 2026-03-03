#!/usr/bin/env python3
"""
notion-sync — read/write tasks and content ideas in Notion.

WRITE — Task:
  sync.py --name "..." --status "..." --agent "..." --priority "..." --department "Marketing|Dev|Operations" [--area "..."] [--notes "..."]

WRITE — Content Idea:
  sync.py --content-idea --name "..." --pillar "..." --format "..." [--source-url "..."] [--draft-path "..."] [--notes "..."] [--draft-body "full copy text"]

WRITE — Approve an idea (set status + link marketing task):
  sync.py --approve --name "..." [--task-id "notion-page-id"]

QUERY — List items needing attention:
  sync.py --query --department "Marketing"            # pending Review tasks
  sync.py --query --content-ideas --status "Review"   # ideas awaiting approval
  sync.py --query --content-ideas --status "Approved" # ideas ready to produce

UPDATE — Change status of an idea:
  sync.py --update-idea --name "..." --status "In Production"
"""
import json, urllib.request, urllib.error, argparse, os, sys
from datetime import date

KEY_FILE = os.path.expanduser("~/.config/notion/api_key")
DB_IDS = {
    "Marketing":    "316e9215-3d4b-8155-94c3-deaff31903a1",
    "Dev":          "316e9215-3d4b-817c-874d-cb9bdd9391c9",
    "Operations":   "316e9215-3d4b-8148-a0a7-f1bfa318a3ca",
    "ContentIdeas": "317e9215-3d4b-8146-a4ab-e09312ec1c89",
}
PRIORITY_MAP = {"High": "🔴 High", "Medium": "🟡 Medium", "Low": "🟢 Low"}

def api(method, path, body=None):
    key = open(KEY_FILE).read().strip()
    headers = {"Authorization": f"Bearer {key}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(f"https://api.notion.com/v1{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"API error {e.code}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)

def find_page(db_id, name):
    result = api("POST", f"/databases/{db_id}/query", {
        "filter": {"property": "Name", "title": {"equals": name}}
    })
    pages = result.get("results", [])
    return pages[0]["id"] if pages else None

def get_prop_text(props, key):
    p = props.get(key, {})
    t = p.get("type")
    if t == "title":   return "".join(x["text"]["content"] for x in p.get("title", []))
    if t == "rich_text": return "".join(x["text"]["content"] for x in p.get("rich_text", []))
    if t == "select":  return (p.get("select") or {}).get("name", "")
    if t == "date":    return (p.get("date") or {}).get("start", "")
    return ""

def query_db(db_id, status_filter=None):
    body = {}
    if status_filter:
        body["filter"] = {"property": "Status", "select": {"equals": status_filter}}
    body["sorts"] = [{"property": "Name", "direction": "ascending"}]
    result = api("POST", f"/databases/{db_id}/query", body)
    return result.get("results", [])

def write_page_body(page_id, text):
    """Write draft copy as blocks into a Notion page body."""
    chunks = [text[i:i+2000] for i in range(0, len(text), 2000)]
    blocks = [{"object":"block","type":"divider","divider":{}}]
    blocks.append({"object":"block","type":"heading_3","heading_3":{"rich_text":[{"type":"text","text":{"content":"Draft Copy"}}]}})
    for chunk in chunks:
        blocks.append({"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":chunk}}]}})
    api("PATCH", f"/blocks/{page_id}/children", {"children": blocks})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",          default="")
    parser.add_argument("--content-idea",  action="store_true")
    parser.add_argument("--approve",       action="store_true", help="Set idea status to Approved")
    parser.add_argument("--update-idea",   action="store_true", help="Update status of an existing idea")
    parser.add_argument("--query",         action="store_true", help="Read items from Notion")
    # Task fields
    parser.add_argument("--status",     choices=["Idea","Research","In Progress","Review","Done",
                                                  "Draft","Approved","In Production","Posted"])
    parser.add_argument("--agent",      choices=["Lani","Meda","Persey","Michael","All"], default="Meda")
    parser.add_argument("--priority",   choices=["High","Medium","Low"], default="Medium")
    parser.add_argument("--department", choices=["Marketing","Dev","Operations"])
    parser.add_argument("--area",       default="")
    parser.add_argument("--notes",      default="")
    # Content Idea fields
    parser.add_argument("--pillar",     choices=["AI Creatorship","Cinematic Frames","Web Design + AI",
                                                  "Generative AI Tools","Building in Public",
                                                  "Marketing-First","AI Engineering"])
    parser.add_argument("--format",     choices=["X Post","X Thread","LinkedIn","Instagram Caption",
                                                  "Carousel","Newsletter"])
    parser.add_argument("--source-url", default="")
    parser.add_argument("--draft-path", default="")
    parser.add_argument("--draft-body", default="", help="Full draft copy — written into page body")
    parser.add_argument("--task-id",    default="", help="Marketing task page ID to link to an idea")
    # Query fields
    parser.add_argument("--content-ideas", action="store_true", help="Query content ideas DB")
    args = parser.parse_args()

    # ── QUERY ──
    if args.query:
        if args.content_ideas:
            db_id = DB_IDS["ContentIdeas"]
            status = args.status or "Review"
            pages = query_db(db_id, status)
            if not pages:
                print(f"No content ideas with status '{status}'")
                return
            print(f"\nContent Ideas — {status} ({len(pages)} items):\n")
            for p in pages:
                props = p["properties"]
                name    = get_prop_text(props, "Name")
                pillar  = get_prop_text(props, "Pillar")
                fmt     = get_prop_text(props, "Format")
                notes   = get_prop_text(props, "Notes")[:120]
                draft   = get_prop_text(props, "Draft Path")
                print(f"  [{pillar}] [{fmt}] {name}")
                if notes: print(f"    Notes: {notes}...")
                if draft: print(f"    Draft: {draft}")
                print()
        else:
            dep = args.department or "Marketing"
            db_id = DB_IDS[dep]
            status = args.status or "Review"
            pages = query_db(db_id, status)
            print(f"\n{dep} Tasks — {status} ({len(pages)} items):\n")
            for p in pages:
                props = p["properties"]
                name   = get_prop_text(props, "Name")
                agent  = get_prop_text(props, "Agent")
                notes  = get_prop_text(props, "Notes")[:100]
                print(f"  [{agent}] {name}")
                if notes: print(f"    {notes}...")
                print()
        return

    # ── UPDATE IDEA STATUS ──
    if args.update_idea:
        pid = find_page(DB_IDS["ContentIdeas"], args.name)
        if not pid:
            print(f"Idea not found: {args.name}", file=sys.stderr); sys.exit(1)
        api("PATCH", f"/pages/{pid}", {"properties": {
            "Status": {"select": {"name": args.status}}
        }})
        print(f"✅ Updated idea status: {args.name} → {args.status}")
        return

    # ── APPROVE ──
    if args.approve:
        pid = find_page(DB_IDS["ContentIdeas"], args.name)
        if not pid:
            print(f"Idea not found: {args.name}", file=sys.stderr); sys.exit(1)
        props = {"Status": {"select": {"name": "Approved"}}}
        if args.task_id:
            props["Marketing Task"] = {"relation": [{"id": args.task_id}]}
        api("PATCH", f"/pages/{pid}", {"properties": props})
        print(f"✅ Approved: {args.name}")
        return

    # ── CONTENT IDEA ──
    if args.content_idea:
        db_id = DB_IDS["ContentIdeas"]
        props = {
            "Name":   {"title": [{"text": {"content": args.name}}]},
            "Status": {"select": {"name": "Idea"}},
            "Added":  {"date": {"start": str(date.today())}},
            "Agent":  {"select": {"name": args.agent}},
        }
        if args.pillar:      props["Pillar"]    = {"select": {"name": args.pillar}}
        if args.format:      props["Format"]    = {"select": {"name": args.format}}
        if args.source_url:  props["Source URL"] = {"url": args.source_url}
        if args.priority:    props["Priority"]  = {"select": {"name": PRIORITY_MAP[args.priority]}}
        if args.draft_path:  props["Draft Path"] = {"rich_text": [{"text": {"content": args.draft_path}}]}
        if args.notes:       props["Notes"]     = {"rich_text": [{"text": {"content": args.notes[:2000]}}]}

        existing_id = find_page(db_id, args.name)
        if existing_id:
            api("PATCH", f"/pages/{existing_id}", {"properties": props})
            page_id = existing_id
            print(f"✅ Updated [Content Idea]: {args.name}")
        else:
            r = api("POST", "/pages", {"parent": {"database_id": db_id}, "properties": props})
            page_id = r["id"]
            print(f"✅ Created [Content Idea]: {args.name}")

        if args.draft_body:
            write_page_body(page_id, args.draft_body)
            print(f"   Draft copy written to page body ✓")
        return

    # ── TASK ──
    if not all([args.status, args.department]):
        print("Error: --status and --department required for tasks", file=sys.stderr); sys.exit(1)
    db_id = DB_IDS[args.department]
    props = {
        "Name":     {"title": [{"text": {"content": args.name}}]},
        "Status":   {"select": {"name": args.status}},
        "Agent":    {"select": {"name": args.agent}},
        "Priority": {"select": {"name": PRIORITY_MAP[args.priority]}},
        "Updated":  {"date": {"start": str(date.today())}},
    }
    if args.area:  props["Area"]  = {"rich_text": [{"text": {"content": args.area}}]}
    if args.notes: props["Notes"] = {"rich_text": [{"text": {"content": args.notes[:2000]}}]}

    existing_id = find_page(db_id, args.name)
    if existing_id:
        api("PATCH", f"/pages/{existing_id}", {"properties": props})
        print(f"✅ Updated [{args.department}]: {args.name}")
    else:
        api("POST", "/pages", {"parent": {"database_id": db_id}, "properties": props})
        print(f"✅ Created [{args.department}]: {args.name}")

if __name__ == "__main__":
    main()
