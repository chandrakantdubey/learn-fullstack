# React Hook Form

**Role:** Primary | **Layer:** Frontend

## Mental model
React Hook Form manages form state and field registration with minimal React re-rendering. Validation is a separate concern and can use the canonical Zod schema.

## Learn
- registration and controlled components
- validation/resolvers
- field arrays
- touched, dirty and submit state
- async submission and server errors
- accessibility and error summaries

## Production
Keep form schemas close to the boundary they validate, distinguish client feedback from authoritative server validation, disable duplicate submissions, and preserve accessible labels/errors.

## Related
React, Zod, shadcn/ui, API contracts.
