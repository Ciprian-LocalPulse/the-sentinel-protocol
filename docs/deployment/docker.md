# Deployment — Docker

*Status: Planned (`ROADMAP.md` Phase 5). This document specifies the
target containerized setup for running the API service (`docs/api/`)
beyond a single local machine.*

## Reference `Dockerfile` (target)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Iron Vault data is mounted, never baked into the image
VOLUME ["/data/sentinel"]
ENV SENTINEL_DATA_DIR=/data/sentinel
CMD ["python", "-m", "prototype.python.api.server"]
```

## Key Constraint

The Iron Vault master key is **never** baked into the image or committed
to the repository. It is injected at runtime via an environment variable
or a mounted secret file, consistent with `docs/security/encryption.md`
§Key Management.

## docker-compose (target)

```yaml
services:
  sentinel:
    build: .
    volumes:
      - sentinel_data:/data/sentinel
    environment:
      - SENTINEL_MASTER_KEY=${SENTINEL_MASTER_KEY}
      - LLM_API_KEY=${LLM_API_KEY}
volumes:
  sentinel_data:
```

## Why Docker Is Not the Default Path

Per `docs/design-principles.md` §7, the local single-process setup
(`local.md`) is the recommended starting point. Containerization is
useful once the system needs to run continuously on infrastructure the
founder doesn't want to keep their own laptop on for — it is not required
to get value from the system.
