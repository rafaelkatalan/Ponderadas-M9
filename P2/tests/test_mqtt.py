# tests/test_publisher.py
import time
from unittest.mock import MagicMock, patch
import paho.mqtt.client as mqtt
from pyTdd.mqtt.publisher import generate_sensor_data, publish_sensor_data

def test_generate_sensor_data():
    sensor_data = generate_sensor_data()
    assert isinstance(sensor_data, dict)
    assert "CO" in sensor_data
    assert "NO2" in sensor_data
    assert "Ethanol" in sensor_data
    assert "Hydrogen" in sensor_data
    assert "Ammonia" in sensor_data

def test_publish_sensor_data():
    # Mocking the MQTT client
    mock_client = MagicMock(spec=mqtt.Client)
    mock_client.publish = MagicMock()

    # Mocking time.sleep to avoid long waits during tests
    with patch('time.sleep'):
        publish_sensor_data(mock_client)

    # Asserting that publish was called
    assert mock_client.publish.called

    # Asserting that publish was called with the correct topic
    expected_topic = "data/sensor1"
    assert mock_client.publish.call_args[0][0] == expected_topic

    # Asserting that publish was called with a string payload
    assert isinstance(mock_client.publish.call_args[0][1], str)

    # Asserting that disconnect is called when KeyboardInterrupt is raised
    with patch('builtins.print'), patch('builtins.input', side_effect=KeyboardInterrupt):
        try:
            publish_sensor_data(mock_client)
        except KeyboardInterrupt:
            pass  # Expected KeyboardInterrupt, no need to handle it here

    assert mock_client.disconnect.called

if __name__ == '__main__':
    # Run tests with: pytest tests/test_publisher.py
    pass
