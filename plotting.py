
import numpy as np
import plotly.graph_objects as go


def cube(fig):

    cube_vertices = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1], 
                            [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]])

    # Define cube edges
    cube_edges = np.array([(0,1), (0,2), (0,3), (1,6), (1,5), (2,4), (2,6), (3,5), (3,4), (4,7), (5,7), (6,7)])


    # Define the trace for cube edges
    edges_x = []
    edges_y = []
    edges_z = []
    for edge in cube_edges:
        edges_x.extend([cube_vertices[edge[0], 0], cube_vertices[edge[1], 0], None])
        edges_y.extend([cube_vertices[edge[0], 1], cube_vertices[edge[1], 1], None])
        edges_z.extend([cube_vertices[edge[0], 2], cube_vertices[edge[1], 2], None])


    fig.add_trace(
    go.Scatter3d(
    x=edges_x,
    y=edges_y,
    z=edges_z,
    mode='lines',
    line=dict(width=2, color='white'))
    )

    return fig


def set_figure(x,y,z, size, colors):

        fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            sizemode='diameter',
            sizeref=0.5,
            size=size,
            color=colors,
            colorscale='Viridis',
            opacity=0.8,
        ),
        # Add the uirevision parameter to enable scene rotation
        uirevision=True
        )])
        
        return fig

def animate_setting(fig, space_size):
    fig.update_layout(scene=dict(
                    xaxis=dict(showticklabels=False,range=[-space_size,space_size],showgrid=False,title='', backgroundcolor="black", showline=False,showbackground=False, zeroline= False),
                    yaxis=dict(showticklabels=False,range=[-space_size,space_size],showgrid=False,title='', backgroundcolor="black", showline=False,showbackground=False, zeroline= False),
                    zaxis=dict(showticklabels=False,range=[-space_size,space_size],showgrid=False,title='', backgroundcolor="black", showline=False,showbackground=False, zeroline= False),
                    ),
                  updatemenus=[dict(type='buttons',
                                    showactive=False,
                                    buttons=[dict(label='Play',
                                                  method='animate',
                                                  args=[None,
                                                        dict(frame=dict(duration=5),
                                                             fromcurrent=True,
                                                             transition=dict(duration=0)
                                                             ),
                                                        dict(frame=dict(duration=0, redraw=False),
                                                             mode='immediate',
                                                             transition=dict(duration=0)
                                                             )
                                                        ]
                                                  ),
                                             dict(label='Stop',
                                                  method='animate',
                                                  args=[[None],
                                                        dict(frame=dict(duration=0, redraw=False),
                                                             mode='immediate',
                                                             transition=dict(duration=0)
                                                             )
                                                        ]
                                                  ),
                                            dict(label="Restart", 
                                                 method="animate", 
                                                 args=[None,
                                                       dict(frame=dict(duration= 5,
                                                                       fromcurrent= False, 
                                                                       redraw= True),
                                                            mode='immediate', 
                                                             )
                                                        ]
                                                  )
                                             ]
                                    )
                             ],
                  paper_bgcolor="black",
                  scene_bgcolor="black",
                  scene_aspectmode='data',
                  title='Particle Simulation',
                  showlegend=False,
                  width=1000,
                  height=800,
                  
                  )
    return fig