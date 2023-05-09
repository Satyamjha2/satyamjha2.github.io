## Random walk, but in polar co-ordinates.
## Also the random walk in r and theta axes are completely independent (unlike the x-y co-ordinate system)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def gen_polar_picture(angle_dtheta, N_step):
    color_list_gold_1=['#FFE964','#BA7322','#FFDC6D','#FFFFB5','#FCFDF6','#FFFF9C','#FDDC53','#D49721','#BB6E03','#5B1F03']
    color_list_gold_cyclic=['#FFE964','#BA7322','#FFDC6D','#FFFFB5','#FCFDF6','#FFFF9C','#FDDC53','#D49721','#BB6E03','#5B1F03','#BB6E03','#D49721','#FDDC53','#FFFF9C','#FCFDF6','#FFFFB5','#FFDC6D','#BA7322','#FFE964']
    color_list_gold_2=['#FFE964','#BA7322','#8B3E04','#FFDC6D','#FFFFB5','#FCFDF6','#FFFF9C','#FDDC53','#D49721','#BB6E03','#5B1F03']
    norm=plt.Normalize(-2,2),
    gold_1 = colors.LinearSegmentedColormap.from_list("", color_list_gold_1)
    gold_2 = colors.LinearSegmentedColormap.from_list("", color_list_gold_2)

    gold_cyclic = colors.LinearSegmentedColormap.from_list("", color_list_gold_cyclic)

    ## Random walk, but in polar co-ordinates.
    ## Also the random walk in r and theta axes are completely independent (unlike the x-y co-ordinate system)
    N_step=N_step*10**4
    plt.rcParams['figure.facecolor'] = 'black'
    plt.figure(figsize=(10,10))
    r=np.zeros(N_step)
    theta=np.zeros(N_step)
    Z= np.zeros(N_step,dtype='complex128')
    Z[0]=0
    theta=0
    r=0
    np.random.seed(0)

    del_theta=0.1*angle_dtheta                   ##step size for angle
    del_r=1                           ##step size for radius
    for i in range(1, N_step):
        k_r=np.random.choice(a=np.arange(3)-1,p=[0.2,0.6,0.2])     ## biased RW to throu the particle in one direction
        k_theta=np.random.choice(a=np.arange(3)-1,p=[0.3,0.5,0.2]) ## biased RW to make a spiral structure
        r+=del_r*k_r
        theta+=del_theta*k_theta
        Z[i]=1*r*np.exp(1j*theta)
    plt.scatter(Z.real,Z.imag,s=1,c=np.linspace(0,1,N_step),alpha=1,cmap=gold_cyclic)                        ##scatter plot the point.  's' specifies the markersize
    #plt.scatter(Z.real,Z.imag,s=1,c='w',alpha=1)                        ##scatter plot the point.  's' specifies the markersize
    plt.axis('equal')
    plt.axis('off')
    plt.savefig('./static/polar.png')