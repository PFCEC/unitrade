---
name: unitrade-quickstart
description: Help first-time Unitrade API users quickly choose the right public component and generate correct starter code for login, product/contract lookup, domestic futures quotes, order workflows, account queries, callbacks, server status, and troubleshooting. Use when the user asks how to start with Unitrade, asks which documented Unitrade component or method to use, wants examples based on the public Unitrade docs/tutorials, or needs help fixing login/order/query errors.
---

# Unitrade Quickstart

Help the user get working Unitrade code quickly, especially when they are new to the components.

## Default Workflow

1. Identify the user's target: login/setup, product lookup, quote snapshot, quote subscription, order, account query, connection/server status, or troubleshooting.
2. Choose the component before writing code:
   - `api`: login/logout, accounts, products, contracts, exchanges.
   - `api.dquote`: domestic futures/options quote.
   - `api.dtrade`: domestic futures/options order and order/match query.
   - `api.ftrade`: foreign futures/options order and order/match query.
   - `api.daccount`: domestic futures account, margin, position, unliquidated positions, combine/net operations.
   - `api.faccount`: foreign futures account, margin, position, unliquidated positions.
3. For a first-time user, start with import, `Unitrade()` initialization, `on_error`, `login`, `login_response.ok`, `api.login_status_flag`, and `api.get_accounts()`.
4. Prefer the variable name `api` in examples. The source docs sometimes use `unitrade`; keep generated examples consistent.
5. Use placeholders or environment variables for URL, account, password, certificate path, and certificate password. Do not hardcode real credentials.
6. Show the smallest complete example that proves the target component works, then mention the next component-specific method if relevant.
7. Treat this public skill as authoritative for documented components. Do not invent or describe quote components that are absent from its component map.

## Load References

Read only the reference needed for the request:

- `${CLAUDE_SKILL_DIR}/references/api-map.md`: component selection, method index, callbacks, return objects, important naming caveats.
- `${CLAUDE_SKILL_DIR}/references/tutorial-recipes.md`: ready-to-adapt code flows distilled from the tutorials.
- `${CLAUDE_SKILL_DIR}/references/troubleshooting.md`: login/order/query failures, error codes, maintenance windows, time format.
- `${CLAUDE_SKILL_DIR}/assets/templates/unitrade_starter.py`: starter script for login, account list, product lookup, and a safe quote check.
- `${CLAUDE_SKILL_DIR}/assets/templates/domestic_futures_test_order.py`: guarded domestic futures order template; it does not send unless the user explicitly enables the confirmation flag.

## Safety Rules

- Do not provide trading advice or recommend specific trades. Treat order code as API mechanics only.
- Before generating order code, make clear whether the example is for test or production. Default to test-style placeholders.
- Register `on_reply` and `on_match` callbacks before sending order examples.
- Use a guard or explicit confirmation variable in templates that can send orders.
- For live order requests, ask the user to confirm environment, account, product, side, quantity, price type, and order condition before producing final runnable code.
- Explain `B/S`, `M/L`, `IOC/ROD/FOK`, open/close, and day-trade flags near any order object.

## Response Style

- Answer in the user's language. Use Traditional Chinese for Chinese requests.
- Start with the chosen component and why.
- Give code first when the user asks to implement or wants an example.
- After code, list the checks to run: login status, accounts, response `ok`/`issend`, `error`/`errormsg`, callback output.
- When docs have inconsistent spelling, call it out briefly and show a defensive snippet.
