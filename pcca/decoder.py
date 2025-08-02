
def positional_analysis(inscriptions):
    """
    PCCA Core Algorithm: Positional Pattern Detection
    Returns: {position_1: signs, position_2: signs, ...}
    """
    results = {"position_1": {}, "position_2": {}, "position_3": {}}
    
    for item in inscriptions:
        signs = item["signs"]
        for i, sign in enumerate(signs):
            pos = f"position_{i+1}"
            results[pos][sign] = results[pos].get(sign, 0) + 1
            
    return results

def validate_context(inscriptions):
    """Archaeological Context Validator"""
    # Implementation example
    context_codes = {}
    for item in inscriptions:
        ctx = item["context"]
        sign_combo = "".join(item["signs"])
        context_codes.setdefault(ctx, {})[sign_combo] = context_codes[ctx].get(sign_combo, 0) + 1
    
    return context_codes
