# Customer Support Ticket Memory Agent

A customer support chatbot that remembers past customer interactions and uses that memory to provide personalized, accurate support.

## The Problem

Customer support teams waste time:
- Answering the same questions repeatedly
- Re-reading old tickets to find solutions
- Losing context between customer interactions

## The Solution

An AI agent with **Hindsight memory** that:
- **Remembers** past support tickets and solutions
- **Recalls** relevant information when a customer asks
- **Improves** over time as it learns from interactions

## How It Works

### 1. Seed: Load memories

```bash
python agent.py seed
 ```
Reads seed_tickets.json and stores all support tickets as memories.

### 2. Memories: View what the agent remembers
```bash
python agent.py memories --customer_id CUST-001
```
Shows all stored memories for a customer.

### 3. Chat: Talk with the agent
```bash
python agent.py chat --customer_id CUST-001
```
Start a chat where the agent uses memory to give personalized answers.

## Demo Commands
Run these commands in order to see the agent in action:

Step 1: Load memories
```bash
python agent.py seed
```
Expected output:
  ✓ Stored: Acme Logistics - App crashes after login...
  ✓ Stored: Acme Logistics - Export to CSV produces...
  ✓ Stored: BluePeak Health - Users intermittently...
  ✓ Stored: BluePeak Health - Audit log missing...
✅ All tickets loaded into memory
```

Step 2: View stored memories
```bash
python agent.py memories --customer_id CUST-001
```
Shows all memories for a customer.

Step 3: Chat with the agent
```bash
python agent.py chat --customer_id CUST-001
```
Then type a message like:
My app keeps crashing after login
The agent responds using its stored memories.

Key Features
✅ Memory Storage — Stores customer support tickets and interactions
✅ Memory Retrieval — Recalls relevant past issues when chatting
✅ Personalized Responses — Uses memory to give context-aware answers
✅ Learning Over Time — Stores each new interaction for future reference

Before vs After Memory Example
Customer: "My app keeps crashing after login"

Agent WITHOUT memory:

"Have you tried restarting your browser? Clearing your cache? Updating to the latest version?"

Agent WITH Hindsight memory:

"I remember you're on Windows 11 with App v2.3.1. You had this exact issue on Aug 12. We fixed it by disabling legacy SSO mode and clearing cached tokens. Let me guide you through that again..."

## Setup & Installation
### Requirements
-Python 3.x
-pip (Python package manager)
### Steps
1.Clone this repository
2.Install dependencies: pip install -r requirements.txt
3.Run: python agent.py seed (loads sample data)
4.Run: python agent.py chat --customer_id CUST-001 (start chatting)

Project Structure

ticket-memory-agent/
├── agent.py              # Main agent code
├── seed_tickets.json     # Sample support tickets
├── memory_store.json     # Local memory storage (auto-created)
├── requirements.txt      # Python dependencies
└── README.md            # This file

What This Demonstrates

This project shows how persistent agent memory transforms support from generic to personalized:

 1.Without memory: Every customer interaction starts from zero
 2.with Hindsight memory: Agent recalls past issues, solutions, and customer context
 3.Result: Faster resolution, better customer experience, happier support teams

Use Cases
-Customer Support: Remember past issues and solutions
-Sales: Recall objections and personalized talking points
-DevOps: Remember incident patterns and fixes
-Project Management: Track decisions and lessons learned

Sample Data
The agent comes with 4 realistic support tickets from 2 customers:

Customer 1: Acme Logistics (CUST-001)

.Ticket 1: App crashes after login with SSO
  .Solution: Disable legacy SSO mode + clear tokens
.Ticket 2: CSV export produces empty file
  .Solution: Increase timeout to 120s + switch to streaming mode

Customer 2: BluePeak Health (CUST-002)

.Ticket 1: Users get "Session expired" every 10 minutes
  .Solution: Fix clock skew + rotate session keys
.Ticket 2: Audit log missing entries for bulk updates
  .Solution: Enable async audit worker + increase queue retention


How to Use

Quick Start
# 1. Load all memories
python agent.py seed

# 2. See what the agent remembers
python agent.py memories --customer_id CUST-001

# 3. Chat with the agent (it uses memory)
python agent.py chat --customer_id CUST-001


Try These Messages in Chat
."My app keeps crashing after login"
."We're having issues with CSV exports"
."Can you help me with session timeout problems?"
."What do you remember about me?"
The agent will reference past tickets and solutions from memory.

Tech Stack
.Python — Agent logic
.Local JSON storage — Memory (can be replaced with Hindsight Cloud API)
.Requests library — HTTP requests (for future cloud integration)

Files Explained
File	                      Purpose

agent.py	           Main agent code with seed, chat, memories commands
seed_tickets.json	   Sample customer support tickets
requirements.txt	   Python package dependencies
memory_store.json  	   Local JSON file storing memories (created after seed)
README.md	           This documentation

Future Improvements
.Connect to real Hindsight Cloud API for persistent memory
.Add LLM integration (Groq/OpenAI) for smarter responses
.Web UI for customer interactions
.Multi-language support
.Analytics dashboard to track agent performance
.Vector search for semantic memory retrieval

Key Insight
Memory makes all the difference.

The same agent, same question, but vastly better because it remembers. This is the power of Hindsight agent memory.

Demo Video
Watch the full demo: [Add your YouTube link here after recording]

Team
[Add your team members' names here]

Project Built For
Microsoft Hindsight Hackathon - October 3, 2026

### Quick Commands Reference
```bash
# Load sample data into memory
python agent.py seed

# View all memories for a customer
python agent.py memories --customer_id CUST-001
python agent.py memories --customer_id CUST-002

# Chat with the agent (it uses memory to respond)
python agent.py chat --customer_id CUST-001

# Exit chat
exit
```

The agent that remembers. The support that matters.

## Team Articles
Read our detailed write-ups about building this project:

[How Agent Memory Transformed Our Customer Support]
Article_Link_1 = https://medium.com/@geethapriyankaankala25/how-agent-memory-transformed-our-customer-support-182c11c4b275

[Why Realistic Data Matters for AI Agents]
Article_Link_2 = https://medium.com/@sathwikch2006/why-realistic-data-matters-for-ai-agents-our-approach-d0244d737850

[Before and After: How Memory Transforms Support]
Article_Link_3 = https://medium.com/@aravinddyaga786/before-and-after-how-memory-transforms-the-support-experience-50b5ad3f2e51

[Building an AI Agent with Persistent Memory]
Article_Link_4 = https://medium.com/@g.shivasai9390/building-an-ai-agent-with-persistent-memory-technical-deep-dive-1aa6307851fc

[Why Your Support Team Needs Agent Memory]
Article_Link_5 = https://medium.com/@tirumalashivakumar.geck/why-your-support-team-needs-agent-memory-the-business-case-65613dd14e4a

