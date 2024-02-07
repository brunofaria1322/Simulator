""" Mobility Test"""

import imageio
from simulator.topology import Network

def main():
    sumo_output_file = "tests/mobility/sumo/fcd-output-file.xml"
    network = Network()

    network.load_sumo_data(sumo_output_file)

    frames = []
    for i in range(1000):
        if network.update_sumo_network(float(i)) == -1:
            break
        image = imageio.v2.imread(f'./img/img_{float(i)}.png')
        frames.append(image)

    imageio.mimsave('./example.gif', # output gif
                frames,          # array of input frames
                fps = 5)         # optional: frames per second
    
    print("Gif created successfully")

if __name__ == "__main__":
    main()

