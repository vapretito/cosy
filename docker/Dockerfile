FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "--login", "-c"]

# Dependencias del sistema
RUN apt-get update && apt-get install -y git curl ffmpeg sox unzip build-essential libsox-dev

# Python & Miniforge
RUN curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
    bash Miniforge3-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniforge3-Linux-x86_64.sh
ENV PATH="/opt/conda/bin:$PATH"

RUN conda create -n cosy python=3.10 -y
RUN echo "conda activate cosy" >> ~/.bashrc
ENV PATH="/opt/conda/envs/cosy/bin:$PATH"
ENV CONDA_DEFAULT_ENV=cosy

# Clonar CosyVoice
WORKDIR /workspace
RUN git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git

# Instalar requerimientos
WORKDIR /workspace/CosyVoice
RUN pip install -r requirements.txt
RUN pip install runpod

# Copiar el handler
COPY runpod_handler.py /workspace/runpod_handler.py

CMD ["python", "/workspace/runpod_handler.py"]
