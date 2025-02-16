from fastapi import APIRouter, HTTPException
from models.vertices import *
from setup import gremlin_client

router = APIRouter(
    prefix="/vertex",
    tags=["Vertices"]
)

@router.post("/player")
def create_player(player: Player):
    """
    Create a player in the graph
    """
    try:
        query = f"g.addV('{player.label.value}')"
        for key, value in player.model_dump().items():
            if key != "label":
                query += f".property('{key}', '{value}')"
        result = gremlin_client.submit(query).all().result()
        return {"message": "Player vertex created", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/team")
def create_team(team: Team):
    """
    Create a team in the graph
    """
    try:
        query = f"g.addV('{team.label.value}')"
        for key, value in team.model_dump().items():
            if key != "label":
                query += f".property('{key}', '{value}')"
        result = gremlin_client.submit(query).all().result()
        return {"message": "Team vertex created", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{vertex_id}")
def read_vertex(vertex_id: str):
    """
    Read a given Vertex ID
    """
    try:
        query = f"g.V('{vertex_id}')"
        result = gremlin_client.submit(query).all().result()
        return {"vertex": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/player/{vertex_id}")
def update_player(vertex_id: str, player: PlayerUpdate):
    """
    Update a player vertex
    """
    if all_fields_none(player):
        raise HTTPException(status_code=422, detail=f"All fields are None")
    try:
        query = f"g.V('{vertex_id}')"
        for key, value in player.model_dump().items():
            if value:
                query += f".property('{key}', '{value}')"
        result = gremlin_client.submit(query).all().result()
        return {"message": "Player updated", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/team/{vertex_id}")
def update_team(vertex_id: str, team: TeamUpdate):
    """
    Update a team vertex
    """
    if all_fields_none(team):
        raise HTTPException(status_code=422, detail=f"All fields are None")
    try:
        query = f"g.V('{vertex_id}')"
        for key, value in team.model_dump().items():
            if value:
                query += f".property('{key}', '{value}')"
        result = gremlin_client.submit(query).all().result()
        return {"message": "Team updated", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/vertices/{vertex_id}")
def delete_vertex(vertex_id: str):
    try:
        query = f"g.V('{vertex_id}').drop()"
        result = gremlin_client.submit(query).all().result()
        return {"message": "Vertex deleted", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))