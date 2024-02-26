package main

import (
	"fmt"
	"math/rand"
	"time"

	"github.com/eclipse/paho.mqtt.golang"
)

// MQTT Broker settings
const (
	brokerAddress = "localhost"
	port          = 1883
	topic         = "data/sensor1"
)

// SensorData represents the structure of sensor readings
type SensorData struct {
	CO       float64 `json:"CO"`
	NO2      float64 `json:"NO2"`
	Ethanol  float64 `json:"Ethanol"`
	Hydrogen float64 `json:"Hydrogen"`
	Ammonia   float64 `json:"Ammonia"`
}

// GenerateSensorData simulates sensor readings
func GenerateSensorData() SensorData {
	return SensorData{
		CO:       rand.Float64() * 1000,
		NO2:      rand.Float64() * 10,
		Ethanol:  rand.Float64() * 490 + 10, // range: 10 to 500
		Hydrogen: rand.Float64() * 1000,
		Ammonia:  rand.Float64() * 500,
	}
}

// PublishSensorData publishes sensor data to MQTT
func PublishSensorData(client mqtt.Client) {
	for {
		sensorData := GenerateSensorData()
		token := client.Publish(topic, 0, false, fmt.Sprintf("%v", sensorData))
		token.Wait()
		fmt.Printf("Published: %+v\n", sensorData)
		time.Sleep(5 * time.Second) // Adjust the interval as needed
	}
}

func main() {
	// MQTT setup and connection
	opts := mqtt.NewClientOptions().AddBroker(fmt.Sprintf("tcp://%s:%d", brokerAddress, port)).SetClientID("sensor-client")
	client := mqtt.NewClient(opts)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		fmt.Println("Error connecting to MQTT broker:", token.Error())
		return
	}

	defer func() {
		// Gracefully handle interrupt (Ctrl+C) to disconnect from MQTT broker
		client.Disconnect(250)
		fmt.Println("Simulation stopped.")
	}()

	// Start the simulation
	PublishSensorData(client)
}
