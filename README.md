# GPT-Role
Welcome to GPT-Role, a game where you and an AI will create a story together.

## Public access
- A demo of the project can be found [here](https://gpt-role.streamlit.app/).

## Development Instructions

### Prerequisites
- Ensure **Docker** is installed and running.

### Execution

> All commands must be executed from the project root directory

1. Build and start the application:
With **Docker** running, execute the program by using:
    ```bash
    docker compose down && docker compose build && docker compose up -d
    ```

2. View logs:
    ```bash
    docker compose logs streamlit -f
    ```
   
> **Note:** The commands can be executed at the same time by using: `docker compose down; docker compose build; docker compose up -d; docker compose logs streamlit -f`
 
### Access
- Open your browser and navigate to: [http://localhost:8501](http://localhost:8501)
