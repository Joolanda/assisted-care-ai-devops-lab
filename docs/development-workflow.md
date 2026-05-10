# Development Workflow

This project uses short-lived branches to keep work structured and reviewable.

## Branch Naming Convention

| Type | Meaning | Example |
|---|---|---|
| `feat` | New application feature | `feat/event-ingestion-api` |
| `ml` | ML or anomaly detection logic | `ml/bed-exit-anomaly-detector` |
| `rag` | RAG or document assistant work | `rag/care-protocol-retriever` |
| `devops` | Docker, CI/CD, monitoring, deployment | `devops/docker-ci-foundation` |
| `security` | Access control, privacy, consent | `security/rbac-access-control` |
| `pm` | Project-management documentation | `pm/risk-register-roadmap` |
| `docs` | Documentation only | `docs/readme-update` |
| `test` | Test coverage improvements | `test/anomaly-detector-tests` |
| `fix` | Bugfix | `fix/health-endpoint` |
| `refactor` | Code cleanup | `refactor/api-route-structure` |
| `exp` | Experimental prototype | `exp/tfidf-rag-prototype` |

## Commit Message Style

Examples:

- `feat: add core Pydantic domain models`
- `ml: add rule-based bed-exit anomaly detector`
- `rag: implement local care protocol retriever`
- `devops: add Dockerfile for FastAPI service`
- `security: add role-based access control rules`
- `pm: add risk register and delivery plan`
- `test: add health endpoint test`
- `docs: update README roadmap`

## Merge Strategy

For portfolio clarity:

1. Create a focused branch.
2. Keep commits small and meaningful.
3. Run tests locally.
4. Merge into `main` after the feature works.
5. Push `main`.

Optional:
Use GitHub Pull Requests to show review-style workflow.