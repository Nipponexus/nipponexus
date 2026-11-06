# Nipponexus calendar structure proposal (2026-11-07)

Key: NX4_CALENDAR_STRUCTURE_PROPOSAL_20261107 / source: nds_structure_lab_20261106_094451 (reused, not rerun)

## 1. files and connection points
```json
{
  "production_files_touched_on_approval": [
    "scripts/nxapply.py (one import dispatch line for structural check11)",
    "new manual type/evidence sidecar file (independent module, import-only connection)",
    "out/ evidence sidecar path per qid"
  ],
  "untouched": [
    "scripts/nxcheck.py",
    "scripts/nxmido.py",
    "checks1-10, rights/factual/existing gates",
    "steps/*",
    "data/sqlite/nipponexus.db",
    "site/*"
  ],
  "connection_shape": "PROVISIONAL single import dispatch; no classifier platform"
}
```

## 2. festival routing back conditions
```json
{
  "rule": "Festival evidence overrides calendar declaration.",
  "on_conflict": "verdict REVIEW_REQUIRED; festival keeps its ORIGINAL strict route (no calendar-based relaxation)",
  "unknown_or_mixed": "REVIEW_REQUIRED"
}
```

## 3. misclassification safeguards
```json
{
  "no_qid_allowlist": true,
  "requirement": "explicit type + bound text/source evidence + human review record; concept alone insufficient",
  "machine_checks": "literal span/excerpt bindings only; no semantic or network verification at machine layer"
}
```

## 4. semantic limits
```json
{
  "no_semantic_pass": true,
  "sources_are_supplied_evidence_not_verified_truth": true,
  "synthetic_tests_labeled": "LAB_SYNTHETIC",
  "na_rule": "NOT_APPLICABLE_WITH_REASON requires reason + evidence and remains pending review; exceptions are ERROR",
  "fixed_cases": "Real Hangesho (Q11406993) unchanged original strict NG; diagnosis C is primary fix, heading-only B is not a fix; date_guard concept exclusion is not calendar evidence"
}
```

## 5. verdict changes before after
```json
{
  "before": "original strict verdicts only (PASS/FAIL per nxmido strict)",
  "after": [
    "structural_ready_pending_evidence_review",
    "FAIL",
    "REVIEW_REQUIRED",
    "NOT_APPLICABLE_WITH_REASON",
    "ERROR",
    "FESTIVAL_EXISTING_ROUTE"
  ],
  "invariant": "no semantic PASS is introduced; existing FAILs unchanged (e.g. Hangesho strict FAIL preserved)"
}
```

## 6. no wrong fail and exempt confirmation scope
```json
{
  "suite": "46 cases, expected_actual_matches 46/46",
  "error_outcomes_expected": 1,
  "unexpected_errors": 0,
  "production_pass_count": 0,
  "real_cases": [
    {
      "qid": "Q11406993",
      "label": "半夏生",
      "original_nxmido": "FAIL",
      "strict": "FAIL"
    },
    {
      "qid": "Q115680256",
      "label": "横手の雪まつり",
      "original_nxmido": "FAIL",
      "strict": "FAIL"
    },
    {
      "qid": "Q774193",
      "label": "久喜の提灯祭り・天王様",
      "original_nxmido": "FAIL",
      "strict": "FAIL"
    }
  ],
  "nxcheck_direct": {
    "exit_code": 0,
    "pass": "8/8"
  }
}
```

## 7. rollback procedure
```json
{
  "steps": "remove the single import dispatch line; delete sidecar module; git revert of the single approval commit",
  "isolation_evidence": "freeze_before/after manifest sha256 identical (c0c0d7a27ee5...), changed=[] , new_protected_files=[]",
  "verification_file": "lab verification.json (timestamp 2026-11-06T09:47:08.663502+09:00)"
}
```

## 8. minimal scope
```json
"DESIGN_ONLY_BEFORE_IMPLEMENTATION. No production writes/imports/jobs/API/AI/commit/build/publication; B footer/site untouched. Future integration is one import dispatch plus manual sidecar only."
```

## 9. not an approval
```json
"This document is a PROPOSAL. Deployment remains blocked pending explicit approval by NDS representative. No approval is granted or implied by this record."
```

This is a proposal, not an approval. (Section 9 restated in prose.)