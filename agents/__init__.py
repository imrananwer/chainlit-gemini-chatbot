class Agent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model

class Runner:
    @staticmethod
    def run_sync(starting_agent, input, run_config):
        # Dummy implementation for testing
        return type('Result', (), {
            "final_output": "This is a dummy response from the agent.",
            "to_input_list": lambda self: input
        })()

class AsyncOpenAI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

class OpenAIChatCompletionsModel:
    def __init__(self, model, openai_client):
        self.model = model
        self.client = openai_client
