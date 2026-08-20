# HTML and CSS Engineering

HTML and CSS are platform fundamentals. Frameworks sit on top of them.

## HTML mental model

HTML describes document structure and meaning.

Prefer semantic elements because they provide structure to browsers, assistive technologies, search engines, and other tooling.

Understand:

- document structure
- headings and landmark elements
- links and navigation
- forms and validation
- buttons vs links
- tables
- media
- dialogs
- metadata
- progressive enhancement

A `button` means an action. An `a` means navigation. Do not use CSS to make one behave like the other.

## Accessibility

Accessibility starts with correct HTML, not ARIA.

Core practices:

- semantic elements
- keyboard navigation
- visible focus
- labels for controls
- meaningful alt text
- accessible names
- sufficient contrast
- reduced-motion support

Use ARIA when native HTML cannot express the required semantics.

## CSS mental model

CSS is a constraint and layout system, not a collection of pixel commands.

Understand:

- cascade
- inheritance
- specificity
- box model
- containing blocks
- formatting contexts
- Flexbox
- Grid
- positioning
- stacking contexts
- responsive design
- custom properties
- media and container queries

## Layout strategy

Choose the primitive that matches the problem:

- Flexbox for one-dimensional alignment
- Grid for two-dimensional page/component layout
- normal flow whenever possible
- absolute positioning for intentional overlays, not primary layout

## Responsive design

Design from content constraints rather than device names.

Use:

- fluid sizing
- sensible max widths
- flexible grids
- container queries where component boundaries matter
- media queries for viewport-level changes

Avoid maintaining a long list of device-specific breakpoints.

## CSS architecture

Choose a predictable strategy:

- component-scoped styles
- utility classes
- CSS Modules
- design tokens via custom properties

The important requirement is consistent ownership and low specificity.

Avoid deeply nested selectors and `!important` as a dependency-resolution mechanism.

## Performance

Watch for:

- oversized images
- expensive animations
- layout thrashing
- excessive DOM depth
- unnecessary font downloads

Prefer compositor-friendly transforms and opacity for animation where appropriate.

## React connection

React changes how UI is composed, but it does not change CSS layout rules or HTML semantics. A strong frontend engineer can debug the platform without React DevTools.
