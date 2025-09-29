from memory import memory
from nlu import parse_intent_entities

def get_request(state):
    current_query = memory.get("current_turn_query", "")
    intent, entities = parse_intent_entities(current_query)
    memory["current_intent"] = intent
    memory["current_entities"] = entities
    print(f"[UserRequest] Query: '{current_query}' | Intent: {intent} | Entities: {entities}")
    return {"request": current_query}
