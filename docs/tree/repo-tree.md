```tree
[drwxr-xr-x 4.0K]  .
├── [drwxr-xr-x 4.0K]  .devcontainer
│   ├── [-rw-r--r-- 5.4K]  README.md
│   ├── [-rw-r--r--  990]  devconSLOW.txt
│   ├── [-rw-r--r-- 1001]  devcontainer.json
│   ├── [-rw-r--r-- 2.5K]  devcontainer.json.backup
│   ├── [-rwxr-xr-x 2.5K]  preflight.sh
│   ├── [drwxr-xr-x 4.0K]  scripts
│   │   ├── [-rw-r--r-- 1.6K]  diagnostics.sh
│   │   ├── [-rw-r--r--  780]  install-uv.sh
│   │   ├── [-rwxr-xr-x 3.9K]  purge-vm.sh
│   │   └── [-rw-r--r-- 1.1K]  rebuild-venv.sh
│   └── [-rwxr-xr-x 2.1K]  startup.sh
├── [-rw-r--r--  455]  .env
├── [-rw-r--r-- 4.7K]  .gitignore
├── [-rw-r--r--  934]  .gitleaks.toml
├── [-rw-r--r--  749]  .pre-commit-config.yaml
├── [-rw-r--r--  376]  .ruff.toml
├── [-rw-r--r--   23]  .semgrepignore
├── [-rw-r--r--    8]  .uvignore
├── [-rw-r--r-- 1.1K]  LICENSE
├── [-rw-r--r-- 3.1K]  README.md
├── [-rw-r--r--  156]  bandit.yaml
├── [drwxr-xr-x 4.0K]  docs
│   ├── [drwxr-xr-x 4.0K]  _includes
│   │   ├── [-rw-r--r--  177]  footer.md
│   │   └── [-rw-r--r-- 1.3K]  header.md
│   ├── [drwxr-xr-x 4.0K]  _static
│   │   └── [-rw-r--r-- 1.1K]  theme.css
│   ├── [drwxr-xr-x 4.0K]  architecture
│   │   ├── [-rw-r--r-- 3.7K]  app-factory-overview.md
│   │   ├── [-rw-r--r-- 1.8K]  blueprints-overview.md
│   │   ├── [-rw-r--r-- 2.8K]  database-model-overview.md
│   │   ├── [-rw-r--r-- 4.2K]  erd-and-python-logic.md
│   │   ├── [-rw-r--r-- 4.1K]  erd-drawing-exercise.md
│   │   ├── [-rw-r--r-- 1.6K]  erd-master.md
│   │   ├── [-rw-r--r-- 1.4K]  erd-printable-png.md
│   │   ├── [-rw-r--r-- 4.9K]  erd-vs-models-side-by-side.md
│   │   ├── [-rw-r--r-- 2.1K]  how-to-read-mermaid-erds.md
│   │   ├── [-rw-r--r--  911]  master-erd.md
│   │   ├── [-rw-r--r-- 4.6K]  reference-architecture.md
│   │   ├── [-rw-r--r-- 1.4K]  relational-erd.md
│   │   ├── [-rw-r--r-- 3.4K]  relational-relationships-overview.md
│   │   ├── [-rw-r--r-- 1.9K]  search-system-overview.md
│   │   └── [-rw-r--r-- 1.6K]  security-overview.md
│   ├── [drwxr-xr-x 4.0K]  assets
│   │   └── [-rw-r--r--    1]  placeholder.txt
│   ├── [-rw-r--r-- 1.3K]  index.md
│   ├── [drwxr-xr-x 4.0K]  maintenance
│   │   ├── [-rw-r--r-- 2.7K]  codespace-onboarding.md
│   │   └── [-rw-r--r-- 1.6K]  codespace-terminal.md
│   ├── [drwxr-xr-x 4.0K]  project
│   │   └── [-rw-r--r-- 6.7K]  db_modelling.md
│   ├── [drwxr-xr-x 4.0K]  security
│   │   └── [-rw-r--r-- 2.1K]  dast-owasp-zap-baseline.md
│   └── [drwxr-xr-x 4.0K]  stylesheets
│       └── [-rw-r--r-- 1.8K]  header.css
├── [drwxr-xr-x 4.0K]  legacy
│   ├── [-rw-r--r-- 2.8K]  bootstrap.yml
│   ├── [-rw-r--r--  838]  cleanup-bootstrap.yml
│   └── [-rw-r--r--  540]  temp-generate-lockfile.yml
├── [-rw-r--r-- 1.7K]  mkdocs.yml
├── [-rw-r--r--  350]  mypy.ini
├── [-rw-r--r--   62]  osv-scanner.toml
├── [-rw-r--r--  64K]  package-lock.json
├── [-rw-r--r--  596]  package.json
├── [-rw-r--r-- 4.1K]  pyproject.toml
├── [-rw-r--r--  108]  pytest.ini
├── [-rw-r--r--    0]  repo-tree.txt
├── [drwxr-xr-x 4.0K]  scripts
│   ├── [-rw-r--r-- 1.6K]  README.md
│   ├── [-rwxr-xr-x  858]  dev-start.sh
│   ├── [-rw-r--r-- 2.7K]  health_check.py
│   ├── [-rwxr-xr-x 1.1K]  reset_caches.sh
│   └── [-rw-r--r--  643]  zap_baseline.py
├── [drwxr-xr-x 4.0K]  src
│   └── [drwxr-xr-x 4.0K]  app
│       ├── [-rw-r--r-- 3.5K]  __init__.py
│       ├── [drwxr-xr-x 4.0K]  api
│       │   ├── [-rw-r--r--  376]  __init__.py
│       │   └── [-rw-r--r-- 5.5K]  routes.py
│       ├── [drwxr-xr-x 4.0K]  auth
│       │   ├── [-rw-r--r--  409]  __init__.py
│       │   └── [-rw-r--r-- 2.6K]  routes.py
│       ├── [drwxr-xr-x 4.0K]  db
│       │   ├── [-rw-r--r--  181]  __init__.py
│       │   └── [-rw-r--r-- 3.2K]  models.py
│       ├── [-rw-r--r-- 2.2K]  extensions.py
│       ├── [drwxr-xr-x 4.0K]  main
│       │   ├── [-rw-r--r--  402]  __init__.py
│       │   ├── [-rw-r--r--    1]  data.py
│       │   ├── [-rw-r--r-- 1.7K]  data_generator.py
│       │   └── [-rw-r--r-- 4.3K]  routes.py
│       ├── [drwxr-xr-x 4.0K]  pwa
│       │   ├── [-rw-r--r--  407]  __init__.py
│       │   └── [-rw-r--r-- 2.3K]  routes.py
│       ├── [drwxr-xr-x 4.0K]  security
│       │   ├── [-rw-r--r--  422]  __init__.py
│       │   └── [-rw-r--r-- 2.0K]  routes.py
│       ├── [drwxr-xr-x 4.0K]  static
│       │   ├── [drwxr-xr-x 4.0K]  css
│       │   │   ├── [-rw-r--r-- 3.0K]  main.css
│       │   │   └── [-rw-r--r--  13K]  tailwind.css
│       │   ├── [drwxr-xr-x 4.0K]  js
│       │   │   ├── [-rw-r--r-- 1.5K]  app.js
│       │   │   ├── [-rw-r--r--   81]  postcss.config.js
│       │   │   ├── [-rw-r--r--  122]  service-worker.js
│       │   │   ├── [-rw-r--r--  366]  sw-register.js
│       │   │   └── [-rw-r--r--  730]  tailwind.config.js
│       │   ├── [-rw-r--r--  105]  manifest.json
│       │   ├── [-rw-r--r--  409]  manifest.webmanifest
│       │   └── [drwxr-xr-x 4.0K]  src
│       │       └── [-rw-r--r--  170]  input.css
│       └── [drwxr-xr-x 4.0K]  templates
│           ├── [-rw-r--r-- 1.7K]  base.html
│           ├── [-rw-r--r-- 2.4K]  catalogue.html
│           ├── [-rw-r--r--  626]  index.html
│           └── [drwxr-xr-x 4.0K]  partials
│               └── [-rw-r--r-- 1.8K]  item_list.html
├── [-rw-r--r--  287]  tailwind.config.js
├── [drwxr-xr-x 4.0K]  tests
│   ├── [-rw-r--r--    1]  __init__.py
│   ├── [-rw-r--r--  106]  test_app.py
│   └── [-rw-r--r--  597]  test_db_initialisation.py
└── [-rw-r--r-- 140K]  uv.lock
```
29 directories, 96 files
