# QA & Test Automation Portfolio

Selenium automation, API testing, and performance testing scripts built while
learning QA, using Daraz, a personal expense tracker app (Mero Kharcha), and
the JSONPlaceholder public API as test targets.

## selenium_automation/
- `daraz_search_test.py` — Automated test verifying Daraz product search returns relevant results, using explicit waits and locator strategies (ID, XPath).
- `mero_kharcha_nav_test.py` — Automated test that fills and submits the Add Expense form in Mero Kharcha, confirming the action completes without error.
- `complete_mero_kharcha_automation.py` — End-to-end automated suite covering registration, login, adding an expense, and verifying it appears correctly in View Expenses.

## postman_api_tests/
- `JSONPlaceholder API Tests.postman_collection.json` — API test suite for JSONPlaceholder covering status code, response time, content-type, field presence/type, and exact value assertions; includes review and correction of AI (Postbot)-generated tests.

## jmeter_load_test/
- `jmeter_posts_load_test.jmx` — Load test simulating 10 concurrent users against the JSONPlaceholder /posts endpoint, measuring average response time, error rate, and throughput.
