from typing import get_args, Any

def literal_type_to_dict(type_: Any) -> dict[str,str]:
    args = get_args(type_)
    mapping = {arg:arg for arg in args}
    return mapping

    