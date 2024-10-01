# Mobility

## Integrating Mobility Data from SUMO

[SUMO (Simulation of Urban MObility)](https://eclipse.dev/sumo/) is an open-source versatile tool that allows you to model and simulate various aspects of urban transportation. Whether you’re designing smart cities, optimizing traffic flow, or analyzing vehicle behavior, SUMO provides a robust framework. In this guide, we’ll explore how to seamlessly integrate SUMO data as input for your simulations, enhancing its realism and accuracy.

Let’s drive into the details! 🚗🌐📡

### Exporting Mobility Data from SUMO

Once you’ve completed your SUMO simulation, it’s time to integrate the mobility data into your project. Ensure that the data is exported in XML format, with geolocational coordinates included. Execute the command below to generate the `fcd-output-file.xml` containing your mobility data:

```bash
sumo -c path_to_sumo_simulation.sumocfg --fcd-output.geo 1 --fcd-output fcd-output-file.xml
```


If your SUMO simulation covers a large period, the exportation and importation of the data will take a considerable amount of time. To expedite the process, modify the `.sumocfg` file by adding or editing the following lines:

```xml
<configuration ...>
    <time>
        <begin value="0"/>    <!-- Adjust the begin value to your desired time -->
        <end value="1000.0"/>   <!-- Adjust the end value to your desired time -->
    </time>
    ...
```

### Importing the Mobility Data into Your Network

To incorporate the exported mobility data into your network, use the command:

```python
sumo_file = "path_to_folder/fcd-output-file.xml"
network = Network()
network.load_sumo_data(sumo_output_file)
```

### Efficient Data Handling with JSON

Upon the initial import, the mobility data is converted and saved as a JSON file for quicker subsequent access. When calling the `load_sumo_data` method again, the JSON file is automatically utilized, bypassing the need for XML parsing:

```python
network = Network()
network.load_sumo_data()
```

### Forcing Data Reimport

If you need to refresh the data from the XML source, simply remove the existing JSON file or invoke the `load_sumo_data` method with the `force_read_xml=True` argument:

```py
sumo_file = "path_to_folder/fcd-output-file.xml"
network = Network()
network.load_sumo_data(sumo_output_file, force_read_xml=True)
```

This ensures that your network always uses the most up-to-date mobility data from your SUMO simulation.
