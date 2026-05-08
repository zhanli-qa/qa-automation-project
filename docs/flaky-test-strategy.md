# Flaky Test Strategy

## 1. What is a Flaky Test?

A flaky test is a test that sometimes passes and sometimes fails without any code changes.

Flaky tests reduce confidence in automation results and may block CI/CD pipelines even when the application is working correctly.

---

## 2. Common Causes

Common causes of flaky tests include:

- Timing issues
- Network instability
- Slow page loading
- Unstable test data
- Test dependency between cases
- Asynchronous UI behavior
- Environment instability
- External service dependency

---

## 3. Detection Strategy

Flaky tests can be identified by:

- Reviewing tests that pass after retry
- Checking failed test history in CI
- Comparing local execution and CI execution results
- Monitoring tests that fail intermittently without code changes
- Reviewing Allure reports, screenshots, logs, and error messages

A test that passes only after retry should still be treated as a potential flaky test and investigated.

---

## 4. Classification

Flaky tests are classified based on root cause:

### UI Timing Flakiness

Usually caused by elements not being ready, page loading delays, or incorrect waiting strategy.

Examples:

- Button is clicked before it is fully visible
- Assertion runs before page navigation completes

### Test Data Flakiness

Usually caused by shared, outdated, or polluted test data.

Examples:

- A user already exists
- Cart data is not cleaned before the next test

### Environment Flakiness

Usually caused by slow CI machines, unstable network, or temporary service issues.

Examples:

- API timeout in CI but passes locally
- Page loads slower in GitHub Actions

### Test Design Flakiness

Usually caused by test dependency or poor test isolation.

Examples:

- One test depends on the result of another test
- Tests must run in a specific order to pass

---

## 5. Mitigation / Fix Strategy

Flaky tests should be fixed based on their root cause.

### UI Timing Fixes

- Use Playwright auto-waiting and locator assertions
- Avoid hard-coded sleep
- Wait for meaningful UI state
- Use stable locators such as role, test id, or clear CSS selectors

Example:

    expect(page.locator(".title")).to_have_text("Products")

### Test Data Fixes

- Use isolated test data
- Avoid sharing mutable data between tests
- Create unique data when needed
- Clean up data after test execution when applicable
- Avoid relying on test data created by previous test cases

### Environment Fixes

- Add timeout configuration where appropriate
- Use logs and screenshots for failure investigation
- Separate real product bugs from infrastructure failures
- Compare local execution results with CI execution results

### Test Design Fixes

- Keep tests independent
- Avoid test order dependency
- Use setup and teardown properly
- Do not rely on previous test execution results
- Keep assertions focused and clear

---

## 6. Retry Policy

Retry is used only as a temporary safety mechanism, not as a replacement for fixing flaky tests.

In this project, retries may be applied selectively to known flaky UI tests.

Example:

    import pytest

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_add_to_cart(inventory_page):
        ...

Command-line retry can also be used during investigation:

    pytest ui/tests --reruns 2 --reruns-delay 1

If a test passes only after retry, it should be reviewed and investigated.

---

## 7. CI Stability Strategy

To improve CI stability:

- Run smoke tests first
- Keep high-risk tests stable and isolated
- Use retries carefully for known flaky UI tests
- Review logs, screenshots, and Allure reports for failed runs
- Track repeated flaky failures and prioritize fixes

CI failures should be categorized as:

- Product defect
- Test issue
- Test data issue
- Environment issue

---

## 8. Best Practices

- Do not use retry to hide real bugs
- Do not use hard-coded sleep unless absolutely necessary
- Prefer stable locators
- Keep tests independent
- Use proper setup and cleanup
- Add logging for critical UI and API actions
- Attach screenshots and error details to Allure reports
- Investigate tests that pass after retry

---

## Summary

The goal of flaky test management is to improve automation reliability and maintain confidence in test results.

Retry helps reduce temporary failures, but the long-term solution is to identify and fix the root cause.