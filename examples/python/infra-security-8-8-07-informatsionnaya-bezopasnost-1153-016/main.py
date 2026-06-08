from fastapi import FastAPI, Request, Depends

app = FastAPI()

def get_feature_flags():
    return FeatureFlagService(config_source=RemoteConfigSource())

@app.get("/checkout")
async def checkout(
    request: Request,
    flags: FeatureFlagService = Depends(get_feature_flags)
):
    user_id = request.headers.get("X-User-Id")
    user_segment = request.headers.get("X-User-Segment")
    
    context = {
        "user_id": user_id,
        "user_segment": user_segment,
        "environment": os.environ.get("ENVIRONMENT"),
    }
    
    if flags.is_enabled("new_checkout_flow", context):
        return await new_checkout_process(request)
    else:
        return await legacy_checkout_process(request)

@app.get("/recommendations/{user_id}")
async def get_recommendations(
    user_id: str,
    flags: FeatureFlagService = Depends(get_feature_flags)
):
    context = {"user_id": user_id}
    
    algorithm = flags.get_variant("recommendation_algorithm", context)
    
    if algorithm == "cf_v2":
        return collaborative_filtering_v2(user_id)
    elif algorithm == "cb_v3":
        return content_based_v3(user_id)
    elif algorithm == "hybrid_v1":
        return hybrid_v1(user_id)
