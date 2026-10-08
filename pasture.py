def pasture_area(wire, w):
    
    l = (wire - 2 * w) / 3
    
   
    if l <= 0:
        return 0.0
        
   
    return w * l


def best_pasture(wire):
    
    a = -2 / 3
    b = wire / 3
    
    
    w = -b / (2 * a)
    
    
    l = (wire - 2 * w) / 3
    
    
    area = pasture_area(wire, w)
    
    return w, l, area
