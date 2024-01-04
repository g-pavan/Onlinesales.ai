import asyncio
import aiohttp
import json
import time

async def evaluate_expressions(expressions, session):
    """
    Evaluate mathematical expressions using a web API.

    Args:
        expressions (list): List of mathematical expressions to evaluate.
        session (aiohttp.ClientSession): An aiohttp client session.

    Returns:
        list: List of evaluated results for the expressions.
    """
    api_url = "http://api.mathjs.org/v4/"
    payload = {
        "expr": expressions,
        "precision": 14
    }
    
    async with session.post(api_url, json=payload) as response:
        if response.status == 200:
            results = await response.json()
            return results['result']
        else:
            return None    

async def main():
    """
    Main entry point for the application.

    Reads mathematical expressions from a file, evaluates them using a web API, and displays the results.
    """
    expressions = []
    with open("expressions.txt", "r") as file:
        for line in file:
            expression = line.strip()
            if expression.lower() == "end":
                break
            expressions.append(expression)

    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        results = await evaluate_expressions(expressions, session)
        if results is not None:
            for i, expression in enumerate(expressions):
                result = results[i]
                print(f"{expression} => {result}")
        else:
            print("Failed to retrieve results from the API.")
    
    end_time = time.time()
    total_execution_time = end_time - start_time
    print(f"Time to evaluate {len(results)} requests in: {total_execution_time:.2f} seconds")
if __name__ == "__main__":
    asyncio.run(main())
