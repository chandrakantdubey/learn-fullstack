# Frontend Testing and Accessibility

Production frontend quality is broader than component tests. Test behavior at the right boundary and treat accessibility as part of correctness.

## Testing layers

```text
Unit
 ↓
Component
 ↓
Integration
 ↓
End-to-end
```

### Unit

Use for deterministic logic:

- parsing
- formatting
- validation rules
- pure domain functions

### Component

Verify observable component behavior:

- rendered content
- interaction
- validation
- loading/error/empty states

Avoid testing implementation details such as private state variables or exact internal hook calls.

### Integration

Verify boundaries between frontend modules and API behavior with controlled network responses.

### End-to-end

Use Playwright or an equivalent browser runner for critical user journeys:

- login
- checkout
- create/edit/delete workflows
- permission boundaries
- important navigation paths

## Network mocking

Mock at the network boundary rather than mocking every internal function. This preserves realistic application behavior while keeping tests deterministic.

## Accessibility

A production component should be usable with:

- keyboard only
- screen reader semantics
- visible focus indicators
- reduced motion settings
- sufficient contrast

Use semantic HTML first. Use automated tools such as axe as a safety net, not as the entire accessibility strategy.

## Test pyramid rule

Keep most tests close to business behavior and reserve E2E for the small set of flows where full-stack confidence matters.

## CI expectations

Every production frontend should have automated:

- type checking
- linting
- unit/component tests
- critical E2E tests
- accessibility checks where practical
- build verification
