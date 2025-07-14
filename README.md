# Monitor de Sistema con Django y psutil

## Descripción
Aplicación web que muestra en tiempo real datos de CPU, memoria RAM, disco y sistema operativo usando Django y la librería [psutil](https://pypi.org/project/psutil/).

## Características
- % de uso de CPU.
- Uso de memoria RAM (GB y %).
- Uso de disco (GB libre, usado, total y %).
- Información del sistema operativo y núcleos físicos/lógicos.
- Actualización manual (botón “Actualizar”).
- Recarga automática cada 5 segundos (configurable en la plantilla).

## Requisitos
- Python 3.8+
- Django 5.2.x
- psutil

## Instalación

1. Clona el repositorio:
   ```bash
   git clone 
   cd monitor
