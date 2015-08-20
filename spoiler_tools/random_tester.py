def get_spoiler_ids(max_limit=10):
    from ..models import Spoiler, Title
    counter = 0
    id_list = []

    while counter < max_limit:
        id_list.append(Spoiler.random_spoiler().id)
        counter += 1
        
    return id_list

def create_unique_ids_list(ids):
    unique_copy = []
    
    for i in ids:
        if i not in unique_copy:
            unique_copy.append(i)
            
    return unique_copy

def spoiler_id_count(ids):
    id_instances = {}
    unique_ids = create_unique_ids_list(ids)

    for i in unique_ids:
        id_instances[i] = 0
        # Removed the -1 after len()
        # otherwise it wouldn't count the last one
        # needs review.
        for r in range(0, len(ids)):
            if ids[r] == i:
                ids[r] == 'counted'
                id_instances[i] += 1
    
    return id_instances
