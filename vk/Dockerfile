FROM python:3.10-slim
ENV BOT_NAME=$VK_BOT_NAME

WORKDIR /usr/src/app/"${VK_BOT_NAME:-vk_bot}"

COPY requirements.txt /usr/src/app/"${VK_BOT_NAME:-vk_bot}"
RUN pip install -r /usr/src/app/"${VK_BOT_NAME:-vk_bot}"/requirements.txt
COPY . /usr/src/app/"${VK_BOT_NAME:-vk_bot}"
