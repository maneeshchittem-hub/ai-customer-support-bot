import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import ToolMessage
from tools import track_order
from rag import search_company_policy

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)


tools = [
    track_order,
    search_company_policy
]


model_with_tools = model.bind_tools(tools)


SYSTEM_PROMPT = """
You are a helpful AI customer support assistant.

Your job is to help customers with company policies
and order tracking.

RULES:

1. If the customer asks about an order status, shipping,
delivery, tracking, or ETA, use the track_order tool.

2. If the customer asks about returns, refunds, cancellation,
shipping policy, delivery policy, or privacy policy,
use the search_company_policy tool.

3. Never invent order information.

4. If an order ID is needed, ask the customer for it.

5. If an order does not exist, clearly tell the customer.

6. Give simple and friendly answers.

7. Never ask for passwords, credit card numbers,
bank account information, or other sensitive information.
"""


def chat_with_agent(user_question):

    messages = [
        (
            "system",
            SYSTEM_PROMPT
        ),
        (
            "human",
            user_question
        )
    ]

    response = model_with_tools.invoke(messages)

    while response.tool_calls:

        messages.append(response)

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            if tool_name == "track_order":

                tool_result = track_order.invoke(
                    tool_args
                )

            elif tool_name == "search_company_policy":

                tool_result = search_company_policy.invoke(
                    tool_args
                )

            else:

                tool_result = "Unknown tool."

            messages.append(
    ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"]
    )
)

        response = model_with_tools.invoke(messages)

    return response.content[0]["text"]