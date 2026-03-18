# Quick URL Shortener on Azure

โปรเจกต์บริการย่อลิงก์ (URL Shortener) ที่พัฒนาด้วย **FastAPI** พร้อมใช้งานร่วมกับฐานข้อมูล SQLite และรองรับการทำงานบน **Azure App Service** ด้วย Docker

🚀 **Live Demo:** [เข้าสู่เว็บไซต์คลิกที่นี่](https://quick-url-shortener-on-azure-egcwa3fbeugud6dw.southeastasia-01.azurewebsites.net/)

## 🛠 เทคโนโลยีที่ใช้ (Tech Stack)
* **Backend:** Python (รองรับการใช้งานผ่าน Base Image `python:3.14.2-slim`) และเว็บเฟรมเวิร์ก FastAPI
* **Database:** SQLite (จัดการผ่าน ORM อย่าง SQLAlchemy)
* **Frontend:** HTML, JavaScript พื้นฐาน และ Tailwind CSS (ผ่าน CDN)
* **Deployment:** Docker และ Azure App Service

## ✨ ฟีเจอร์ (Features)
* **ย่อลิงก์ (Shorten URL):** แปลง URL ที่ยาวให้กลายเป็นลิงก์สั้นแบบสุ่ม
* **ระบบ Redirect:** เมื่อผู้ใช้เข้าถึงผ่านลิงก์สั้น ระบบจะทำการพาไปยัง URL ต้นฉบับโดยอัตโนมัติ
* **หน้า UI พร้อมใช้งาน:** มีหน้าเว็บไซต์แบบเรียบง่ายสำหรับกรอกและรับลิงก์สั้นได้ทันที

## 🚀 การติดตั้งและรันโปรเจกต์ในเครื่อง (Local Development)

1. **ดาวน์โหลดโค้ด** และเข้าไปที่โฟลเดอร์โปรเจกต์
2. **ติดตั้งไลบรารีที่จำเป็น** จากไฟล์ `requirements.txt`:
   ```bash
   pip install -r requirements.txt
