# Tailwind CSS

**Role:** Primary | **Layer:** Frontend

## Mental model
Tailwind provides utility classes that encode styling decisions close to markup while a build step generates the required CSS.

## Learn
- utility composition
- responsive and state variants
- design tokens and theme configuration
- arbitrary values and custom utilities
- component extraction
- dark mode and accessibility
- content scanning and production builds

## Production patterns
Create a small design vocabulary, centralize tokens, avoid uncontrolled arbitrary values, and use component abstractions where repetition becomes meaningful. Keep accessibility independent of visual styling.

## Pitfalls
Utility-heavy markup can become unreadable when component boundaries are poor. Do not treat Tailwind as a substitute for design-system architecture.
