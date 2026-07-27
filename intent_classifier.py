import os
from typing import Optional

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from prompts import INTENT_CLASSIFICATION_PROMPT


class IntentClassifier:
    VALID_INTENTS = {
        "Product Inquiry",
        "Order Status",
        "Returns & Refunds",
        "Technical Support",
        "General Query",
    }

    def __init__(self, model_name: Optional[str] = None, api_key: Optional[str] = None):
        self.model_name = model_name or os.getenv("LLM_MODEL", "gpt-4o-mini")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY in your .env file.")

        self.llm = ChatOpenAI(
            model=self.model_name,
            api_key=self.api_key,
            temperature=0.0,  
            max_tokens=20,
        )
        self.chain = INTENT_CLASSIFICATION_PROMPT | self.llm | StrOutputParser()

    def classify(self, message: str) -> str:
        if not message or not message.strip():
            return "General Query"

        try:
            raw_result = self.chain.invoke({"message": message})
            intent = raw_result.strip()
            for valid_intent in self.VALID_INTENTS:
                if valid_intent.lower() in intent.lower():
                    return valid_intent
                  return "General Query"

        except Exception as e:
            print(f"[IntentClassifier] Error during classification: {e}")
            return "General Query"
