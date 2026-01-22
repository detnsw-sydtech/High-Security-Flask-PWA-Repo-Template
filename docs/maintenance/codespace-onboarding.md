# Getting Started in Your Codespace

This project is designed to **set itself up for you**.  
Most of the time, you just open the Codespace and start coding.

## What happens automatically

When your Codespace is created:

1. **uv is installed**  
2. **A virtual environment (`.venv`) is created**  
3. **All dependencies are installed**  
4. **Basic checks run** to make sure Python and uv are correct  

When your Codespace starts:

1. **Old VM cache is cleaned** (to keep things fast and stable)  
2. **Diagnostics run** (so staff can help if something breaks)  
3. **The Flask app starts** on port `5000`  

You’ll usually see a prompt telling you the app is running and a link to open it in the browser.

---

## Common commands you might use

**From the terminal in the Codespace:**

- **Check environment health**
```bash
bash .devcontainer/scripts/diagnostics.sh
```
- **Rebuild the virtual environment (if something feels “off”)**
```bash
bash .devcontainer/scripts/rebuild-venv.sh
```

- **Run the app again (if you stopped it)**
```bash
bash .devcontainer/startup.sh
```


