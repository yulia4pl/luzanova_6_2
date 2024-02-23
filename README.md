input_file.csv:
Date,Distance,Reading
2024-01-01,"41m","10°C"
2024-01-01,"151ft","70°F"
2024-01-01,"15m","15°C"
2024-01-01,"100ft","62°F"
2024-01-01,"31m","15°C"
2024-01-01,"21m","17°C"
2024-01-01,"10m","15°C"
2024-01-01,"10ft","61°F"

You were given a file that contain temperature measurements, but there are two measurement units used: Celsius and Fahrenheit. We need to fix it! 
Also file includes the distance from the Earth for each reading. As you might have guessed, the distance is given in meters and feet.

Command line:
python3 main.py input_file.csv m C
python3 main.py input_file.csv ft F
python3 main.py input_file.csv m F
python3 main.py input_file.csv ft C

result_file.csv:
Date,Distance,Reading
2024-01-01,41m,10°C
2024-01-01,46m,21°C
2024-01-01,15m,15°C
2024-01-01,30m,16°C
2024-01-01,31m,15°C
2024-01-01,21m,17°C
2024-01-01,10m,15°C
2024-01-01,3m,16°C