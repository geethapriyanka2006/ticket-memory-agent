import os
import json
import sys

# Simulated memory storage (local file)
MEMORY_FILE = "memory_store.json"

def init_memory_store():
    """Initialize memory storage"""
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({}, f)

def seed_memories():
    """Load tickets into simulated memory"""
    print("📥 Seeding memories from seed_tickets.json...")
    
    init_memory_store()
    
    with open("seed_tickets.json", "r") as f:
        tickets = json.load(f)
    
    memory_store = {}
    
    for ticket in tickets:
        customer_id = ticket["customer_id"]
        customer_name = ticket["customer_name"]
        environment = ticket["environment"]
        issue = ticket["issue"]
        resolution = ticket["resolution"]
        
        memory_text = f"Customer: {customer_name} | Environment: {environment} | Issue: {issue} | Resolution: {resolution}"
        
        if customer_id not in memory_store:
            memory_store[customer_id] = []
        
        memory_store[customer_id].append(memory_text)
        print(f"  ✓ Stored: {customer_name} - {issue[:50]}...")
    
    # Save to local file
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_store, f, indent=2)
    
    print("✅ All tickets loaded into memory\n")

def get_memories(customer_id):
    """Retrieve memories for a customer"""
    init_memory_store()
    
    with open(MEMORY_FILE, "r") as f:
        memory_store = json.load(f)
    
    return memory_store.get(customer_id, [])

def store_interaction_memory(customer_id, user_message, response_text):
    """Store interaction as memory"""
    init_memory_store()
    
    with open(MEMORY_FILE, "r") as f:
        memory_store = json.load(f)
    
    if customer_id not in memory_store:
        memory_store[customer_id] = []
    
    memory_text = f"User asked: {user_message[:100]} | Agent responded: {response_text[:100]}"
    memory_store[customer_id].append(memory_text)
    
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_store, f, indent=2)

def show_memories(customer_id):
    """Display all memories for a customer"""
    print(f"\n📚 Memories for customer {customer_id}:\n")
    
    memories = get_memories(customer_id)
    
    if not memories:
        print("  (No memories found)")
    else:
        for i, memory in enumerate(memories, 1):
            print(f"  Memory {i}: {memory}\n")

def simple_response(customer_id, user_message, memories):
    """Generate response based on memories"""
    if memories:
        memory_summary = "\n".join(memories[:2])
        return f"I found relevant information about you:\n\n{memory_summary}\n\nBased on your history, regarding '{user_message}': I recommend the solutions that worked before."
    else:
        return f"You asked: '{user_message}'. I can help, but I don't have previous history for you yet."

def chat(customer_id):
    """Chat with the agent using memory"""
    print(f"\n💬 Chat started with customer {customer_id}")
    print("(Type 'exit' to quit)\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Get memories
        memories = get_memories(customer_id)
        
        # Generate response
        agent_response = simple_response(customer_id, user_input, memories)
        
        print(f"\nAgent: {agent_response}\n")
        
        # Store this interaction
        store_interaction_memory(customer_id, user_input, agent_response)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python agent.py seed                          # Load ticket data into memory")
        print("  python agent.py chat --customer_id CUST-001   # Chat with a customer")
        print("  python agent.py memories --customer_id CUST-001 # View stored memories")
        return
    
    command = sys.argv[1]
    
    if command == "seed":
        seed_memories()
    
    elif command == "chat":
        if len(sys.argv) < 4 or sys.argv[2] != "--customer_id":
            print("Usage: python agent.py chat --customer_id CUST-001")
            return
        customer_id = sys.argv[3]
        chat(customer_id)
    
    elif command == "memories":
        if len(sys.argv) < 4 or sys.argv[2] != "--customer_id":
            print("Usage: python agent.py memories --customer_id CUST-001")
            return
        customer_id = sys.argv[3]
        show_memories(customer_id)
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()