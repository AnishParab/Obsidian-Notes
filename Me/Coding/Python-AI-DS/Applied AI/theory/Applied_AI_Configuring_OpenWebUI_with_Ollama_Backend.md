# OpenWebUI
[Website Link](https://openwebui.com/?sort=new&t=all)

---
# Steps
##### Step 1
[Current Link](https://docs.openwebui.com/getting-started/)
- Pull and run a docker image form the above link.
##### Step 2
- Run the container but instead use this command for Linux
``` bash
docker run -d \
  -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --add-host=host.docker.internal:host-gateway \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```
- add-host is not used in the website docs.
##### Step 3
- Now you can run the UI on `localhost:3000`
- So now, `localhost:3000` and port number `11434` talk to each other.
- Note that the page will be **unreachable** for a while.
- Go to Admin Panel > Settings > Models  to pull a model.

---
# Choose a Model
[Refer this](https://ollama.com/library)

- Syntax of the models written will be `ollama run model-name`
- Hence copy-paste the `model-name` in your settings section in _step 3_.

---
