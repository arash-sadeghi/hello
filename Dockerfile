FROM continuumio/miniconda3:24.5.0-0
WORKDIR /app
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml
ENV PATH=/opt/conda/envs/fastapi-hello/bin:$PATH
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


