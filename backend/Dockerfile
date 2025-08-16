FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENV PIP_ONLY_BINARY=:all: PIP_DISABLE_PIP_VERSION_CHECK=1

# OpenMP runtime for numba (SHAP)
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# heavy deps in cached layers
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --prefer-binary numpy==1.26.4
RUN pip install --no-cache-dir --prefer-binary torch==2.3.1 -f https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir --prefer-binary shap==0.45.1 matplotlib==3.8.4
RUN pip install --no-cache-dir --prefer-binary \
    fastapi==0.104.1 uvicorn[standard]==0.24.0 \
    transformers==4.35.2 huggingface_hub==0.23.5 hf_transfer==0.1.6 \
    python-multipart==0.0.6

# app code last
COPY . .

# Spaces provides $PORT; bind 0.0.0.0 (default 7860)
CMD ["sh","-c","uvicorn app:app --host 0.0.0.0 --port ${PORT:-7860}"]
