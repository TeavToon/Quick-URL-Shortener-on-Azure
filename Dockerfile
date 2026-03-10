# ใช้เวอร์ชันที่คุณต้องการ
FROM python:3.14.2-slim

# ตั้งค่า Environment Variable เพื่อให้ Python ไม่สร้างไฟล์ .pyc 
# และให้ Log แสดงผลใน Azure ทันที (unbuffered)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# ติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมด (อย่าลืมสร้าง .dockerignore เพื่อไม่ให้เอาไฟล์ขยะไปด้วย)
COPY . .

# คำสั่งรัน
# เพิ่ม --proxy-headers เพื่อให้ทำงานกับ Load Balancer ของ Azure ได้ถูกต้อง
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers", "--forwarded-allow-ips", "*"]