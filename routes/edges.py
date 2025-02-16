from fastapi import APIRouter, HTTPException, status, Query
from models.vertices import *
from setup import gremlin_client
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.traversal import T

router = APIRouter(
    prefix="/edges",
    tags=["Edges"]
)

# Create an edge
@app.post("/edges/", status_code=status.HTTP_201_CREATED)
def create_edge(source_id: str, target_id: str, label: str, properties: dict = None):
    query = (
        __.V(source_id)
        .addE(label)
        .to(__.V(target_id))
        .property(T.id, f"{source_id}-{target_id}-{label}")
    )
    if properties:
        for key, value in properties.items():
            query = query.property(key, value)
    result = gremlin_client.submit(query)
    return {
        "message": "Edge created successfully",
        "result": result
    }

# Read an edge by ID
@app.get("/edges/{edge_id}")
def read_edge(edge_id: str):
    query = __.E(edge_id).elementMap()
    result = execute_gremlin_query(query)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Edge not found"
        )
    return result[0]

# Update an edge's properties
@app.put("/edges/{edge_id}")
def update_edge(edge_id: str, properties: dict):
    query = __.E(edge_id)
    for key, value in properties.items():
        query = query.property(key, value)
    execute_gremlin_query(query)
    return {"message": "Edge updated successfully"}

# Delete an edge by ID
@app.delete("/edges/{edge_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_edge(edge_id: str):
    query = __.E(edge_id).drop()
    execute_gremlin_query(query)
    return {"message": "Edge deleted successfully"}

# List all edges
@app.get("/edges/")
def list_edges(label: str = Query(None, description="Filter edges by label")):
    query = __.E()
    if label:
        query = query.hasLabel(label)
    query = query.elementMap()
    result = execute_gremlin_query(query)
    return result