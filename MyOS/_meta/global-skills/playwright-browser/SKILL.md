---
name: playwright-browser
description: Automate browser interactions, DOM scraping, form submission, and end-to-end verification using Playwright MCP.
---

# Playwright Browser Automation Skill

Use this skill when you need headless browser automation, UI flow verification, form submissions, or live DOM inspection via Playwright MCP tools.

## Core Rules

1. **Snapshot-First Navigation:**
   - Always run a snapshot or accessibility tree inspection after navigating to an unfamiliar page before clicking or filling inputs.
   - Prefer stable accessibility attributes (`role`, `aria-label`, placeholder text, label associations) over fragile CSS selectors or dynamic hash classes.

2. **Wait for State Settle:**
   - Always verify navigation or AJAX responses have finished before proceeding to subsequent clicks.
   - Avoid hardcoded sleeps; wait for specific elements or network conditions to resolve.

3. **Capture Visual Evidence on Failures:**
   - When a test, assertion, or unexpected page state occurs, immediately call `browser_take_screenshot` to document the state before terminating the browser instance.

4. **Resource Hygiene:**
   - Always gracefully close pages and browser contexts once the task or test scenario has completed to prevent orphaned Chromium processes from draining CPU and memory.

