document.addEventListener("DOMContentLoaded", () => {
  const weatherInfo = document.getElementById("weather-info");
  const locationInput = document.getElementById("location");
  const getWeatherButton = document.getElementById("get-weather");

  getWeatherButton.addEventListener("click", async () => {
    const location = locationInput.value.trim();

    if (location === "") {
      weatherInfo.innerText = "Please enter a location.";
      return;
    }

    const apiKey = "ea8ccd864d96ebeffa65ea13776a4b49"; 
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;

    try {
      const response = await fetch(apiUrl);

      if (!response.ok) {
        throw new Error("Invalid location. Please try again.");
      }

      const weatherData = await response.json();
      const temperature = weatherData.main.temp;
      const description = weatherData.weather[0].description;

      weatherInfo.innerText = `Temperature: ${temperature}°C\nDescription: ${description}`;
    } catch (error) {
      weatherInfo.innerText = error.message;
    }
  });
});

