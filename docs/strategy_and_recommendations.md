# Strategy and Recommendations

## Why these 2 tests were automated

### 1. E2E UI: valid single bet placement with receipt verification
I chose this because it is the shortest end-to-end path that exercises the highest business value:
- match discovery
- selection state
- stake entry
- place bet action
- asynchronous resolution
- success receipt integrity

A failure here means the product’s main user promise is broken.

### 2. API: reject stake with more than 2 decimal places
I chose this because it targets a money rule that is:
- business critical
- deterministic
- fast to execute
- better validated directly at the API layer than through the UI only

This also gives the automation suite useful layer coverage instead of duplicating the same assertion twice through the browser.

## What I intentionally left manual only

### Error modal UX and retry behavior
This is highly valuable, but I would keep first coverage manual until the product team clarifies:
- exact retry semantics
- duplicate prevention expectations
- whether state should persist visually between failure and retry

### Filters UX
Date and odds filters are important, but not as critical as the transaction path. They are also more likely to change in UX details, so I would initially keep them manual while the feature stabilizes.

### Exploratory checks around presentation and readability
Copy quality, visual layout issues, and cross-surface balance readability are best caught with quick focused exploratory passes.

## Top recommendations if the project scales

### 1. Add API contract checks and test data control in CI
- Run API smoke and validation suites on every pull request.
- Seed or reset user data before each run.
- Add schema assertions for `/matches`, `/balance`, `/place-bet`, and `/reset-balance`.

### 2. Introduce stable test selectors and clearer state hooks
- Add `data-testid` attributes for odds buttons, bet slip fields, modals, and receipt rows.
- Expose deterministic hooks for loading, success, and error states.
- This will make UI automation more maintainable and less flaky.

### 3. Clarify the specification before expanding coverage
Highest priority clarifications:
- minimum stake value (`€1.00` vs `€1.01`)
- payout rounding and currency formatting
- retry behavior and duplicate submission rules
- exact filter behavior for empty-result and invalid-range states

With those clarified, I would next automate:
- insufficient balance API and UI checks
- no-selection UI guardrail
- 409 bet-in-progress concurrency scenario
- reset-balance contract test
