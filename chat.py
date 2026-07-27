import os
import sys
from typing import List, Tuple

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from prompts import SUPPORT_RESPONSE_PROMPT, FALLBACK_PROMPT
from intent_classifier import IntentClassifier
from knowledge_base import KnowledgeBase

load_dotenv()

class ConversationMemory:
    def __init__(self, max_turns: int = 5):
        self.max_turns = max_turns
        self.history: List[Tuple[str, str]] = []   

    def add(self, user_msg: str, assistant_msg: str) -> None:
        """Add a new exchange to memory."""
        self.history.append((user_msg, assistant_msg))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def format(self) -> str:
        """Format history as a string for the prompt."""
        if not self.history:
            return "No previous conversation."
        lines = []
        for user_msg, assistant_msg in self.history:
            lines.append(f"Customer: {user_msg}")
            lines.append(f"Assistant: {assistant_msg}")
        return "\n".join(lines)

    def clear(self) -> None:
        """Clear conversation history."""
        self.history.clear()


class CustomerSupportAssistant:
  def __init__(self):
        self.memory = ConversationMemory(max_turns=5)
        self.kb = KnowledgeBase()
        self.classifier = IntentClassifier()
    
        model_name = os.getenv("LLM_MODEL", "gpt-4o-mini")
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
            )
        self.llm = ChatOpenAI(
            model=model_name,
            api_key=api_key,
            temperature=0.7,
            max_tokens=300,
        )
        self.response_chain = SUPPORT_RESPONSE_PROMPT | self.llm | StrOutputParser()
        self.fallback_chain = FALLBACK_PROMPT | self.llm | StrOutputParser()

    def process_message(self, message: str) -> str:
        if not message or not message.strip():
            return "I didn't catch that. Could you please rephrase your question?"
        try:
            intent = self.classifier.classify(message)
            print(f"   [Detected Intent: {intent}]")
            context = self.kb.retrieve(intent)
            history = self.memory.format()
            response = self.response_chain.invoke({
                "history": history,
                "intent": intent,
                "context": context,
                "message": message,
            })
            self.memory.add(message, response)
            return response
        except Exception as e:
            print(f"   [Error: {e}]")
            try:
                return self.fallback_chain.invoke({"message": message})
            except Exception:
                return (
                    "I'm sorry, I'm experiencing some technical difficulties right now. "
                    "Please try again in a moment, or contact our team directly at support@example.com."
                )

    def run(self) -> None:
        """Start the interactive chat loop."""
        print("=" * 60)
        print("  🤖 AI Customer Support Assistant")
        print("=" * 60)
        print("  Type your question below. Type 'exit', 'quit', or 'bye' to end.")
        print("  Type 'clear' to reset conversation history.")
        print("=" * 60)
        print()
        while True:
            try:
                user_input = input("👤 Customer: ").strip()
                if user_input.lower() in {"exit", "quit", "bye", "goodbye"}:
                    print("\n🤖 Assistant: Thank you for contacting us! Have a great day! 👋")
                    break
                if user_input.lower() == "clear":
                    self.memory.clear()
                    print("🤖 Assistant: Conversation history cleared. How can I help you?\n")
                    continue
                if not user_input:
                    continue
                response = self.process_message(user_input)
                print(f"🤖 Assistant: {response}\n")

            except KeyboardInterrupt:
                print("\n\n🤖 Assistant: Session ended. Goodbye! 👋")
                break
            except EOFError:
                break

def main():
    """Entry point with error handling."""
    try:
        assistant = CustomerSupportAssistant()
        assistant.run()
    except ValueError as ve:
        print(f"\n⚠️  Setup Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected Error: {e}")
        sys.exit(1)
      
if __name__ == "__main__":
    main()
