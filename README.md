# Portal chat backend

## Add dependency 

```shell
pip install fastapi
```

Or Poetry, to use poetry with vscode:

```shell
pip install poetry
poetry config virtualenvs.in-project true
poetry add openai
```

## Run app

To run app without docker

```shell
poetry install
uvicorn app.main:app --host 0.0.0.0 --port 8018 --reload
```

With docker (recommended)

```shell
docker compose up
```

To run in detached mode:

```shell
docker compose up -d
```

## Build image

```shell
docker compose up --build
```

The image will only be built once. When changing a dependency, use --build to force the rebuilding of the image when starting a container

Docker Hub: https://hub.docker.com/repository/docker/locnguyenivy/langchain-server/tags?page=1&ordering=last_updated

## Environment variable

Add environment variable in `.env` file.

## Using under ivy engine network

Run this command to create docker network

```shell
docker network create <network-name>
```

## Langchain section

### Installation

Install the LangChain CLI if you haven't yet

```bash
pip install -U langchain-cli
```

### Adding packages

```bash
# adding packages from 
# https://github.com/langchain-ai/langchain/tree/master/templates
langchain app add $PROJECT_NAME

# adding custom GitHub repo packages
langchain app add --repo $OWNER/$REPO
# or with whole git string (supports other git providers):
# langchain app add git+https://github.com/hwchase17/chain-of-verification

# with a custom api mount point (defaults to `/{package_name}`)
langchain app add $PROJECT_NAME --api_path=/my/custom/path/rag
```

Note: you remove packages by their API path

```bash
langchain app remove my/custom/path/rag
```

### Setup LangSmith (Optional)
LangSmith will help us trace, monitor and debug LangChain applications. 
LangSmith is currently in private beta, you can sign up [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

### Launch LangServe

```bash
langchain serve
```