"""
Costco Shopping Agent Demo - Browser Agent with LangGraph

This demo shows the LangGraph-based browser agent shopping at Costco.com.
Update the Azure OpenAI credentials below before running.

Task: Find and report the price of a specific product at Costco.
"""
import asyncio
import logging
from openai import AsyncAzureOpenAI

from agent import LangGraphBrowserAgent

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)


async def main():
    """Run Costco shopping demo with Azure OpenAI"""
    
    # ============================================================
    # CONFIGURATION - Update these with your credentials
    # ============================================================
    
    azure_endpoint = "https://your-endpoint.openai.azure.com/"  # UPDATE THIS
    api_key = "your-api-key-here"  # UPDATE THIS
    api_version = "2024-12-01-preview"
    deployment_name = "gpt-4o-mini"  # Or your deployment name
    
    # ============================================================
    # TASK - Grocery shopping with delivery
    # ============================================================
    
    task = """Complete a Costco grocery shopping order with the following items:

SHOPPING LIST:
1. Paper towels
2. Milk
3. Toilet paper
4. Dish wash (dishwashing detergent)

DELIVERY INFO:
- Address: 830 Birch Ave, Sunnyvale, CA 94086
- Recipient: Si Chang

STEPS TO COMPLETE:
1. For each item in the shopping list:
   - Find the search box and type the item name
   - Press Enter or click the search button to search
   - Find and click on the first product in the results
   - Click "Add to Cart" button to add it to cart
   - Navigate back to search for the next item (use browser back or go to homepage)

2. After adding all 4 items:
   - Go to cart (click cart icon or navigate to cart page)
   - Verify all 4 items are in the cart
   - Proceed to checkout if possible
   - Enter delivery address: 830 Birch Ave, Sunnyvale, CA 94086
   - Enter recipient name: Si Chang
   - Complete as much of checkout as possible (may require sign-in)

Be persistent and complete the shopping order!"""
    
    # ============================================================
    # AGENT SETUP
    # ============================================================
    
    # Initialize Azure OpenAI client
    client = AsyncAzureOpenAI(
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint
    )
    
    print("\n" + "="*70)
    print("COSTCO SHOPPING AGENT DEMO (LangGraph)")
    print("="*70)
    print(f"\nTask: {task}")
    print(f"\nUsing: LangGraph + Azure OpenAI ({deployment_name})")
    print("="*70 + "\n")
    
    # Create the LangGraph agent
    agent = LangGraphBrowserAgent(
        task=task,
        llm_client=client,
        model=deployment_name,
        headless=False,  # Set to True to hide browser window
        max_steps=50,    # Increased for complex shopping task with 4 items + checkout
        api_version=api_version,
        azure_endpoint=azure_endpoint,
        api_key=api_key
    )
    
    # ============================================================
    # RUN THE AGENT
    # ============================================================
    
    try:
        result = await agent.run()
        
        print("\n" + "="*70)
        print("SHOPPING COMPLETE!")
        print("="*70)
        print(f"\n{result}\n")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    # Run the Costco grocery shopping demo
    asyncio.run(main())


