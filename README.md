# 🤖 Instagram Followers Scraper & Auto-Follow Bot

Este repositorio contiene dos scripts en Python automatizados con Selenium para manejar tareas de scraping y seguimiento de usuarios en Instagram. **Utilizar con responsabilidad respetando los límites de la plataforma.**

---

## 📁 Contenido del Repositorio

1. **`scrape_followers.py`**  
   Extrae seguidores de una cuenta de Instagram específica y los guarda en un archivo `.txt`, evitando duplicados.

2. **`auto_follow.py`**  
   Lee usuarios desde un archivo de texto (generado por el scraper) y los sigue automáticamente hasta un límite diario seguro.

---

## ⚠️ Límites recomendados de uso en Instagram

Para evitar bloqueos o restricciones temporales por parte de Instagram, se recomienda seguir los siguientes límites:

- ✅ **60 follows por hora**  
- ✅ **150 follows por día**  
- ❌ **200 unfollows por hora**  
- ❌ **4000 unfollows por día**

> *Estos límites pueden cambiar con el tiempo. Usar con precaución.*

---

## 📌 Requisitos

- Python 3.8+
- Google Chrome
- ChromeDriver compatible
- Selenium

Instalación de dependencias:

```bash
pip install selenium
