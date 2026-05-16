def task_test():
    """Run application test"""
    return {"actions": ["uv run pytest -v"], "verbosity": 2}


def task_echo():
    """Echo your name in the terminal"""
    return {
        "params": [
            {
                "name": "name",
                "long": "name",
                "short": "n",
                "default": "mundo",
                "type": str,
            }
        ],
        "actions": ["echo %(name)s"],
        "verbosity": 2,
    }
