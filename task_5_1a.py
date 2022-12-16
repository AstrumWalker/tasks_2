PC_Names= {
    "Paradise": {
        "OS": "Windows 10 Pro",
        "Processor": "Intel Core i5-10400F",
        "RAM": "16384 MB",
        "Video card": "Nvidia GeForce RTX 2060 6G",
        "ROM": "1TB HDD Barracuda 7200prm",
        "PSU": "DeepCool DN 600W",
        "Motherboard": "GIGABYTE H410M H V3 LGA 1200",
    },
    "Tank": {
        "OS": "Windows 10 Home",
        "Processor": "AMD Ryzen 5 2600 six core",
        "RAM": "16384 MB",
        "Video card": "Nvidia GeForce RTX 3070 8G",
        "ROM": "128 GB SSD AData",
        "PSU": "Fractal Design Ion+ 760P 760W",
        "Motherboard": "GIGABYTE B550 AORUS ELITE V2 AM4",
    },
    "Stitch": {
        "OS": "Windows 11 Pro",
        "Processor": "AMD Ryzen Threadripper PRO 3995WX",
        "RAM": "1024 GB",
        "Video card": "Nvidia PNY Quadro RTX 6000 24G",
        "ROM": "7680 GB Intel Optane D7-P5510",
        "PSU": "Thermaltake Toughpower TF1 1550W",
        "Motherboard": "ASUS Pro WS WRX80E-SAGE SE WIFI",
    },
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(PC_Names[device][parameter])