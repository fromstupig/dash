# Prerequisites

- OS: macOS High Sierra version 10.x | Ubuntu v16.04 or later
- Runtime environment: Python version 3.7.8
- Database: PostgreSQL 10.x
  * Extensions: Postgis
- Package manager: Homebrew (macOS) | APT (Ubuntu)


# Setup project

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --trusted-host pypi.python.org
```

# Run Docker
- docker-compose -f docker-compose.local.yml up (If installed postgres local, please change port)
    
## Upgrade database
- Upgrade database (follow [here](#upgrade-database))

```
export FLASK_APP=manage:app
flask db upgrade
source seed/scripts/seeder.sh (run this script to update seed data)
```

## Add new migration

```
export FLASK_APP=manage:app
flask db migrate -m "briefly migration note"
```

# Start rest api

```
. entrypoint.sh
```

# Override environment configuration

- Create *.env* file at root folder
- Put your configure you would like to overide in your .env file with syntax **YOUR_CONFIG_KEY=YOUR_CONFIG**
- Check list available config in *config.py*

# Git branching convention

- Always create new branch from development branch
- Branch name:
  * Feature task: features/story_id-briefly_story_description
  * Development bugs: bugs/story_id-briefly_bug_description
  * Production bugs: hotfixs/story_id-briefly_bug_description

