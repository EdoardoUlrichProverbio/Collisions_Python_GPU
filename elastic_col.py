import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def update_sim(frame, fig, params):
     
#----------------------------Parameters----------------------
 
    x = params["r"][0]
    y = params["r"][1]
    z = params["r"][2]
    v = params["v"]
    mask = params["mask"]
    if frame%100 == 0: print("frame: ",frame) 
    dt = params["dt"]
    size = params["size"]/1e03
    rad_dist = params["rad_dist"]/1e03
    mass = params["mass"]

    #-----------------------------update---------------------------

    #compute difference of particle positions (avoiding fot the particle withs itself)
    diffx = torch.stack([(x-xi) for xi in x])
    diffy = torch.stack([(y-yi) for yi in y])
    diffz = torch.stack([(z-zi) for zi in z])

    distance = torch.sqrt(diffx**2 + diffy**2 + diffz**2) #compunting distance matrix

    coll = distance<rad_dist
    collision = coll*mask
    id_coll = collision.nonzero()
    mass1, mass2 = mass[id_coll[:,0]], mass[id_coll[:,1]]
    vel1 = v[:,id_coll[:,0]]
    vel2 = v[:,id_coll[:,1]]
    pos1 = params["r"][:,id_coll[:,0]]
    pos2 = params["r"][:,id_coll[:,1]]

    v[:,id_coll[:,0]] -= (2*mass2 /(mass1+mass2))*torch.sum((vel1-vel2)*(pos1-pos2), axis=0)/torch.sum((pos1-pos2)**2, axis=0) * (pos1-pos2)
    v[:,id_coll[:,0]] -= (2*mass1 /(mass1+mass2))*torch.sum((vel1-vel2)*(pos1-pos2), axis=0)/torch.sum((pos2-pos1)**2, axis=0) * (pos2-pos1)

    #update
    params["r"] += v*dt


    #boundaries
    params["v"][0][params["r"][0] > 1 - size] *= -1
    params["v"][1][params["r"][1] > 1 - size] *= -1
    params["v"][2][params["r"][2] > 1 - size] *= -1

    params["v"][0][params["r"][0] < -1 + size] *= -1
    params["v"][1][params["r"][1] < -1 + size] *= -1
    params["v"][2][params["r"][2] < -1 + size] *= -1

    # Update the Plotly figure
    fig.data[0].x = params["r"][0]
    fig.data[0].y = params["r"][1]
    fig.data[0].z = params["r"][2]

    return fig.data, fig, params


