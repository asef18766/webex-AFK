FROM python:3.10-slim
RUN apt update && apt install -y adb curl && curl -sSL https://install.python-poetry.org | python3 -
RUN echo 'export PATH=$PATH:$HOME/.local/bin' >> /root/.bashrc && mkdir /app
WORKDIR /app
COPY pyproject.toml poetry.lock user_info.json /app/
RUN bash -c "source /root/.bashrc && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root"
COPY main.py /app/
ENTRYPOINT /bin/bash -c "sleep infinity"