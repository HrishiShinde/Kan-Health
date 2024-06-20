from model import HealthAI

# Testing...
print("Starting Test...")
test_queries = [
    "Hi, who are you?",
    "I have diabetes. What should I do?",
    # "I have high blood pressure. What are the best practices?",
    # "I am experiencing chest pain. What could be the reasons?",
]

ai = HealthAI()

print("Loading queries...")
for query in test_queries:
    print(f"Query: {query}")
    print(f"Health Plan: {ai.generate_health_plan(query)}\n")
    print(f"Health Plan2: {ai.generate_health_plan2(query)}\n")
