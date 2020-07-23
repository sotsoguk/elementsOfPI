# Elements of Programming Interviews
# Chapter 04 - Primitives
# 4.11 Intersect Triangles
#  
# 

from collections import namedtuple

# kinda class like / struct
Rectangle = namedtuple('Rectangle',('x','y','w','h'))
Point = namedtuple('Point',('x','y'))

def is_Rectangle(p):
    def is_rectangular(a,b,c):
        return (a.x-b.x)*(c.x-b.x) * (a.y-b.y)*(c.y-b.y) == 0
    
    def rectangle(points):
        return is_rectangular(p[0],p[1],p[2]) and is_rectangular(p[1],p[2],p[3]) and is_rectangular(p[2],p[3],p[0])
    
    # adopt for any order of the points. 
    # In total there are 4! = 24 combinations. But 4 rotations => 6, and one can reverse the order => 3 possibilites
    if len(p) != 4:
        return False
    
    return rectangle([p[0],p[1],p[2],p[3]]) or rectangle([p[0],p[3],p[2],p[1]]) or rectangle([p[0],p[1],p[3],p[2]])

def dot(u,v):
    return u.x*v.x + u.y*v.y

def get_vec(a,b):
    return Point(b.x-a.x,b.y-a.y)

def get_normal(a):
    return Point(-a.y,a.x)

def intersect_rotated_rects(r1,r2):
    # compute edges of rectangles
    edges = []
    
    for i in range(4):
        edge_r1 = get_vec(r1[i],r1[(i+1)%4])
        edge_r2 = get_vec(r2[i],r2[(i+1)%4])
        edges.append(edge_r1)
        edges.append(edge_r2)
    
    for e in edges:
        # get normal for edge
        projline = get_normal(e)
        min1,max1,min2,max2 = 1000,-1000,1000,-1000
        


    #get edges of first rectangle,compute
    
def intersect_rectangle(a,b):
    def is_intersect(r1,r2):
        return (a.x+a.w >= b.x and b.x+b.w>=a.x 
                and b.y+b.w >= a.y and a.y + a.h >= b.y)
    
    if not is_intersect(a,b):
        return Rectangle(0,0,-1,-1) # no intersection

    xi = max(a.x,b.x)
    yi = max(a.y,b.y)
    return Rectangle(
        xi,
        yi,
        min(a.x+a.w,b.x+b.w)-xi,
        min(a.y+a.h,b.y+b.h)-yi
    )


if __name__ == "__main__":
    r1 = Rectangle(10,10,20,20)
    r2 = Rectangle(30,30,10,10)
    print(intersect_rectangle(r1,r2))

    p1 = Point(0,0)
    p2 = Point(10,10)
    p3 = Point(0,10)
    p4 = Point(10,1)
    ps = [p1,p2,p3,p4]
    print(is_Rectangle(ps))