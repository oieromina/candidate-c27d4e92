# Execution Results and Bug Reports

## Scope executed
Top scenarios executed conceptually from the prioritized plan:
- TP-01 Valid single bet placement
- TP-02 Stake validation boundaries
- TP-05 Error handling / retry path

Also performed targeted exploratory checks around selection replacement, balance consistency, and receipt content integrity.

## Test execution summary

| Scenario ID | Result | Notes |
|---|---|---|
| TP-01 | Pass with watch items | Core flow should succeed; verify all receipt fields and post-close cleared state in live run. |
| TP-02 | Mixed | Money validation is high risk; boundary and precision checks should be validated in both UI and API. |
| TP-05 | Risk identified | Retry / close semantics deserve focused coverage because they can cause duplicate submissions or stranded state. |

> Note: This document is structured as an interview-style execution report. Final pass/fail should be confirmed against a live run of the target environment.

## Bug reports

### BUG-01 — Stake minimum value is inconsistent between business rules and validation table
**Severity:** High  
**Reproduction steps**
1. Review the feature specification.
2. Compare the business rules section with the validation table.

**Expected result**
- The minimum stake should be defined consistently across the specification.

**Actual result**
- Business rules state **Stake min = €1.00**, while the validation table states **Minimum €1.01**, and the minimum UI copy says **Minimum stake is €1.00**.

**Business impact**
- Conflicting requirements make it impossible to determine the correct expected behavior, leading to flaky tests, mismatched UI/API validation, and possible production disputes for rejected bets.

**Evidence**
- Spec discrepancy across sections 3, 4.1, and 4.4.

---

### BUG-02 — Close behavior requirement conflicts with receipt state-clearing requirement
**Severity:** Medium  
**Reproduction steps**
1. Review success receipt behavior and error modal close behavior in the specification.
2. Compare state-clearing expectations after each modal closes.

**Expected result**
- Modal close behaviors should be fully unambiguous and consistent about whether stake and selection persist or clear.

**Actual result**
- Success receipt says closing returns to the main flow without active selection.
- Error modal says **Close** clears current selection/stake, while **Rebet** retries placement.
- It is not explicitly stated whether values remain visible before retry, whether retry reuses the same stake, or how duplicate submissions are prevented during in-progress state.

**Business impact**
- Ambiguity can create duplicate bets, user confusion, and inconsistent automation assertions.

**Evidence**
- Functional requirements sections 2.3, 2.4, and 2.5.

---

### BUG-03 — Missing explicit contract for rounding and currency formatting of payout
**Severity:** Medium  
**Reproduction steps**
1. Review the payout definition and API contract.
2. Look for required rounding behavior when stake × odds produces more than 2 decimal places.

**Expected result**
- Specification should define rounding precision and format for payout in UI and API.

**Actual result**
- Payout is defined as stake × odds, but no explicit rounding rule is given for receipt, API response, or balance presentation.

**Business impact**
- Different layers may show different payout amounts, causing trust and reconciliation issues.

**Evidence**
- Feature spec section 2.4 and API contract in section 5.3.

## Quick exploratory notes

- Selection replacement should be stress-tested across different matches, not only within the same match row.
- The 409 “bet already in progress” rule deserves concurrent request testing, even if the UI usually serializes requests.
- The spec says odds are static for the session, so refreshing or re-querying mid-session should not change displayed odds for already loaded events.
