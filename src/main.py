from fastapi import FastAPI
from .config.app import bootstrap

app = FastAPI()

# best practice
# if __name__ == '__main__':
    # bootstrap(app)


bootstrap(app)