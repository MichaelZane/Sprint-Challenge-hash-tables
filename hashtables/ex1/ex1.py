def get_indices_of_item_weights(weights, length, limit):
    cache = {}
       
    for i in range(length):       
    #loop list - get() key if present         
        result = cache.get(limit - weights[i])
      
        if result != None:
            # print(i, result)
            return (i, result)   
         
    # add to cache when not in it
        cache[weights[i]] = i
        # print(cache)
            
    return None

if __name__ == "__main__":
    pass