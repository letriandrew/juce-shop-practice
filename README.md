# 🧃 OWASP Juice Shop: Security Lab & Tracker

Welcome to my personal hacking lab for the **OWASP Juice Shop**. This repository tracks my progress through the 172 challenges, stores the custom tools I've built, and documents my learning journey.

---

## 📊 Master Progress
**Challenges Completed:** `1 / 172`  
`[▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]` **0.5%**

---

## 🛠️ Tool Chest
A collection of custom scripts and tools used during my penetration testing.

| Tool Name | Language | Purpose & Functionality |
| :--- | :---: | :--- |
| `js-miner.py` | Python | Automatically crawls JS files to find hidden routes and API endpoints via Regex. |
| `your-tool-here.py` | Python | Describe what your next tool does here. |

---

## 🗒️ Challenge Log

| # | Challenge Name | Status | Difficulty | Description, Experience & Thoughts |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Score Board** | ✅ | ⭐ | **Desc:** Find the hidden score board page.<br>**Exp:** I found this by searching the client-side JS code for `path: "score-board"`. It taught me that hiding a URL in the code isn't the same as securing it. |
| **2** | **Example Name** | 🚧 | ⭐⭐ | **Desc:** Briefly describe the goal.<br>**Exp:** Write what you tried, what failed, and how you eventually got it. |
| **3** | **Next Target** | ❌ | ? | **Thoughts:** Notes on what you plan to try next. |

> *Self-Correction: Add rows as you go by copying the empty template below.*
> `| # | Name | ❌ | ⭐ | Desc/Exp |`

---

## 🧠 Key Learnings & Methodology
*Record high-level takeaways that apply to multiple categories here.*

* **Client-Side Exposure:** Modern SPAs (Angular/React) often leak the entire site map in the main JavaScript bundle.
* **Broken Access Control:** Just because a link is missing from the menu doesn't mean the page is protected. Server-side validation is the only true fix.
* **Methodology:** Start with `Inspect Element` -> `Sources` -> `Global Search (Ctrl+Shift+F)` to map the "hidden" surface area.

---

## 📂 Repository Structure
* `/savefiles`: JSON save files for locally ran OWASP Juice Shop site.
* `/tools`: My custom Python and Bash scripts.
* `/notes`: Detailed walkthroughs of complex 5-star and 6-star challenges.
* `/screenshots`: Proof of pwnage for the record.

---
*Created by [letriandrew] - 2026*