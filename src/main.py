from fastapi import FastAPI
from .config.app import bootstrap

app: FastAPI | None = None

# best practice
# if __name__ == '__main__':
#     app = bootstrap()

app = bootstrap()