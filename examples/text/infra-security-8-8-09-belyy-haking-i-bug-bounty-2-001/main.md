## Summary
Any authenticated user can export billing data of another organization
by changing the numeric `org_id` in POST /api/v2/reports/export.

## Steps to reproduce
1. Log in as user-a@test.example.com (org 100).
2. Intercept POST /api/v2/reports/export with Burp.
3. Replace `"org_id":100` with `"org_id":101`.
4. Observe HTTP 200 and CSV containing PII of org 101.

## Impact
Broken Access Control — confidentiality of all customers in other tenants (GDPR-relevant).

## Remediation
Authorize org_id against session membership on server side.

## Supporting material
- request-export-org101.http (attached)
- screen-recording.mp4 (90s)
