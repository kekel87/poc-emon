# POCemon

> aka POC (Proof Of Concept) + Pokemon 🤩

The goal of this monorepo is to centralize my POC back, front and why not fullstack,
made during my various professional experiences.

All backs will serve the same API and use the same DB structure.

All fronts must have the same interface and consume the same API (whatever the back).

## Project organization

```
📦poc-emon
 ┣ 📂shared
 ┃ ┣ 📂data
 ┃ ┣ 📂style
 ┃ ┗ 📂...
 ┣ 📂fronts
 ┃ ┣ 📂angular
 ┃ ┣ 📂vanilla-js
 ┃ ┗ 📂...
 ┣ 📂backs
 ┃ ┣ 📂fastapi
 ┃ ┣ 📂plumber
 ┃ ┣ 📂nestjs
 ┃ ┗ 📂...
 ┗ 📂 fullstack
   ┗ 📂...
```

## Back

All backs must achieve these objectives:
- OpenAPI compliante
- must serve an OpenAPI (swagger-ui)
- SQLite compatible
- BDD migration tool
- code linter and formater
- unit tests
- integration tests

## Front

All front must achieve these objectives:
- classic list search view edition app
- same UI
- consume OpenAPI
- code linter and formater
- unit tests
- integration tests

## FullStack

> No plan for that at the moment...

## API

> API description here

## BDD

> BDD structure here

## UI

> UI here