# Test Plan — Single Bet Placement

Source inputs reviewed:
- Feature specification for Single Bet Placement
- Assignment brief and betting domain notes

## TP-01 — Place a valid single pre-match bet and verify receipt integrity
**Priority:** Critical  
**Risk rationale:** This is the core revenue path. Failure here blocks primary user value and undermines trust in monetary transactions.

**Steps**
1. Open the application with the provided user id.
2. Confirm upcoming football matches are displayed.
3. Select one valid outcome for a match.
4. Enter a valid stake, e.g. `€10.00`.
5. Click **Place Bet**.
6. Wait for the final resolved outcome.
7. Review the success receipt.
8. Close the receipt.

**Expected result**
- One selection is active in the bet slip.
- Place Bet enters loading state and resolves successfully.
- Stake is deducted from balance.
- Success receipt shows Bet ID, match details, selection, stake, odds at placement, payout, and placement timestamp.
- Closing the receipt returns the user to the main flow with no active selection.

---

## TP-02 — Enforce stake boundaries and precision at UI and API level
**Priority:** Critical  
**Risk rationale:** Stake validation protects money handling, fraud risk, and reconciliation accuracy. Boundary defects here have direct financial impact.

**Steps**
1. Select any valid match outcome.
2. Enter each of the following values one by one and attempt to place a bet: blank, text, `0`, `1`, `0.99`, `100`, `100.01`, `10.123`.
3. Observe UI feedback and API responses where applicable.

**Expected result**
- Blank stake is blocked.
- Non-numeric stake is rejected.
- Values below minimum are rejected with minimum message.
- Values above maximum are rejected with maximum message.
- More than 2 decimals are rejected.
- Valid values within range and precision rules are accepted.

---

## TP-03 — Prevent betting without a valid selection or with invalid selection replacement behavior
**Priority:** High  
**Risk rationale:** Incorrect selection state can place the wrong outcome, which is a severe trust and settlement issue.

**Steps**
1. Open the page and do not select any odds.
2. Attempt to place a bet with a valid stake.
3. Select one outcome.
4. Select another outcome for the same or another match.
5. Observe bet slip state.
6. Remove the selection with per-selection remove or Remove All.

**Expected result**
- Bet cannot be placed without a selection.
- Only one active selection exists at a time.
- New selection replaces the previous selection.
- Remove controls clear the selection cleanly.

---

## TP-04 — Validate insufficient balance handling and balance consistency
**Priority:** High  
**Risk rationale:** Inconsistent balance state causes failed bets, accounting discrepancies, and user support incidents.

**Steps**
1. Check starting balance.
2. Attempt a stake greater than the current balance.
3. Place a valid smaller bet.
4. Compare displayed header balance, bet slip balance, and API balance.
5. Reset balance through the API and re-check consistency.

**Expected result**
- Oversized stake is rejected with insufficient balance messaging.
- After a successful bet, all balance surfaces show the same deducted amount.
- Reset returns persisted state and response body consistently to the initial configured value.

---

## TP-05 — Error modal and retry path when placement fails
**Priority:** High  
**Risk rationale:** Payments-like actions need reliable recovery. Broken retry/close behavior can duplicate bets or strand users in an uncertain state.

**Steps**
1. Trigger a bet placement failure condition.
2. Observe the error modal.
3. Click **Rebet**.
4. Trigger another failure and use **Close** or the top-right **X**.

**Expected result**
- Error modal title is **Something went wrong**.
- Body explains the failure and suggests trying again.
- **Rebet** closes the modal and retries placement.
- **Close** and top-right **X** close the modal and clear current selection and stake.

---

## TP-06 — Filters: inclusive date range and odds validation
**Priority:** Medium  
**Risk rationale:** Filtering is not core settlement logic, but it affects discoverability and can hide valid events or mislead users into betting the wrong market set.

**Steps**
1. Apply a single-day date filter.
2. Apply an inclusive multi-day range.
3. Apply min/max odds range values at boundaries.
4. Enter an invalid odds range such as min > max.

**Expected result**
- Single-day and date-range filters include matching dates inclusively.
- Odds filter applies inclusively.
- Invalid ranges are rejected with clear feedback.
- Results stay limited to upcoming football matches only.
