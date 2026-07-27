from typing import List, Dict, Optional

class KnowledgeBase:
    def __init__(self):
        self._documents: Dict[str, List[str]] = {
            "Product Inquiry": [
                "Our product catalog includes electronics, home appliances, and accessories. "
                "All products come with a 1-year manufacturer warranty.",
                "You can check product specifications, availability, and pricing on our website. "
                "Contact sales for bulk orders or custom requirements.",
                "New arrivals are updated every Monday. Subscribe to our newsletter for early access.",
            ],
            "Order Status": [
                "You can track your order in real-time using the tracking number sent to your email. "
                "Orders typically ship within 1-2 business days.",
                "Standard delivery takes 3-5 business days. Express shipping is available for urgent orders.",
                "If your order is delayed beyond the estimated date, please contact us with your order ID.",
            ],
            "Returns & Refunds": [
                "We offer a 30-day return policy for unused items in original packaging. "
                "Refunds are processed within 5-7 business days after we receive the return.",
                "To initiate a return, go to 'My Orders' and select 'Return Item'. Print the prepaid label provided.",
                "Defective or damaged items can be returned for a full refund or replacement at no extra cost.",
            ],
            "Technical Support": [
                "For common issues, try restarting the device and checking for software updates first.",
                "Our support team is available 24/7 via live chat and email for technical troubleshooting.",
                "Visit our Help Center for step-by-step guides, FAQs, and video tutorials.",
                "If the issue persists, our technicians can schedule a remote diagnostic session.",
            ],
            "General Query": [
                "Our business hours are Monday to Friday, 9 AM to 6 PM (EST). "
                "Live chat support is available during these hours.",
                "You can reach us via email at support@example.com or call our toll-free number.",
                "We value your feedback! Share your experience to help us improve our services.",
            ],
        }

    def retrieve(self, intent: str, top_k: int = 2) -> str:
        docs = self._documents.get(intent, self._documents["General Query"])
        selected = docs[:top_k]
        return "\n\n".join(selected)

    def add_document(self, intent: str, content: str) -> None:
        if intent not in self._documents:
            self._documents[intent] = []
        self._documents[intent].append(content)

    def list_intents(self) -> List[str]:
        """Return all available intent categories."""
        return list(self._documents.keys())
