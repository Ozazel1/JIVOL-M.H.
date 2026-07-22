# Jivol - GOD LEVEL Hacker Agent

Production-ready autonomous AI agent with automated backups, health monitoring, and uncensored AI model support.

## Features

- **Telegram Integration**: Full command interface via Telegram bot
- **Uncensored AI Models**: 5 free models via OpenRouter with automatic failover
- **Agent System**: Specialized agents (Recon, Exploit, Persistence, Exfil, Accountant)
- **Automated Backups**: Configurable interval with rotation (max 10 backups by default)
- **Health Monitoring**: `/health` endpoint for uptime monitoring
- **Graceful Shutdown**: Signal handling with final backup on exit
- **Comprehensive Logging**: File + stdout logging with configurable levels
- **Thread-Safe**: All operations protected with locks
- **Production Ready**: Docker, Railway, and Gunicorn optimized

## Deployment to Railway

### Prerequisites
- Railway account (free tier available)
- GitHub account
- Telegram Bot Token
- OpenRouter API Key (for uncensored AI models)

### Setup Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Deploy Jivol GOD MODE"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/jivol.git
   git push -u origin main
   ```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your jivol repository
   - Railway will auto-detect Python project

3. **Configure Environment Variables**
   In Railway dashboard, add these variables:
   - `TELEGRAM_TOKEN` - Your Telegram bot token
   - `OPENROUTER_KEY` - Your OpenRouter API key
   - `YOUTUBE_API_KEY` - (Optional) YouTube API key
   - `BACKUP_ENABLED` - Set to `true`
   - `BACKUP_INTERVAL` - Backup interval in seconds (default: 3600)
   - `MAX_BACKUPS` - Maximum backups to keep (default: 10)
   - `LOG_LEVEL` - Logging level (INFO, DEBUG, WARNING, ERROR)
   - `PORT` - Set to `8080`

4. **Persistent Storage**
   - In Railway, add a Volume named `backups`
   - Mount path: `/app/backups`

5. **Health Check**
   - Railway will automatically use `/health` endpoint
   - Configured in railway.json

## Backup Strategy

**Automatic Backups:**
- Configurable interval (default: hourly)
- Automatic rotation (keeps MAX_BACKUPS most recent)
- Thread-safe backup operations
- Graceful shutdown triggers final backup

**Manual Backup Commands:**
- Send `backup` to Telegram bot for immediate backup
- Send `restore` to restore from latest backup

**Backup Contents:**
- `jivol_accountant_log.json` - All targets, creds, reports, URLs
- `tool_manifest.json` - Tool inventory and scores

**Backup Locations:**
- Local: `/app/backups/`
- Railway Volume: Mounted at `/app/backups` for persistence

## Cost

**Railway Free Tier:**
- $5/month credit included
- Typical usage: ~$2-4/month for this workload
- Covers compute, storage, and egress

**Alternative: Render Free Tier**
- 750 free hours/month
- Spins down after 15min inactivity
- Not recommended for 24/7 operation

## Monitoring

**Health Endpoint:**
```
GET /health
```
Returns:
```json
{
  "status": "ok",
  "uptime": 3600,
  "agents": 5,
  "model": "gryphe/mythomax-l2-13b",
  "backup_enabled": true,
  "backup_count": 3,
  "telegram_connected": true,
  "ai_enabled": true
}
```

**Logs:**
- View logs in Railway dashboard
- Structured logging with timestamps
- Configurable log levels via LOG_LEVEL
- File logging to `jivol.log`

## Telegram Commands

- `run: <cmd>` - Execute ghost command
- `spawn <target>` - Spawn full agent team
- `spawn <target> <role>` - Spawn specific agent (recon/exploit/persistence/exfil/general)
- `agents` - List active agents
- `accountant` - View intel report
- `logcreds <target> <user> <pass> [url]` - Log credentials
- `optimize <idea>` - Team optimization
- `status` - System status
- `backup` - Create backup
- `restore` - Restore latest backup
- `whoami` - Who is Jivol
- `model` - Current AI model
- `reset` - Clear memory
- `uptime` - Uptime
- `help` - Show all commands

## Security Notes

- All admin credentials logged in accountant
- Ghost mode: proxies, Tor, MAC spoofing
- Zero trace operations
- Never downloads without permission
- Absolute obedience to Sir
- Thread-safe operations
- Graceful shutdown with backup

## Model Configuration

**Free Uncensored Models (via OpenRouter):**
- gryphe/mythomax-l2-13b
- mistralai/mistral-7b-instruct:free
- huggingfaceh4/zephyr-7b-beta:free
- openchat/openchat-7b:free
- nousresearch/nous-hermes-2-mixtral-8x7b-dpo

**Fallback:**
- If all models fail, uses persona backup
- Never rejects Sir's commands

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| TELEGRAM_TOKEN | - | Telegram bot token (required) |
| OPENROUTER_KEY | - | OpenRouter API key (optional, enables AI) |
| YOUTUBE_API_KEY | - | YouTube API key (optional) |
| BACKUP_ENABLED | true | Enable/disable automated backups |
| BACKUP_INTERVAL | 3600 | Backup interval in seconds |
| MAX_BACKUPS | 10 | Maximum backups to keep |
| LOG_LEVEL | INFO | Logging level (DEBUG/INFO/WARNING/ERROR) |
| PORT | 8080 | Server port |

## Troubleshooting

**Bot not responding:**
- Check Railway logs for errors
- Verify TELEGRAM_TOKEN is set
- Check webhook is deleted (auto-deletes on start)

**AI not responding:**
- Verify OPENROUTER_KEY is set
- Check model availability in logs
- Falls back to persona if API fails

**Backups not working:**
- Ensure BACKUP_ENABLED=true
- Check Volume is mounted in Railway
- Verify backups directory exists
- Check logs for backup errors

**High memory usage:**
- Reduce MAX_BACKUPS
- Increase BACKUP_INTERVAL
- Check for orphaned threads in logs

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your keys
nano .env

# Run locally
python jivol.py
```

## Production Deployment

The refactored code includes:
- Comprehensive error handling
- Thread-safe operations
- Graceful shutdown with signal handlers
- Structured logging
- Configuration via environment variables
- Health check endpoint
- Automated backup rotation
- Production-optimized Gunicorn config
