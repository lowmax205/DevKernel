---
name: selfhost-devops
description: Governs self-hosted deployment, container orchestration, reverse proxy configuration, Cloudflare Tunnel integration, and automated backup routines for self-hosted Linux server environments.
---

# The /selfhost-devops Skill

Use this skill whenever working on Docker Compose, Nginx configurations, environment files, Cloudflare Tunnels, or disaster recovery backup scripts.

## Multi-Container Architecture

```yaml
# docker-compose.prod.yml
version: '3.8'

networks:
  internal-net:
    internal: true # STRICTLY ISOLATED: No external route
  proxy-net:
    driver: bridge

volumes:
  postgres_data:
  uploads_data:
  backups_data:

services:
  app-postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: app_prod
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - internal-net

  app-api:
    build:
      context: .
      dockerfile: apps/api/Dockerfile
    restart: unless-stopped
    environment:
      DATABASE_URL: postgres://${DB_USER}:${DB_PASSWORD}@app-postgres:5432/app_prod
      PORT: 3000
    depends_on:
      - app-postgres
    volumes:
      - uploads_data:/app/uploads
    networks:
      - internal-net
      - proxy-net

  app-web:
    build:
      context: .
      dockerfile: apps/web/Dockerfile
    restart: unless-stopped
    environment:
      PORT: 3001
    networks:
      - proxy-net

  app-nginx:
    image: nginx:alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./infra/nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app-api
      - app-web
    networks:
      - proxy-net

  cloudflare-tunnel:
    image: cloudflare/cloudflared:latest
    restart: unless-stopped
    command: tunnel run --token ${CF_TUNNEL_TOKEN}
    depends_on:
      - app-nginx
    networks:
      - proxy-net
```

## Security Invariants

1. **PostgreSQL Network Isolation**: The database container must only belong to `internal-net`. It must never publish ports (`5432:5432` is forbidden in production).
2. **Authorized File Streaming**: The `uploads_data` volume is mounted exclusively by `app-api`. Nginx must not serve uploaded files directly from a public URL; files are verified through auth headers.
3. **Environment Segregation**: Production secrets (`.env.production`) must never be committed to git. Use `.env.example` with clear documentation.

---

## Automated Backup Strategy

Automated backup shell script located in `infra/scripts/backup.sh`:
- Runs via cron every midnight (`0 0 * * *`).
- Generates a timestamped `pg_dump` with gzip compression.
- Archives the `uploads` directory.
- Retains 7 daily and 4 weekly backups locally.
- Syncs encrypted archives to remote secondary storage (e.g., S3/R2 or off-site rsync).
