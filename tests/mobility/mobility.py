""" Mobility Test"""

import imageio
from src.topology import Network

"""
cd ./tests/mobility/sumo

# Run the simulation
# Berlin - biggest
sumo -c ./BeST/berlin.sumocfg --fcd-output.geo 1 --fcd-output fcd-output-file.xml
# smallest
sumo -c ./MannheimSumoModel/osm.sumocfg --fcd-output.geo 1 --fcd-output fcd-output-file.xml
"""


def main():
    sumo_output_file = "tests/mobility/sumo/fcd-output-file.xml"
    network = Network()

    network.load_sumo_data(sumo_output_file)

    frames = []
    for i in range(1000):
        if network.update_sumo_network(float(i)) == -1:
            break
        image = imageio.v2.imread(f"./img/img_{float(i)}.png")
        frames.append(image)

    imageio.mimsave(
        "./example.gif",  # output gif
        frames,  # array of input frames
        fps=5,  # optional: frames per second
        loop=0,  # optional: loop the gif
    )

    print("Gif created successfully")


if __name__ == "__main__":
    main()
