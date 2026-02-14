# JSX — Introduction

## What JSX Is

- Syntax extension for JavaScript
    
- Used by React to describe UI
    
- Compiles to plain JavaScript (`React.createElement`)
    

## Core Idea

- UI is written as expressions
    
- Looks like HTML, but **is not HTML**
    
- JSX = syntax sugar, not a template language
    

## Key Properties

- JSX evaluates to JavaScript objects
    
- Can embed JS expressions with `{}`
    
- Must return a **single root element**
    

## Example Mental Model

- JSX describes **UI shape**
    
- React renders it based on current state
    

## Rules

- Use `className`, not `class`
    
- Use `camelCase` for props (`onClick`)
    
- Expressions only (no statements inside `{}`)
    

## Why JSX Exists

- Co-locates UI + logic
    
- Improves readability for component trees
    
- Enables static analysis and tooling
    

## Common Misconceptions

- JSX ≠ HTML
    
- Browser does not understand JSX
    
- JSX does not cause runtime overhead (compile-time transform)

---
