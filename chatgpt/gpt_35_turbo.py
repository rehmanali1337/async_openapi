from chatgpt.enums import Endpoint, Model, Role
from .basic_model import BaseModel


class GPT35_Turbo(BaseModel):
    def __init__(self, api_key: str, temperature: float = 1.0) -> None:
        super().__init__(api_key, Model.GPT_35_TURBO, Endpoint.CHAT_COMPLETION, temperature=temperature)

    async def system_prompt(self, prompt: str) -> str:
        data = {
            "model": self.model,
            "temperature": self.temperature,
            "messages": [
                {"role": Role.SYSTEM, "content": prompt},
            ],
        }

        resp = await self._request(data)
        return resp["choices"][0]["message"]["content"]
