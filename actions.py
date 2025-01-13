from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideAIInfo(Action):
    def name(self) -> Text:
        return "action_provide_ai_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = (
            "Artificial Intelligence (AI) is the simulation of human intelligence in machines. "
            "It involves learning, reasoning, and self-correction. Examples include chatbots, "
            "image recognition, and natural language processing."
        )
        dispatcher.utter_message(text=response)
        return []

class ActionProvideMLInfo(Action):
    def name(self) -> Text:
        return "action_provide_ml_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = (
            "Machine Learning (ML) is a subset of AI that allows systems to learn from data "
            "and improve over time without being explicitly programmed. Types include supervised, "
            "unsupervised, and reinforcement learning."
        )
        dispatcher.utter_message(text=response)
        return []

class ActionProvideAlgorithmInfo(Action):
    def name(self) -> Text:
        return "action_provide_algorithm_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = (
            "AI/ML algorithms include Decision Trees, Neural Networks, Support Vector Machines (SVMs), "
            "K-Nearest Neighbors (KNN), and Ensemble Methods like Random Forest and Gradient Boosting."
        )
        dispatcher.utter_message(text=response)
        return []

class ActionProvideUseCases(Action):
    def name(self) -> Text:
        return "action_provide_use_cases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = (
            "AI/ML use cases include personalized recommendations in e-commerce, fraud detection in finance, "
            "predictive maintenance in manufacturing, and disease diagnosis in healthcare."
        )
        dispatcher.utter_message(text=response)
        return []

class ActionProvideAdvancedTopics(Action):
    def name(self) -> Text:
        return "action_provide_advanced_topics"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = (
            "Advanced topics include Transfer Learning, Generative Adversarial Networks (GANs), "
            "Reinforcement Learning, and the Transformer architecture used in NLP."
        )
        dispatcher.utter_message(text=response)
        return []
