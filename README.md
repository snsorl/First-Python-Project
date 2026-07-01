# Tiny Python + Vanilla JS Full-Stack Starter

The simplest possible full-stack app: **Python (Flask) backend + SQLite database + vanilla HTML/JS frontend.**

## Run it

```bash
pip install flask flask-cors
python app.py
```

Open http://localhost:5000

## What's where

| File | Role | Java analog |
|---|---|---|
| `app.py` | Python backend — defines API routes, talks to SQLite | A Spring Boot `@RestController` + `JdbcTemplate` |
| `index.html` | Home page with a button that navigates | A JSP / Thymeleaf template |
| `messages.html` | Page with input + list, talks to backend via `fetch()` | Same |
| `style.css` | Styling | Same |
| `data.db` | SQLite file (created on first run) | Your H2/Postgres DB |

## How a request flows (the whole point of "full-stack")

1. You type in the input → click **Save**
2. JS `fetch("/api/messages", { method: "POST", body: {...} })` → HTTP request leaves the browser
3. Flask matches the URL to `@app.post("/api/messages")` in `app.py`
4. Python runs `INSERT INTO messages ...` against SQLite
5. Python returns JSON → JS receives it → re-renders the list

## Java → Python quick notes

- No `;` at end of lines. Indentation = blocks (no `{ }`).
- `def func():` instead of `public void func()`. No type declarations required.
- `dict` = `HashMap`, `list` = `ArrayList`, `None` = `null`, `True/False` capitalized.
- Decorators like `@app.get("/...")` are like Java annotations (`@GetMapping`).
- `pip` = `maven/gradle` (installs packages from PyPI).

## Next steps

- Add a `DELETE /api/messages/<id>` endpoint and a delete button.
- Add a second table (e.g. `users`) and a JOIN.
- Swap SQLite for Postgres (change the connection, SQL stays nearly identical).
- Try FastAPI instead of Flask (modern, async, auto-generates API docs).
