from typing import Annotated

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from prompts import generate, reflect


class State(TypedDict):
    messages: Annotated[list, add_messages]


def generation_node(state: State) -> State:
    return {"messages": [generate.invoke(state["messages"])]}


def reflection_node(state: State) -> State:
    # Other messages we need to adjust
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    # First message is the original user request. We hold it the same for all nodes
    translated = [state["messages"][0]] + [
        cls_map[msg.type](content=msg.content) for msg in state["messages"][1:]
    ]
    res = reflect.invoke(translated)
    # We treat the output of this as human feedback for the generator
    return {"messages": [HumanMessage(content=res)]}


def should_continue(state: State):
    class Consts:
        MAX_ITERATIONS = 6

    if len(state["messages"]) > Consts.MAX_ITERATIONS:
        return END
    return "reflect"


def graph_builder():
    builder = StateGraph(State)
    builder.add_node("generate", generation_node)
    builder.add_node("reflect", reflection_node)
    builder.add_edge(START, "generate")
    builder.add_conditional_edges("generate", should_continue)
    builder.add_edge("reflect", "generate")
    memory = MemorySaver()
    return builder.compile(checkpointer=memory)


if __name__ == "__main__":
    final_state = graph_builder().invoke(
        {
            "messages": [
                HumanMessage(
                    content="Generate an essay on great stock market failures and successes"
                )
            ],
        },
    )
    print(final_state["messages"][-1].content)
