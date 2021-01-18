from starlette.requests import Request

from server.core.services.dataflow_graph import DataFlowGraph


def get_dataflow_graph(request: Request) -> DataFlowGraph:
    return request.app.state.dataflow_graph
